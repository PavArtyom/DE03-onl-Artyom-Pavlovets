
def make_order(product, qty):
    shop_list = {
        "macbook": 1500,
        "keyboard": 250,
        "mouse": 80,
        "monitor": 120,
        "headphones": 150,
    }
    if product in shop_list.keys():
       value =  shop_list.get(product)
       price = int(value) * qty
    else:
        print('Товар не найден!')
    with open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/orders.txt", "r+") as orders_shop:
        orders_shop.write(str(price) + ' - стоимость товара' +'\n' + str(product) + ' - название позиции'
                          +'\n' + str(qty) + ' - Количество позиций')
    return f'Общая стоимость:{price}, Наименование товара:{product}, Количество позиций: {qty}'





