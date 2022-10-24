from flask import render_template, jsonify
from app.models.area_model import AreaModel


class AreaController:
    # Instance method self
    # def all(self):
    # records = AreaModel.query.all()  # select * from
    # return render_template('areas.html', areas=records)
    def all(self):
        records = AreaModel.query.all()
        return jsonify(records), 200
