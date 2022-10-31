# -*- coding: utf-8 -*-
# app/statements/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_table import Table, Col, LinkCol
import babel
babel.default_locale('LC_TIME')
babel.dates.format_datetime


class StatementForm(FlaskForm):
    classes = ['StatementForm']
    cadastral = StringField(render_kw={"placeholder": "Кадастровый номер"})
    submit = SubmitField(render_kw={"value": "Найти"})


class StatementTable(Table):
    classes = ['StatementTable']
    id = Col('id', show=False)
    cadastral = Col('Кадастровый')
    statement = Col('Выписка')
    date_requery = Col('Дата')
    view = LinkCol('Просмотр', 'statements.view', url_kwargs=dict(id='id'), anchor_attrs={'target': '_blank'})
    download = LinkCol('Загрузка', 'statements.download', url_kwargs=dict(id='id'))
