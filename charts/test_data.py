import oandapy
import pprint

oanda = oandapy.API(environment="practice", access_token='d6cd7f45a3a9f38c177fbc2753423cd0-1ea5da4d5076e7cd3fab66e6c3b2fa5c')

response = oanda.get_history(instrument="EUR_USD", start='2005-01-01T00', granularity='M1')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response)`