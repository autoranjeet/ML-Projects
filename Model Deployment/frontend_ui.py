from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('rf1.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods = ['Get'])
def predict_response():

    """Lets predict response
    This is using dockstrings specifications.
    ---

    parameters:
      - name: salary
        in: query
        type: number
        required: true
      - name: balance
        in: query
        type: number
        required: true
      - name: previous
        in: query
        type: number
        required: true
      - name: duration
        in: query
        type: number
        required: true
      - name: campaign
        in: query
        type: number
        required: true
      - name: blue_collor
        in: query
        type: number
        required: true
      - name: entreprenuer
        in: query
        type: number
        required: true
      - name: housemaid
        in: query
        type: number
        required: true
      - name: management
        in: query
        type: number
        required: true
      - name: retired
        in: query
        type: number
        required: true
      - name: self-employed
        in: query
        type: number
        required: true
      - name: services
        in: query
        type: number
        required: true
      - name: student
        in: query
        type: number
        required: true
      - name: technician
        in: query
        type: number
        required: true
      - name: unemployed
        in: query
        type: number
        required: true
      - name: unknown
        in: query
        type: number
        required: true
      - name: married
        in: query
        type: number
        required: true
      - name: single
        in: query
        type: number
        required: true
      - name: secondary
        in: query
        type: number
        required: true
      - name: tertiary
        in: query
        type: number
        required: true
      - name: unknown
        in: query
        type: number
        required: true
      - name: d_yes
        in: query
        type: number
        required: true
      - name: h_yes
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
  
    salary = request.args.get('salary')
    age = request.args.get('age')
    balance = request.args.get('balance')
    previous = request.args.get('previous')
    duration = request.args.get('duration')
    campaign = request.args.get('campaign')
    blue_collor = request.args.get('blue-collar')
    entreprenuer = request.args.get('entrepreneur')
    housemaid = request.args.get('housemaid')
    management = request.args.get('management')
    retired = request.args.get('retired')
    self_employed = request.args.get('self-employed')
    services = request.args.get('services')
    student = request.args.get('student')
    technician = request.args.get('technician')
    unemployed = request.args.get('unemployed')
    job_unknown = request.args.get('unknown')
    married = request.args.get('married')
    single = request.args.get('single')
    secondary = request.args.get('secondary')
    tertiary = request.args.get('tertiary')
    edu_unknown = request.args.get('unknown')
    default_yes = request.args.get('d_yes')
    housing_yes = request.args.get('h_yes')
    prediction = classifier.predict([[salary,age,balance,previous,duration,campaign,blue_collor,entreprenuer,housemaid,management,retired,self_employed,services,
    student,technician,unemployed,job_unknown,married,single,secondary,tertiary,edu_unknown,default_yes,housing_yes]])
    print(prediction)

    return "The Client will respond as "+ str(prediction)



@app.route('/predict_file', methods = ['POST'])
def predict_response_file():
    """Let's predict the response of customers
    This is using dockstrings specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    
    responses:
        200:
            description: The output values
    """

    df_test = pd.read_csv(request.files.get('file'))
    predicted = classifier.predict(df_test)
    return "The Client will respond as "+ str(list(predicted))


if __name__=='__main__':
    app.run()