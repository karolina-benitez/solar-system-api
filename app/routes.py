from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from .models.planets import Planet
from flask import make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/", methods=["POST", "GET"])
def handle_planets():
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

        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            surface_area=request_body["surface_area"])

        db.session.add(new_planet)
        db.session.commit()

        return {
            "success": True,
            "message": f"planet {new_planet.name} has been created"
        }, 201


@planets_bp.route("/<planet_id>", methods=["GET", "DELETE", "PUT"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "surface_area": planet.surface_area
        }
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} deleted sucessfully")
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.surface_area = form_data["surface_area"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated!")
