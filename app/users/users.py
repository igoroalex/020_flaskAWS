from flask import Blueprint, render_template, request

bp = Blueprint(
    import_name=__name__,
    name="Edamam",
    url_prefix="/",
    template_folder="templates",
)


@bp.route("/")
def get_html_index():
    return "<p>Hello, World 21 !</p>"
