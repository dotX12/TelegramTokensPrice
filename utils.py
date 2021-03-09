import json

from API import CoinGeckoAPI

cg = CoinGeckoAPI()


class Math:

    @staticmethod
    def format_decimal(x):
        if x < 0.001:
            return format(x, '.7f')
        return '{0:,}'.format(x)

    @staticmethod
    def rounding(integer):
        if integer:
            return "%.3f" % integer
        else:
            return 'There is no data'


class WrapperJson(Math):

    async def price_token(self, coin_id, currency='usd') -> dict:
        data = await cg.get_coins_markets(vs_currency=currency, ids=coin_id, order='market_cap_desc',
                                          sparkline=False, price_change_percentage='1h,24h,7d,30d')
        return {
            'name': data[0]['name'],
            'symbol': data[0]['symbol'],
            'current_price': self.format_decimal(data[0]['current_price']),
            'low_24h': self.format_decimal(data[0]['low_24h']),
            'high_24h': self.format_decimal(data[0]['high_24h']),
            'price_change_24h': data[0]['price_change_24h'],
            'price_change_percentage_24h': data[0]['price_change_percentage_24h'],
            'price_change_percentage_1h_in_currency': data[0]['price_change_percentage_1h_in_currency'],
            'price_change_percentage_24h_in_currency': data[0]['price_change_percentage_24h_in_currency'],
            'price_change_percentage_7d_in_currency': data[0]['price_change_percentage_7d_in_currency'],
            'price_change_percentage_30d_in_currency': data[0]['price_change_percentage_30d_in_currency'],
        }

    def get_formatted_text(self, data_token, currency='USD'):
        return (f'Token: **{data_token["name"]} ({(data_token["symbol"]).upper()})**\n'
                f'Price: **{data_token["current_price"]} {currency} 💵**\n'
                f'1h: **{self.rounding(data_token["price_change_percentage_1h_in_currency"])} % ** | '
                f'24h: **{self.rounding(data_token["price_change_percentage_24h_in_currency"])} % **\n'
                f'7d: **{self.rounding(data_token["price_change_percentage_7d_in_currency"])} % ** | '
                f'30d: **{self.rounding(data_token["price_change_percentage_30d_in_currency"])} %**\n\n'
                f'24h LOW | 24h HIGH :\n'
                f'**{data_token["low_24h"]} | {data_token["high_24h"]}**\n')

    @staticmethod
    def get_id_from_symbol(symbol):
        with open('tokens.json', 'r') as file:
            json_data = json.load(file)
            for token in json_data:
                if token['symbol'] == symbol or token['id'] == symbol:
                    return token['id']
