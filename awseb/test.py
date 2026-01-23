import requests

host = 'student-performance-env.eba-mergmnms.us-east-1.elasticbeanstalk.com'
url = f'http://{host}/predict'

student = {
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
}

response = requests.post(url, json=student)

print(response.json())