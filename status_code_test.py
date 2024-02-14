# Ростислав Пономарев, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_get_order():
    track_number = sender_stand_request.get_order_by_track()
    assert track_number.status_code == 200
