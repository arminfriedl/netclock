from flask import render_template, request, flash, redirect, url_for

from . import app
from . import forms

@app.route('/<uuid:countdown_id>', methods=['GET'])
def countdown(countdown_id):
    return render_template('countdown/countdown.html', countdown_id=countdown_id)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def countdown_admin():
    form = forms.CountdownAdminForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('countdown/countdown_admin.html', form=form, clock=None)
