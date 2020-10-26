from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import Optional


class CountdownAdminForm(FlaskForm):
    hours = fields.IntegerField("Hours", [Optional()],
                                render_kw={"min": 0, "max": 999, "placeholder": "00", "autocomplete": "off"})
    minutes = fields.IntegerField("Minutes", [Optional()],
                                  render_kw={"min": 0, "max": 59, "placeholder": "00", "autocomplete": "off"})
    seconds = fields.IntegerField("Seconds", [Optional()],
                                  render_kw={"min": 0, "max": 59, "placeholder": "00", "autocomplete": "off"})
