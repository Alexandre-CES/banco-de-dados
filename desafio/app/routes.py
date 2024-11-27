from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Partner
from geoalchemy2 import WKTElement
from app.helpers import format_multipolygon, format_error
from sqlalchemy import select
from sqlalchemy import func

bp = Blueprint('routes', __name__)

@bp.route('/create', methods=['POST'])
def create():
    '''Create new partner'''

    try:
        data = request.json

        #checking if id exit
        partnerId = db.session.execute(select(Partner).where(Partner.id == data['id'])).scalar_one_or_none()
        if partnerId:
            return jsonify(message='Id already exist!'), 400

        #checking if document exist
        partnerDocument = db.session.execute(select(Partner).where(Partner.document == data['document'])).scalar_one_or_none()
        if partnerDocument:
            return jsonify(message='Document already exist!'), 400

        #parsing to wkt
        multipolygon_wkt = f"MULTIPOLYGON({format_multipolygon(data['coverageArea']['coordinates'])})"
        point_wkt = f"POINT({data['address']['coordinates'][0]} {data['address']['coordinates'][1]})"

        #creating partner
        partner = Partner(
            id=data['id'],
            tradingName=data['tradingName'],
            ownerName=data['ownerName'],
            document=data['document'],
            coverageArea=WKTElement(multipolygon_wkt, srid=4326),
            address=WKTElement(point_wkt, srid=4326)
        )

        #adding to database
        db.session.add(partner)
        db.session.commit()
        return jsonify(message="Partner added"), 201
    
    #errors
    except TypeError as te:
        return format_error("Invalid data type", details=str(te), code=400)
    except KeyError as ke:
        return format_error("Missing data", details=f"Missing key: {ke}", code=400)
    except Exception as ex:
        return format_error("Unexpected error", details=str(ex), code=500)
    

@bp.route('/loadById', methods=['POST'])
def load():
    '''Receive id and load corresponding partner'''

    try:
        request_id = (request.json)['id']

        partner = db.session.execute(select(Partner).where(Partner.id == request_id)).scalar_one_or_none()

        if partner:
            partner = partner.as_dict()
            return jsonify(partner), 200
        else:
            return jsonify(message='partner não encontrado'), 400

    #errors
    except TypeError as te:
        return format_error('Invalid data type: ', details=str(te), code=400)
    except ValueError as ve:
        return format_error('Value error: ', details=str(ve), code=400)
    except KeyError as ke:
        return format_error("Missing data", details=f"Missing key: {ke}", code=400)
    except Exception as ex:
        return format_error('unexpected error', details=str(ex),code=500)

@bp.route('/search', methods=['POST'])
def search():
    '''Search nearest partner from given coordinates'''

    try:
        request_coordinates = (request.json)['coordinates']
        point = WKTElement(f"POINT({request_coordinates[0]} {request_coordinates[1]})", srid=4326)

        #Consult nearest partner and distance
        nearest_partner = (
            db.session.query(Partner)
            .filter(func.ST_Within(point, Partner.coverageArea))
            .order_by(func.ST_Distance(Partner.coverageArea, point))
            .first()
        )
        
        if nearest_partner:
            return jsonify(nearest_partner=nearest_partner.as_dict()), 200
        else:
            return jsonify(message="No partner found covering the given location"), 404

    #errors
    except TypeError as te:
        return format_error('Invalid data type: ', details=str(te), code=400)
    except ValueError as ve:
        return format_error('Value error: ', details=str(ve), code=400)
    except KeyError as ke:
        return format_error("Missing data", details=f"Missing key: {ke}", code=400)
    except Exception as ex:
        return format_error('unexpected error', details=str(ex),code=500)