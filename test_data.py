import pprint

import oandapy
from settings.local import ACCESS_TOKEN, ACCOUNT_ID

oanda = oandapy.API(
    environment = "practice",
    access_token = ACCESS_TOKEN
)

instruments = oanda.get_instruments(ACCOUNT_ID)
response = oanda.get_history(instrument="EUR_USD", start='2005-01-01T00', granularity='M1')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(instruments)
