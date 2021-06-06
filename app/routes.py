from app import db
from .models.planets import Planet
from flask import Blueprint
from flask import request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/", methods=["GET"])
def get_all_planets():
    return {
        "name": "Mercury",
        "surface_area": "4,797,000km2",
        "description": ["The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon."]
    }

@planets_bp.route("/", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(name = request_body["name"],
                        description =  request_body["description"],
                        surface_area = request_body["surface_area"])

    db.session.add(new_planet)
    db.session.commit()

    return (f"planet {new_planet.name} has been created", 201)



# As a client, I want to send a request with new valid planet data and get a success response, so that I know the API saved the planet data
# As a client, I want to send a request to get all existing planets, so that I can see a list of planets, with their id, name, description, and other data of the planet.
# As a client, I want to send a request to get one existing planet, so that I can see the id, name, description, and other data of the planet.