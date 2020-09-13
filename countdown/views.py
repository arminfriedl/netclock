from flask import render_template, request, flash, redirect, url_for, session

from . import app
from . import forms
from .countdown import Cache

@app.route('/', methods=['GET', 'POST'])
def create():
    session.permanent = True
    if not session.get('created_countdowns'):
        session['created_countdowns'] = []

    form = forms.CountdownAdminForm(request.form)
    if request.method == 'POST' and form.validate():
        cache = Cache.getInstance()
        total = form.seconds.data or 0
        total += (form.minutes.data or 0) * 60
        total += (form.hours.data or 0) * 60 * 60

        countdown = cache.add_countdown(total)
        session['created_countdowns'].append(str(countdown['id']))
        session.modified = True
        return redirect(url_for('countdown.created'))

    return render_template('countdown/create.html', form=form, clock=None)

@app.route('/mine', methods=['GET'])
def created():
    return render_template('countdown/created.html', countdowns=session.get('created_countdowns') or [])

@app.route('/<uuid:countdown_id>', methods=['GET'])
def view(countdown_id):
    return render_template('countdown/view.html', countdown_id=countdown_id)

