BTC_PRICE = 338.0
"""float: Price of BTC in USD"""

class Abitca(object):
    """A Specie factory (like a bank)"""
    pass

class Specie(object):
    """Unit and object representation of currency for Abitcus

    Attributes:
        value (float): Accessible value of Specie, in represented in either BTC or USD
        _value (float): Private value of Specie, in represented in USD. Used to calculate `value`
        fee (float): Cost of fee for any transaction
    """
    def __init__(self, *args, **kwargs):
        self._value = kwargs.get('value', 0.0)

    def to_btc(self):
        self.value = round(self._value, 2)
        return self.value

    def to_usd(self):
        self.value = round(self.value*BTC_PRICE, 8)
        return self.value

    @property
    def fee(self):
        if self._value < 15:
            self._fee = 0.15
        self._fee = 0.01*self._value
        return self._fee

def calculate_buy_rate(price, sell_rate):
    pass