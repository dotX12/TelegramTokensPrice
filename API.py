from urls import MARKET_URL
from client import HTTPClient


class CoinGeckoAPI(HTTPClient):

    async def get_coins_markets(self, vs_currency, ids, order, sparkline, price_change_percentage):
        return await self.request('GET', MARKET_URL.format(vs_currency, ids, order, sparkline, price_change_percentage))

