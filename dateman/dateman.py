"""
    __init__
        item is a dictionary
"""


class Item:
    def __init__(self, item):
        self._item_code = item['item_code']
        self._expiry_date = item['expiry_date']

    @property
    def get_item(self):
        return self._item_code + ' ' + self._expiry_date
