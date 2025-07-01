from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load model and scaler
ridge_model = pickle.load(open('models/ridge_model.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Route for welcome page
@app.route('/')
def index():
    return render_template('index.html')  # This is your welcome.html

# Route for form page (GET) and result page (POST) – using home.html
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            scaled_data = standard_scaler.transform(new_data)
            result = ridge_model.predict(scaled_data)

            return render_template('home.html', results=round(result[0], 2))
        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")
    else:
        return render_template('home.html')  # On GET, show the blank form

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
