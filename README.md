# Filetool

Filetool is a simple web-based file conversion tool built with Python and Flask. It allows users to upload a file, select a supported output format, convert the file, and download the converted result.

## Features

* Upload files through a web interface
* Drag-and-drop file uploading
* CSV to JSON conversion
* Download converted files
* Flash messages for errors and validation
* Responsive interface
* Temporary file cleanup after downloading

## Technologies

* Python
* Flask
* HTML
* CSS
* JavaScript
* Jinja
* CSV and JSON libraries

## Project Structure

```text
file_converter/
├── app.py
├── converters/
│   ├── __init__.py
│   └── csv_to_json.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── convert.html
│   └── download.html
├── uploads/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore
```

## How It Works

The user first uploads a file and selects the desired output format. Flask receives the uploaded file and saves it temporarily. The application then selects the appropriate converter based on the input and output formats.

Currently, Filetool supports:

```text
CSV → JSON
```

The conversion logic is separated into the `converters` directory so that additional conversion formats can be added without putting all of the conversion logic inside `app.py`.

After conversion, the user is taken to a download page where they can manually download the converted file.

## Running Locally

Clone the repository and enter the project directory:

```bash
git clone https://github.com/sunkanmi-me/filetool.git
cd filetool
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add a Flask secret key:

```text
SECRET_KEY=your-secret-key
```

Run the application:

```bash
python3 -m flask --app app run
```

Then open the local address provided by Flask in your browser.

## Future Improvements

Planned improvements include:

* Support for more file formats
* More conversion combinations
* Improved file validation
* Better temporary-file management
* Improved security for uploaded filenames
* Additional frontend improvements
* Deployment for public use

## Author

**Sunkanmi**

GitHub: https://github.com/sunkanmi-me
