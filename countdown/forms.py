from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.fields import html5
from wtforms.validators import Optional

class CountdownAdminForm(FlaskForm):
    hours = html5.IntegerField("Hours", [Optional()],
                               render_kw = {"min":0, "max":999, "placeholder": "00"})
    minutes = html5.IntegerField("Minutes", [Optional()],
                                 render_kw = {"min":0, "max":59, "placeholder": "00"})
    seconds = html5.IntegerField("Seconds", [Optional()],
                                 render_kw = {"min":0, "max":59, "placeholder": "00"})
