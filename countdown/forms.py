from flask_wtf import FlaskForm
from wtforms import TimeField

class CountdownAdminForm(FlaskForm):
    totalTime = TimeField('Time')
