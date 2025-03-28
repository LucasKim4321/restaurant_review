from rest_framework.test import APITestCase
from django.urls import reverse
from restaurants.models import Restaurant


class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        # 테스트 코드를 작성하기 위해 필요한 것들을 미리 생성해두는 것
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

    def test_restaurant_list_view(self):
        # url = reverse를 사용하고 url name은 'restaurant-list' 사용
        # get 메서드를 사용하여 restaurant list를 가져오는 것을 테스트하기 위한 코드를 작성
        url = reverse('restaurant-list')
        Restaurant.objects.create(**self.restaurant_info)  # 생성

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data.get('results')), 1)
        self.assertEqual(response.data.get('results')[0].get('name'), self.restaurant_info['name'])
        self.assertEqual(response.data.get('results')[0].get('description'), self.restaurant_info['description'])
        self.assertEqual(response.data.get('results')[0].get('address'), self.restaurant_info['address'])
        self.assertEqual(response.data.get('results')[0].get('contact'), self.restaurant_info['contact'])
        self.assertEqual(response.data.get('results')[0].get('open_time'), self.restaurant_info['open_time'])
        self.assertEqual(response.data.get('results')[0].get('close_time'), self.restaurant_info['close_time'])
        self.assertEqual(response.data.get('results')[0].get('last_order'), self.restaurant_info['last_order'])
        self.assertEqual(response.data.get('results')[0].get('regular_holiday'), self.restaurant_info['regular_holiday'])

    def test_restaurant_post_view(self):
        # url = reverse를 사용하고 url name은 'restaurant-list' 사용
        # post 메서드를 사용하여 모델생성을 테스트 하기위한 코드를 작성
        url = reverse('restaurant-list')
        response = self.client.post(url, self.restaurant_info, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.first().name, self.restaurant_info['name'])

    def test_restaurant_detail_view(self):
        # url = reverse를 사용하고 url name은 'restaurant-detail' 사용
        # get 메서드를 사용하여 특정 restaurant 정보를 가져오는 것을 테스트 하기위한 코드를 작성
        restaurant = Restaurant.objects.create(**self.restaurant_info)  # 생성
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name'), self.restaurant_info['name'])

    def test_restaurant_update_view(self):
        # url = reverse를 사용하고 url name은 'restaurant-detail' 사용
        # post 메서드를 사용하여 restaurant 정보를 업데이트하는 것을 테스트 하기위한 코드를 작성
        restaurant = Restaurant.objects.create(**self.restaurant_info)  # 생성
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})
        updated_restaurant_info = {
            "name": "Updated Restaurant",
            "description": "Updated Description",
            "address":  "Updated Address",
            "contact": "Updated Contact",
            "open_time": "11:00:00",
            "close_time": "23:00:00",
            "last_order": "22:00:00",
            "regular_holiday": "TUE"
        }

        response = self.client.put(url, updated_restaurant_info, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(response.data.get('name'), updated_restaurant_info['name'])
        self.assertEqual(response.data.get('description'), updated_restaurant_info['description'])
        self.assertEqual(response.data.get('address'), updated_restaurant_info['address'])
        self.assertEqual(response.data.get('contact'), updated_restaurant_info['contact'])
        self.assertEqual(response.data.get('open_time'), updated_restaurant_info['open_time'])
        self.assertEqual(response.data.get('close_time'), updated_restaurant_info['close_time'])
        self.assertEqual(response.data.get('last_order'), updated_restaurant_info['last_order'])
        self.assertEqual(response.data.get('regular_holiday'), updated_restaurant_info['regular_holiday'])

    def test_restaurant_delete_view(self):
        # url = reverse를 사용하고 url name은 'restaurant-detail' 사용
        # post 메서드를 사용하여 모델삭제를 테스트하기 위한 코드를 작성
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        url = reverse('restaurant-detail', kwargs={'pk': restaurant.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Restaurant.objects.count(), 0)