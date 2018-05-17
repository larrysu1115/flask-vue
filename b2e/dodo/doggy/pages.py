from flask import Blueprint, render_template

blueprint_pages = Blueprint('doggy_pages', __name__, template_folder='templates')

@blueprint_pages.route('/<page_name>')
def show(page_name):
    return render_template('show.html', page_name=page_name)
