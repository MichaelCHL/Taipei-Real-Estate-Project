import pickle
import numpy as np
import math
import sklearn

from flask import json


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, land_shifting, num_building, num_land, num_garage, total_floor_num, complete_year,
                        room_num, compartment, manage_org, carpark_price, main_building_area, subsidiary_building_area,
                        balcony_area, elevator, unit_ntd):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = land_shifting
    x[1] = num_building
    x[2] = num_land
    x[3] = num_garage
    x[4] = total_floor_num
    x[5] = complete_year
    x[6] = room_num
    x[7] = compartment
    x[8] = manage_org
    x[9] = carpark_price
    x[10] = main_building_area
    x[11] = subsidiary_building_area
    x[12] = balcony_area
    x[13] = elevator
    x[14] = unit_ntd
    if loc_index >= 0:
        x[loc_index] = 1

    #return __model.predict([x])[0]
    return round(math.exp(__model.predict([x])[0]))

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('Loading saved artifacts..start')
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[16:]

    with open('./artifacts/taipei_house_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('Loading saved artifacts..done')



if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_location_names())
    print(get_estimated_price('district_Beitou District', 29.12, 1, 1, 1, 9, 94, 4, 1, 1, 0, 92.15, 6.97, 9.5, 1, 113512))