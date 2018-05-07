import importlib
importlib.import_module('lib/Cabler')

RADIUS = 100
cabler = Cabler(RADIUS)
# cabler.tube('tata-tgn-atlantic')
# def all():
#   cable_ids = map(lambda d: d['id'], cabler.all)
#   # cable_ids = map(lambda x: x['id'], cables)
#   print cable_ids
  # for cable_id in cable_ids:
  #   cabler.tube(cable_id)

cabler.tube_from_points([
  LatLon(40.152908, -74.062861), # wall township, NJ
  LatLon(35.32533, -81.86866)    # forest city, NC
], 'NJ_NC')

