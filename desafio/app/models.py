from app.database import db
from geoalchemy2 import Geometry
from sqlalchemy.orm import Mapped, mapped_column

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
