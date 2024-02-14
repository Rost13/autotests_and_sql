# Ростислав Пономарев 13 когорта

import configuration
import requests
import data


# Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body)


# Сохранение номера трека заказа
def get_order_track():
    track_response = post_new_order(data.order_body)
    return track_response.json()["track"]


# Выполнение запроса на получение заказа по треку
def get_order_by_track():
    track_num = get_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t": track_num})
