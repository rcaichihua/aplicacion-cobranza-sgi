from app import app
from app.controller.area_controller import AreaController


@app.route('/areas', methods=['GET'])
def areas_get_all():
    controller = AreaController()
    return controller.all()
