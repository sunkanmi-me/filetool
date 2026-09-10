import os

from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    send_file,
    after_this_request
)
from converters.csv_to_json import csv_to_json


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/convert", methods=["GET", "POST"])
def convert():

    if request.method == "POST":

        file = request.files.get("file")
        output_format = request.form.get("format")

        # Make sure a file was selected
        if not file or file.filename == "":
            flash("Please input the file you want to convert.")
            return render_template("convert.html")

        # Make sure an output format was selected
        if not output_format:
            flash("Please select an output format.")
            return render_template("convert.html")

        # Save the original uploaded file
        input_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(input_path)

        # CSV → JSON
        if file.filename.lower().endswith(".csv") and output_format == "json":

            output_filename = (
                file.filename.rsplit(".", 1)[0] + ".json"
            )

            output_path = os.path.join(
                OUTPUT_FOLDER,
                output_filename
            )

            # Convert the file
            csv_to_json(input_path, output_path)

            # Show download page
            return render_template(
                "download.html",
                filename=output_filename
            )

        # Conversion does not exist yet
        flash(
            "We don't support this conversion yet "
            "or the file format is invalid."
        )

        return redirect("/convert")

    else:
        return render_template("convert.html")





@app.route("/download/<filename>")
def download(filename):

    output_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    input_filename = filename.rsplit(".", 1)[0] + ".csv"

    input_path = os.path.join(
        UPLOAD_FOLDER,
        input_filename
    )

    @after_this_request
    def cleanup(response):

        if os.path.exists(output_path):
            os.remove(output_path)

        if os.path.exists(input_path):
            os.remove(input_path)

        return response

    return send_file(
        output_path,
        as_attachment=True,
        download_name=filename
    )