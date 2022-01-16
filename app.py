from distutils.log import debug
import pickle
from flask import Flask,render_template, request

tikolo = Flask(__name__)
md = pickle.load(open('model.pkl','rb'))
@tikolo.route('/')
def index():
    return render_template('index.html')
@tikolo.route('/predict', methods=['GET','POST'])
def predict():
    input_received = request.form.get('temperature')
    try:
        input_received = float(input_received)
        if input_received >= -10000 and input_received <= 10000:
            tt = md.predict([[input_received]]) 
            res = round(tt[0], 2)
            print(res)
            return render_template('index.html',prediction_text_area=f"Total revenue is Rs. {res}/-")
        else:
            return render_template('index.html',prediction_text_area="Range not valid!")
    except:
        # avxhghsg
        return render_template('index.html',prediction_text_area="Enter float values.")


 
    # print(res)
    # return render_template('index.html',prediction_text_area="Total revenue is Rs. "+str(res) + "/-")
    # return render_template('index.html',prediction_text_area=f"Total revenue is Rs. {res}/-")



if __name__=="_main_":
    tikolo.run(debug = True)
