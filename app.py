from flask import Flask,render_template, request
app=Flask(_name_)
@app.route("/")
def Home():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        msg =request.form.get("message")
        print(msg)
    else:
        return render_template("predict.html")

if _name_=="__main__":
    app.run(host="0.0.0.0",port=5050)












    