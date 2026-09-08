from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/convert", methods=["GET", "POST"])
def convert():
    return render_template("convert.html")
    # if request.method == "POST":
    #     return render_template("convert.html")
    
    # else:
    #     return render_template("convert.html")