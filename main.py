from flask import Flask,request,render_template,request,redirect
from app.utils import Prediction
import app.CONFIG as path
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index',methods=['POST','GET'])
def index():    
    data = request.form
    proj_obj = Prediction(data)
    predicted_output = proj_obj.predict_output()
    return render_template('index.html',iris_type = predicted_output)

if __name__ == "__main__":
    app.run(host=path.HOST_NAME,port=path.PORT_NUMBER)