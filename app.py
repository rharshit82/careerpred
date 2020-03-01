import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
modelpcm = pickle.load(open('modelpcm.pkl', 'rb'))
modelart = pickle.load(open('modelart.pkl', 'rb'))
modelcommerce = pickle.load(open('modelcommerce.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('main.html')
@app.route('/arts')
def arts():
    return render_template('arts.html')
@app.route('/commerce')
def commerce():
    return render_template('commerce.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/science')
def science():
    return render_template('science.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    #output = round(prediction[0], 2)
    if prediction[0]==[0]:
        # ouroutput="Commerce"
        return render_template("commerce.html")
    elif prediction[0]==[1] :
        return render_template("science.html")
    elif prediction[0]==[2] :
        return render_template("arts.html")
@app.route('/predict_pcm',methods=['POST'])
def predict_pcm():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = modelpcm.predict(final_features)
    if prediction==['Scientist']:
        return render_template("scientist.html")
    elif prediction == ['Engineer']:
        return render_template("engineer.html")
    elif prediction==['Professor'] :
        return render_template("professor.html")
@app.route('/predict_art',methods=['POST'])
def predict_art():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = modelart.predict(final_features)
    if prediction==['lawyer']:
        return render_template("lawyer.html")
    elif prediction == ['fashion designer']:
        return render_template("fashion_designer.html")
    elif prediction==['Generalism'] :
        return render_template("journalism.html")
    elif prediction==['Management'] :
        return render_template("management.html")
@app.route('/predict_commerce',methods=['POST'])
def predict_commerce():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = modelcommerce.predict(final_features)
    if prediction==['CA']:
        return render_template("ca.html")
    elif prediction == ['Economist']:
        return render_template("economist.html")
    elif prediction==['Businessman'] :
        return render_template("businessman.html")



@app.route('/logical', methods=['post', 'get'])
def logical():
    message = ''
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        count = 0
        if(int_features[0]==2):
            count+=1
        if(int_features[1]==3):
            count+=1
        if int_features[2]==0:
            count+=2
        if int_features[3]==1:
            count+=2
        if int_features[4]==2:
            count+=2
        if int_features[5]==1:
            count+=2
        message = 'Your Logical Reasoning Score is ' + str(count)
    return render_template('logical_skills.html', message=message)
@app.route('/technological', methods=['post', 'get'])
def technological():
    message = ''
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        count = 0
        if(int_features[0]==2):
            count+=1
        if(int_features[1]==0):
            count+=1
        if int_features[2]==1:
            count+=2
        if int_features[3]==0:
            count+=2
        if int_features[4]==2:
            count+=2
        if int_features[5]==1:
            count+=2
        message = 'Your Technological Skills Score is ' + str(count)
    return render_template('technological_skills.html', message=message)

@app.route('/engineer')
def engineer():
    return render_template('engineer.html')
@app.route('/professor')
def professor():
    return render_template('professor.html')
@app.route('/scientist')
def scientist():
    return render_template('scientist.html')
@app.route('/pred_pcm')
def pcm():
    return render_template('pcm.html')
@app.route('/pred_art')
def pred_art():
    return render_template('artpred.html')
@app.route('/pred_commerce')
def pred_commerce():
    return render_template('commercepred.html')
@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/businessman')
def businessman():
    return render_template('businessman.html')
@app.route('/ca')
def ca():
    return render_template('ca.html')
@app.route('/economist')
def eco():
    return render_template('economist.html')
@app.route('/lawyer')
def lawyer():
    return render_template('lawyer.html')
@app.route('/fashion_designer')
def fashion():
    return render_template('fashion_designer.html')
@app.route('/journalism')
def journalism():
    return render_template('journalism.html')
@app.route('/management')
def management():
    return render_template('management.html')





if __name__ == "__main__":
    app.run(debug=True)