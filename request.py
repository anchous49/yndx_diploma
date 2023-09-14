import config
import data
import requests

# Создание нового заказа
def post_new_order(create_order):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                    json=create_order,
                    headers=data.headers)
response = post_new_order(data.create_order)

track_order = response.json()["track"]   # Сохранение трекера

def get_order_track(track_order):    # Получение заказа по треку
    return requests.get(config.URL_SERVICE + config.GET_TRACK_ORDER,
                        params={"t": track_order})