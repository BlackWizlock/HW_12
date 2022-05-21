from flask import Blueprint, render_template, request
from main.views import DATABASE

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/")
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route("/upload", methods=['POST'])
def uploaded_page():
    picture = request.files.get("picture")
    picture.save(f"../../static/{picture.filename}")
    text = request.values.get("content")
    DATABASE.json_write({"pic": "./static/"+picture.filename, "content": text})
    return render_template("post_uploaded.html", added_text=text, added_picture=picture.filename)
