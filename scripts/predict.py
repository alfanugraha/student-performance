import pickle
from flask import Flask, request, jsonify

with open('dtree_model.pkl', 'rb') as f_in:
    model, dv = pickle.load(f_in)

app = Flask('student-performance-prediction')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    [{
        'school': 'GP',
        'sex': 'M',
        'age': 16,
        'address': 'U',
        'famsize': 'GT3',
        'pstatus': 'T',
        'medu': '5th to 9th grade',
        'fedu': 'primary education (4th grade)',
        'mjob': 'other',
        'fjob': 'other',
        'reason': 'home',
        'guardian': 'mother',
        'traveltime': '<15 min',
        'studytime': '5 to 10 hours',
        'failures': 3,
        'schoolsup': 'no',
        'famsup': 'yes',
        'paid': 'yes',
        'activities': 'yes',
        'nursery': 'yes',
        'higher': 'yes',
        'internet': 'yes',
        'romantic': 'yes',
        'famrel': 'excellent',
        'freetime': 'high',
        'goout': 'very high',
        'dalc': 'very low',
        'walc': 'average',
        'health': 'very good',
        'absences': 0,
        'g1': 20,
        'g2':200
    }]
    '''
    student = request.get_json()

    X = dv.transform([student])
    y_pred = model.predict(X)[0]

    result = {
        'predicted_final_grade': int(y_pred)
    }

    return jsonify(result)

@app.route('/')
def index():
    return jsonify({'message': 'Student Performance Prediction API is running.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)