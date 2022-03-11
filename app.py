from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np


app = Flask(__name__, static_url_path='/static/', static_folder='/static/')
pkl_file = open('taipei_house_price_model.pickle', 'rb')
model = pickle.load(open('taipei_house_price_model.pickle', 'rb'))
index_dict = pickle.load(pkl_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        result = request.form

        index_dict = pickle.load(open('cat', 'rb'))
        location_cat = pickle.load(open('location_cat', 'rb'))

        new_vec = np.zeros(27)

        result_location = result['district']


        new_vec[index_dict[str(result['district'])]] = 1

        new_vec[0] = result['land shifting total area']
        new_vec[1] = result['num_building']
        new_vec[2] = result['num_land']
        new_vec[3] = result['num_garage']
        new_vec[4] = result['total floor number']
        new_vec[5] = result['complete year']
        new_vec[6] = result['num_room']
        new_vec[7] = result['compartment']
        new_vec[8] = result['management org']
        new_vec[9] = result['main building area']
        new_vec[10] = result['subsidiary building area']
        new_vec[11] = result['balcony area']
        new_vec[12] = result['elevator']
        new_vec[13] = result['unit ntd']
        new_vec[14] = result['Carpark']

        new = [new_vec]

        prediction = np.exp(model.predict(new))

        return render_template('index.html', Predict_score = 'The estimate price is {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)