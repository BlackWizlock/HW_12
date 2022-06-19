from flask import Blueprint, render_template, request
from functions import DataBase
import logger_init

main_blueprint = Blueprint("main_blueprint",
                           __name__,
                           template_folder="templates")

DATABASE = DataBase()


@main_blueprint.route("/")
def main_page():
    """
    Вьюшка - основная. При обращении обновляем загрузку БД, т.к. могли появиться 
    новые сообщения
    """
    DATABASE.class_database_loader()
    return render_template("index.html")


@main_blueprint.route("/post_list/")
def post_list():
    """
    Вьюшка - результат поиска в БД, обработка пустого поиска
    """
    search_request = request.args.get("s")
    logger_init.logger_mine.info(f"Search request: {search_request}")
    if search_request:
        return render_template(
            "post_list.html",
            search_request=search_request,
            filtered_database=DATABASE.search_in_database(search_request),
        )
    return render_template("post_list.html")


# Обработка ошибок Блюпринта


@main_blueprint.errorhandler(404)
def page_not_found(error):
    return "<h1><center><font color='red'>Error 404</font><br>Something goes wrong!"\
            "Page not found.</center></h1><hr>"


@main_blueprint.errorhandler(400)
def database_not_found(error):
    return ("<h1><center><font color='red'>Error</font>"
            "<br>Database - not found!</center></h1><hr>")
