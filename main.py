from flask import Flask,request,render_template,request,redirect
from app.utils import Prediction
app = Flask(__name__)

@app.route('/index',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        data = request.form
        proj_obj = Prediction(data)
        predicted_output = proj_obj.predict_output()
        return redirect(render_template('index.html',name = predicted_output))
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)