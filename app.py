from flask import Flask, render_template, request
from review import review_code
import os

app = Flask(__name__)

# ==============================
# Upload Folder Configuration
# ==============================

UPLOAD_FOLDER = "user_uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==============================
# Detect Programming Language
# ==============================

def detect_language(filename):

    extension = filename.split(".")[-1].lower()

    languages = {

        "py": "Python",
        "c": "C",
        "cpp": "C++",
        "java": "Java",
        "js": "JavaScript",
        "html": "HTML",
        "css": "CSS"

    }

    return languages.get(extension, "Unknown")


# ==============================
# Home Page
# ==============================

@app.route("/")
def home():

    return render_template("index.html")


# ==============================
# Upload & Review
# ==============================

@app.route("/upload", methods=["POST"])
def upload():

    if "code_file" not in request.files:

        return "No file uploaded."

    file = request.files["code_file"]

    if file.filename == "":

        return "Please select a file."

    try:

        # Read uploaded file

        code = file.read().decode("utf-8")

        # AI Review

        review = review_code(code)

        # Detect Language

        language = detect_language(file.filename)

        return render_template(

            "result.html",

            filename=file.filename,

            language=language,

            review=review

        )

    except Exception as e:

        return f"<h2>Error</h2><pre>{e}</pre>"


# ==============================
# History Page
# ==============================

@app.route("/history")
def history():

    return render_template("history.html")


# ==============================
# About Page
# ==============================

@app.route("/about")
def about():

    return render_template("about.html")


# ==============================
# Run Flask
# ==============================

if __name__ == "__main__":

    app.run(debug=True)