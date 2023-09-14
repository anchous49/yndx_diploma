import request
# Касперская Анна, 8-ая когорта, финальный проект. Инженер по тестированию+

# Функция для позитивной проверки
def positive_assert(track_order):
    order_response = request.get_order_track(track_order)
    assert order_response.status_code == 200


# Тест 1
def test_get_order_track_success_response():
    positive_assert(request.track_order)