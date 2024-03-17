"""
This app checks the price of bitcoin using:  https://api.coindesk.com/v1/bpi/currentprice.json
"""
import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    number_of_bitcoin = get_bitcoins()

    response, error = make_api_request(url)

    if error:
        print('Error while trying to fetch data, try checking your internet connection!')
        return

    if not response:
        print("Unable to get response!")
        return

    rate = get_rate_from_response(response)

    if not rate:
        print('Unable to parse rate.')
        return

    print_current_rate(rate)
    total = calculate_bitcoin_total(rate, number_of_bitcoin)
    print_total(total)


def get_bitcoins(input_bitcoin = '', number_of_bitcoin = None):
    '''
    Gets amount of bitcoin a user has.
    Returns amount of bitcoin as a float.
    '''

    # Constantly loops till we get the user's input of bitcoin as a float.
    while not number_of_bitcoin or len(input_bitcoin) == 0 or not isinstance(number_of_bitcoin, float):
        input_bitcoin = input('How much bitcoin do you have: ')
        try:
            number_of_bitcoin = float(input_bitcoin)
        except Exception as e:
            print(e)

    return float(number_of_bitcoin)


def print_current_rate(rate):
    '''
    Simple method to print the current rate of bitcoin.
    '''
    print(f'The rate of the USD is ${rate}.')


def calculate_bitcoin_total(rate, bitcoin_amount):
    '''
    Gets user's USD worth of bitcoin by multiplying rate and amount of bitcoin
    '''
    return rate * bitcoin_amount


def print_total(total):
    '''
    Prints the USD worth of a user's bitcoin.
    '''
    print(f'The total amount of USD you have in bitcoin is ${total}.')


def make_api_request(url):
    '''
    Tries to get API request.
    If successful, it'll return a tuple of response in json and None.
    If failed, it will return tuple of None and Exception.
    '''
    try:
        response = requests.get(url).json()
        return response, None
    except Exception as e:
        return None, e


def get_rate_from_response(response):
    '''
    Goes through API response and makes sure it contains the proper bitcoin conversion data.
    Returns rate (float) if found or None if not found.
    '''
    if not response or not response['bpi'] or not response['bpi']['USD'] or not response['bpi']['USD']['rate_float']:
        return None

    rate = response['bpi']['USD']['rate_float']

    try:
        rate = float(rate)
    except Exception as e:
        print(e)

    return rate


if __name__ == '__main__':
    main()

