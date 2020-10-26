""" Timezone management

Provides:
- `search.py`: Fast prefix search for timezones
- `timezone.py`: Conversion functions
- `api.py`: A REST API for the functionality provided by this package
"""
from flask import Blueprint

app = Blueprint('timezone', __name__, template_folder='templates')
from . import api
