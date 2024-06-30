
from flask import Blueprint, render_template, request
import joblib
import numpy as np

main = Blueprint('main', __name__)

# Load the trained model
model = joblib.load('model/parkinsons_model.pkl')

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        form_data = request.form.to_dict()
        features = [float(value) for value in form_data.values()]
        
        # Predict using the model
        prediction = model.predict([features])
        result = 'Positive' if prediction[0] == 1 else 'Negative'
        
        return render_template('index.html', result=result)
    return render_template('index.html')
    