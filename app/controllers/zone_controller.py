from flask import request
from typing import Collection
from app.controllers.global_controller import GlobalController
from app.models.zone import Zone
from app.constants.status_code import HTTP_BAD_REQUEST_CODE, HTTP_CREATED_CODE
from app.constants.response_messages import ERROR_MESSAGE, SUCCESS_MESSAGE
from app.constants.required_params import required_params
from app import database

zones: Collection = database.zones

class ZoneController:
  def create():
    body = request.get_json()
    params = required_params['zone']['create']
    includes_params = GlobalController.includes_all_required_params(params, body)

    try:
      if includes_params:
        zone = Zone(**body)
        zone_data = zone.dict(exclude_none=True)

        zones.insert_one(zone_data)

        return GlobalController.generate_response(HTTP_CREATED_CODE, SUCCESS_MESSAGE, zone_data)

      raise Exception()

    except:
      return GlobalController.generate_response(HTTP_BAD_REQUEST_CODE, ERROR_MESSAGE)