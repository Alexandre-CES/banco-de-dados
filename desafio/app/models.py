from app.database import db
from geoalchemy2 import Geometry
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
import json


class Partner(db.Model):
    __tablename__ = 'partners'

    #simple objects
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    tradingName: Mapped[str] = mapped_column(db.String(255), nullable=False)
    ownerName: Mapped[str] = mapped_column(db.String(255), nullable=False)
    document: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)

    #Geometry objects
    coverageArea: Mapped[object] = mapped_column(Geometry(geometry_type='MULTIPOLYGON', srid=4326), nullable=False)
    address: Mapped[object] = mapped_column(Geometry('POINT', srid=4326), nullable=False)

    def as_dict(self):
        session = db.session
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        # parse geometry to GeoJSON
        data['coverageArea'] = session.scalar(func.ST_AsGeoJSON(self.coverageArea)) if self.coverageArea else None
        data['address'] = session.scalar(func.ST_AsGeoJSON(self.address)) if self.address else None

        # parse GeoJSON strings to dicts
        if data['coverageArea']:
            data['coverageArea'] = json.loads(data['coverageArea'])
        if data['address']:
            data['address'] = json.loads(data['address'])

        return data