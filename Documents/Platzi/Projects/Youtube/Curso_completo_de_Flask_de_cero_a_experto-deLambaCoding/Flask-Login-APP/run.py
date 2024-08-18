from venv import create
from app import create_app, db
from app.auth.models import User


flask_scrapy_app =  create_app("prod")
with flask_scrapy_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name="test").first():
        User.create_user(
            user="test",
            email="test-testing@test.com",
            password="test**123"
        )
flask_scrapy_app.run()
