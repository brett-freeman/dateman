import dateman

item = {
    'item_code': '123',
    'expiry_date': '2020-12-31'
}

item = dateman.Item(item)

print(item.get_item)
