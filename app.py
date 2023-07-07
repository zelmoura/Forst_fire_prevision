from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder= "./")

model=pickle.load(open('./model.pkl','rb'))




@app.route('/')
def hello_world():
    return render_template('forest_fire.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
