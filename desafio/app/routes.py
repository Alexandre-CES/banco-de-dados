from flask import Blueprint, jsonify
from app.database import db
from app.models import Partner
from geoalchemy2 import WKTElement

bp = Blueprint('routes', __name__)

@bp.route('/test')
def home():
    partner = Partner(
        id=1,
        tradingName="Adega da Cerveja - Pinheiros",
        ownerName="Zé da Silva",
        document="1432132123891/0001",
        coverageArea=WKTElement(
            'MULTIPOLYGON(((30 20, 45 40, 10 40, 30 20)), ((15 5, 40 10, 10 20, 5 10, 15 5)))',
            srid=4326
        ),
        address=WKTElement(
            'POINT(-46.57421 -21.785741)',
            srid=4326
        )
    )
    db.session.add(partner)
    db.session.commit()
    return jsonify(message="Partner added"), 201
