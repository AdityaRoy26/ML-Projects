from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

#loading model
pipe=pickle.load(open("Ridge.pkl","rb"))

#loading the dataset
data=pd.read_csv("Cleaned_data.csv")

locations=sorted(data["location"].unique())

@app.route("/")
def home():
    return render_template("index.html",locations=locations)
@app.route("/predict",methods=["POST"])
def predict():

    location=request.form.get("location")
    total_sqft = float(request.form.get('total_sqft'))
    bath=int(request.form.get("bath"))
    bhk=int(request.form.get("bhk"))

    input_df=pd.DataFrame([[location,total_sqft,bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction=pipe.predict(input_df)[0]

    return render_template(
        "index.html",
        locations=locations,
        prediction=round(prediction,2)
    )

if __name__=="__main__":
    app.run(debug=True)
