from flask import Blueprint, render_template, request
from functions import DataBase
from pprint import pprint as pp

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

DATABASE = DataBase()



@main_blueprint.route("/")
def main_page():
    DATABASE.class_database_loader()
    return render_template("index.html")


@main_blueprint.route("/post_list/")
def post_list():
    search_request = request.args.get("s")
    if search_request:
        return render_template("post_list.html",
                               search_request=search_request,
                               filtered_database=DATABASE.search_in_database(search_request))
    return render_template("post_list.html")
