from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__) #your application
linear=pickle.load(open('fitness.pkl','rb'))


@app.route('/') # default route
def home():
    return render_template("BFP.html")


@app.route('/predict',methods=['post'])
def predict():
    sc=float(request.form['step_count'])
    mo=float(request.form['mood'])
    cb=float(request.form['calories_burned'])
    hs=float(request.form['hours_of_sleep'])
   
   
    
    
    print(sc,mo,cb,hs)
    a=np.array([[sc,mo,cb,hs]])
    
    result=linear.predict(a)
    if(result == 0):
        output="You are body is UnFit"
        print("You are body is UnFit")
    else:
        output="You are body is Fit"
        print("You are body is Fit")
    return render_template('BFP.html',prediction_text=output)
    

if __name__ == '__main__':
    app.run() # you are running your app