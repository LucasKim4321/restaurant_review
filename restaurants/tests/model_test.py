from django.test import TestCase
from restaurants.models import Restaurant


class RestaurantModelTest(TestCase):

    # 기본 셋팅
    def setUp(self):
        # Restaurant 모델 테스트 시 필요한 세팅 기재
        self.restaurant_info = {
            "name": "Test Restaurant",
            "description": "Test Description",
            "address":  "Test Address",
            "contact": "Test Contact",
            "open_time": "10:00:00",
            "close_time": "22:00:00",
            "last_order": "21:00:00",
            "regular_holiday": "MON"
        }

    def test_create_restaurant(self):
        # objects의 create 메서드를 테스트하기 위한 코드 기재
        restaurant = Restaurant.objects.create(**self.restaurant_info)

        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(restaurant.name, self.restaurant_info['name'])
        self.assertEqual(restaurant.description, self.restaurant_info['description'])
        self.assertEqual(restaurant.address, self.restaurant_info['address'])
        self.assertEqual(restaurant.contact, self.restaurant_info['contact'])
        self.assertEqual(restaurant.open_time, self.restaurant_info['open_time'])
        self.assertEqual(restaurant.close_time, self.restaurant_info['close_time'])
        self.assertEqual(restaurant.last_order, self.restaurant_info['last_order'])
        self.assertEqual(restaurant.regular_holiday, self.restaurant_info['regular_holiday'])
        self.assertEqual(restaurant.__str__(), self.restaurant_info['name'])


# restaurant/test.py
