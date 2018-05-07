import importlib
importlib.import_module('lib/Cabler')

RADIUS = 100
cabler = Cabler(RADIUS)

# create cables for the TATA-TGN Atlantic network
cabler.tube('tata-tgn-atlantic')

# a function to populate a globe with all cables
def all_cables():
  cable_ids = map(lambda d: d['id'], cabler.all)
  for cable_id in cable_ids:
    cabler.tube(cable_id)

# create a custom cable using lat/lon coords
cabler.tube_from_points([
  LatLon(40.152908, -74.062861), # wall township, NJ
  LatLon(35.32533, -81.86866)    # forest city, NC
], 'NJ_NC')

