from flask import render_template, request, flash, redirect, url_for

from countdown import app, forms

@app.route('/<uuid:id>', methods=['GET'])
def countdown(id):
    return render_template('countdown.html', id)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def countdown_admin():
    form = CountdownAdminForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('countdown_admin.html', form=form, clock=None)
