from flask import Flask, render_template, request
import pandas as pd
import pandas as pd
import numpy as np

# Create a random dataset
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh']
crime_types = ['Murder', 'Robbery', 'Rape', 'Burglary', 'Theft']
crime_rates = np.random.rand(25)

data = {'State/UT': np.repeat(states, 5),
        'Crime Head': np.tile(crime_types, 5),
        'Crime Rate': crime_rates}

crime_data = pd.DataFrame(data)

# Save the dataset to a CSV file
crime_data.to_csv('crime_data.csv', index=False)


app = Flask(__name__)

# Load the crime data
crime_data = pd.read_csv('crime_data.csv')

# Define a function to filter the data based on state and crime type
def filter_data(state, crime_type):
    filtered_data = crime_data[(crime_data['State/UT'] == state) & (crime_data['Crime Head'] == crime_type)]
    return filtered_data

@app.route('/')
def index():
    states = sorted(crime_data['State/UT'].unique())
    crime_types = sorted(crime_data['Crime Head'].unique())
    return render_template('index.html', states=states, crime_types=crime_types)

@app.route('/', methods=['POST'])
def predict():
    state = request.form.get('state')
    crime_type = request.form.get('crime_type')
    filtered_data = filter_data(state, crime_type)
    predicted_value = filtered_data['Crime Rate'].values[0]
    return render_template('index.html', states=sorted(crime_data['State/UT'].unique()), crime_types=sorted(crime_data['Crime Head'].unique()), predicted_value=predicted_value)

if __name__ == '__main__':
    app.run(debug=True)
