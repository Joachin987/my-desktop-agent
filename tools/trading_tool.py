import alpaca_trade_api as tradeapi

class TradingTool:
    def __init__(self, api_key: str, api_secret: str, base_url: str):
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

    def get_account_info(self):
        """Retrieve account information."""
        return self.api.get_account()

    def get_positions(self):
        """Retrieve current positions."""
        return self.api.list_positions()

    def place_order(self, symbol: str, qty: int, side: str, order_type: str, time_in_force: str):
        """Place a market order."""
        return self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=order_type,
            time_in_force=time_in_force
        )
