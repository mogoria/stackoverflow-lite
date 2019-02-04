from app import app


def test_app_in_debug():
    assert app.config['DEBUG'] == True


def test_db():
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/stackoverflow-lite'
