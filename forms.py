from flask_wtf import FlaskForm, TimeField

class CountdownAdminForm(FlaskForm):
    totalTime = TimeField('Time')
