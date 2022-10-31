# -*- coding: utf-8 -*-
# app/statements/models.py

from app.extensions import db


class StatementModel(db.Model):
    __tablename__ = 'statements'
    id = db.Column(db.Integer, primary_key=True)
    cadastral = db.Column(db.String)
    statement = db.Column(db.String)
    date_requery = db.Column(db.String)
    path_name = db.Column(db.String)
    xml = db.Column(db.Binary)
    pdf = db.Column(db.Binary)

    def __repr__(self):
        return self.id, self.cadastral, self.statement, self.date_requery

    @staticmethod
    def search(cadastral):
        result = db.session.query(  StatementModel.id,
                                    StatementModel.cadastral,
                                    StatementModel.statement,
                                    StatementModel.date_requery).filter(StatementModel.cadastral == cadastral).order_by(db.desc(StatementModel.date_requery)).all()
        #[print(i) for i in result]
        return result

    @staticmethod
    def get_file(id):
        result = db.session.query(StatementModel.xml,
                                  StatementModel.pdf).filter(StatementModel.id == id).one()
        if result:
            return result
        else:
            return None
