from flask import Blueprint, render_template, request

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/")
def loader_page():
    return render_template("post_form.html")


@loader_blueprint.route("/uploads/", methods=['GET', 'POST'])
def uploaded_page():
    if request.method == 'POST':
        picture = request.files.get("picture")
        picture.save(f"./uploads/{picture.filename}")
        text = request.form.get("content")
        return render_template("post_uploaded.html", added_text=text)
    return render_template("post_uploaded.html")
