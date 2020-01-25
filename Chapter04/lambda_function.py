import json
from urllib.request import urlopen

def get_quote(request):
    Slots = request['currentIntent']['slots']
    ticker = Slots['ticker']
    price = call_quote_api(ticker)
    message = 'The last price of ticker {} was {}'.format(ticker, price)
    return close(message)

def call_quote_api(ticker):
    response = urlopen('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=3WIN88G0AVG7RZPX'.format(ticker))
    response = json.load(response)
    ''' Sample Response: 
    {'Global Quote': {'01. symbol': 'AAPL', '02. open': '316.2700', '03. high': '318.7400', '04. low': '315.0000', '05. price': '318.7300',
    '06. volume': '33454635', '07. latest trading day': '2020-01-17', '08. previous close': '315.2400', '09. change': '3.4900', 
    '10. change percent': '1.1071%'}} '''
    return response['Global Quote']["05. price"]


def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    if intent == 'GetQuote':
        return get_quote(event)
    return "Sorry, I'm not sure what you have in mind.  Please try again."
    
def close(message):
    return {
        'sessionAttributes': {},
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': message
            }
        }
    }
