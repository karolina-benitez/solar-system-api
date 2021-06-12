def test_get_one_planet_by_id_no_data(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404


def test_get_one_planet_by_id(client, three_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    description = response_body["description"]
    # Assert
    assert response.status_code == 200
    assert response_body['description'] == "The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon."
    assert response_body == {
        "description": "The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon.",
        "id": 1,
        "name": "Mercury",
        "surface_area": "74,797,000km2"
    }


def test_get_planets(client, three_saved_planets):
    # Act
    response = client.get("/planets/")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [[{
        "description": "The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon.",
        "id": 1,
        "name": "Mercury",
        "surface_area": "74,797,000km2"}, {
        "description": "Similar in size and structure to Earth, Venus has been called Earth's twin.",
        "id": 2,
        "name": "Venus",
        "surface_area": "460,234,317km2"}, {
        "description": "Dark, cold and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system.",
        "id": 3,
        "name": "Neptune",
        "surface_area": "7,618,272,763km2"

    }], 200]
