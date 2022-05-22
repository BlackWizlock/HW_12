from flask import Blueprint, render_template, request, send_from_directory
from main.views import DATABASE

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/")
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route("/uploads/<path:path>")
@loader_blueprint.route("/uploads", methods=['POST'])
def uploaded_page(path=None):
    if request.method == "POST":
        picture = request.files.get("picture")
        picture.save(f"./uploads/{picture.filename}")
        text = request.values.get("content")
        DATABASE.json_write({"pic": "../../uploads/" + picture.filename, "content": text})
        return render_template("post_uploaded.html", added_text=text, added_picture=picture.filename)
    else:
        return send_from_directory("uploads", path)
