from flask import Blueprint

app = Blueprint('worldclock', __name__, template_folder='templates')
from . import views
from . import api
