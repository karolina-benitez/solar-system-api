import pytest
from app import create_app
from app import db
from app.models.planets import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    # Arrange
    planet_1 = Planet(name="Mercury",
                      description="The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon.",
                      surface_area="74,797,000km2")

    planet_2 = Planet(name="Venus",
                      description="Similar in size and structure to Earth, Venus has been called Earth's twin.",
                      surface_area="460,234,317km2")

    planet_3 = Planet(name="Neptune",
                      description="Dark, cold and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system.",
                      surface_area="7,618,272,763km2")

    db.session.add_all([planet_1, planet_2, planet_3])
    db.session.commit()