from flask import Flask
from app.database import db
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables
    load_dotenv(override=True)

    # Create Flask app
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@"
        f"{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"
    )

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    with app.app_context():
        from app.routes import bp as routes_bp
        app.register_blueprint(routes_bp)

        # Ensure tables are created
        db.create_all()

    return app