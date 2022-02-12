import numpy as np
import pickle
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
import folium

svm_model = pickle.load(open('svm_model.sav', 'rb'))
rfc_model = pickle.load(open('rfc_model.sav', 'rb'))
rgb_model = pickle.load(open('rgb_model.sav', 'rb'))

model = svm_model

app = Flask(__name__)

# Classes
class Site:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

site = Site(-2.174854, -79.879308)


@app.route('/')
def index():
    start_coords = (site.lat, site.lon)
    folium_map = folium.Map(location=start_coords, width=750, height=500, zoom_start=18)
    return folium_map._repr_html_()

@app.route('/predict',methods=['POST'])
def predict():

    raw_features = [float(x) for x in request.form.values()]
    new_coord = (raw_features[0], raw_features[1])
    final_features = [np.array(raw_features)]
    prediction = model.predict(final_features)

    folium_map = folium.Map(location=new_coord, width=750, height=500, zoom_start=18)

    return render_template('frontend/src/App.js', total_sin=f"Numero de siniestros: {str(prediction)}", mapa=folium_map)


if __name__ == '__main__':
    app.run(debug=True)

