from flask import Flask, render_template, request

# Correct Flask initialization
app = Flask(__name__)

# Home route
@app.route("/")
def Home():
    return render_template("index.html")

# Predict route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")  # Get the message from the form
        print(msg)  # You can add logic to process the message here
        return render_template("predict.html", msg=msg)  # Pass the message to the template if needed
    else:
        return render_template("predict.html")  # Render the predict page when the method is GET

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
