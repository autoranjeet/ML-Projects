from flask import Flask,request
import pandas as pd
import pickle

app = Flask(__name__)
pickle_in = open('rf1.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
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
    
    if prediction[0] == 1:
        client_response = 'Yes'
    else:
        client_response = 'No'

    return "The Client will respond as "+ str(client_response)


@app.route('/predict_file', methods = ['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get('file'))
    predicted = classifier.predict(df_test)

    return "The Client will respond as "+ str(list(predicted))



if __name__=='__main__':
    app.run()