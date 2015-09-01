import pprint

import oandapy
from settings.local import ACCESS_TOKEN, ACCOUNT_ID

oanda = oandapy.API(
    environment = "practice",
    access_token = ACCESS_TOKEN
)

def get_forex_names():
    forex_list = []
    instruments = oanda.get_instruments(ACCOUNT_ID)

    for instrument in instruments['instruments']:
        temp_pair = instrument['instrument'].split('_')
        bad_pairs = "ZAR DKK CZK PLN TRY THB SEK PLN NOK MXN HKD SGD CNH HUF SAR"
        if temp_pair[0] not in bad_pairs and temp_pair[1] not in bad_pairs:
            forex_list.append(instrument['instrument'])

    return forex_list

def get_minute_data(pair):
    response = oanda.get_history(instrument=pair, start='2005-01-01T00', granularity='M1')
    return response

pair_list = get_forex_names()


for pair in pair_list:
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(get_minute_data(pair))

def get_financial_calendar():
    pp = pprint.PrettyPrinter(indent=4)
    response = oanda.get_eco_calendar(instrument="EUR_USD", period=31536000)
    pp.pprint(response)

get_financial_calendar()