from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from .models.planets import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []

        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "surface_area": planet.surface_area
            })
        return jsonify(planets_response, 200)

    elif request.method == "POST":
        request_body = request.get_json()

        new_planet = Planet(name = request_body["name"],
                            description =  request_body["description"],
                            surface_area = request_body["surface_area"])

        db.session.add(new_planet)
        db.session.commit()

        return {
            "success": True,
            "message": f"planet {new_planet.name} has been created"
            }, 201


# As a client, I want to send a request to get one existing planet, so that I can see the id, name, description, and other data of the planet.