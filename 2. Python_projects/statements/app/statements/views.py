# -*- coding: utf-8 -*-
# app/statements/views.py
from . import statements
from .forms import StatementForm, StatementTable
from .models import StatementModel
from app.extensions import ApplyStyle
from flask import render_template, request, send_file, Response, redirect, url_for
from io import BytesIO


@statements.route('/', methods=['GET', 'POST'])
def statement():
    if request.method == 'GET':
        form = StatementForm()
        return render_template('statements.html', form=form)
    elif request.method == 'POST':
        data = StatementModel.search(request.form.get('cadastral').strip())
        table = StatementTable(data)
        form = StatementForm()
        return render_template('statements.html', form=form, table=table)


@statements.route('/view/<int:id>', methods=['GET', 'POST'])
def view(id):
    files = StatementModel.get_file(id)
    if files[1]:
        return Response(files[1], mimetype='application/pdf')
    elif files[0]:
        response = Response(files[0].decode('utf-8'), mimetype='text/xml')
        response.headers['X-Content-Type-Options'] = "nosniff"
        return response
    else:
        return redirect(url_for('statements.statement'))


@statements.route('/download/<int:id>', methods=['GET', 'POST'])
def download(id):
    files = StatementModel.get_file(id)
    if files[1]:
        return send_file(BytesIO(files[1]), as_attachment=True, attachment_filename=str(id)+'.pdf', mimetype='application/pdf')
    elif files[0]:
        return send_file(BytesIO(files[0]), as_attachment=True, attachment_filename=str(id)+'.xml', mimetype='text/xml')
    else:
        return redirect(url_for('statements.statement'))
