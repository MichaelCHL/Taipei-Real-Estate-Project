from flask import Flask, request, jsonify
import util

app = Flask(__name__)
# @app.route('/hello')
# def hello():
#     return 'hi'




@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        location = request.form.get('location')
        land_shifting = float(request.form.get('land shifting total area'))
        num_building = int(request.form.get('num_building'))
        num_land = int(request.form.get('num_land'))
        num_garage = int(request.form.get('num_garage'))
        total_floor_num = int(request.form.get('total floor number'))
        complete_year = int(request.form.get('complete year'))
        compartment = int(request.form.get('compartment'))
        manage_org = int(request.form.get('management org'))
        carpark_price = float(request.form.get('carpark total price'))
        main_building_area = float(request.form.get('main building area'))
        subsidiary_building_area = float(request.form.get('subsidiary building area'))
        balcony_area = float(request.form.get('balcony area'))
        elevator = int(request.form.get('elevator'))
        unit_ntd = int(request.form.get('unit ntd'))
        room_num = int(request.form.get('num_room'))

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, land_shifting, num_building, num_land, num_garage, total_floor_num, complete_year, compartment, manage_org, carpark_price, main_building_area, subsidiary_building_area, balcony_area, elevator, unit_ntd, room_num)
        })

        response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print('Starting Python Flash Server For Home Price Prediction...')
    util.load_saved_artifacts()
    app.run(debug=True)