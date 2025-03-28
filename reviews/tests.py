from django.test import TestCase
from restaurants.models import Restaurant
from reviews.models import Review
from django.contrib.auth import get_user_model

User = get_user_model()

class ReviewModelTest(TestCase):
    def setUp(self):
        # Review 모델 테스트 시 필요한 세팅 기재
        self.test_user = {
            'email': 'test@example.com',
            'nickname': 'testuser',
            'password': 'password1234',
        }
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
        self.test_review = {
            "title":  "Test Title",
            "comment": "Test Comment"
        }

    def test_create_review(self):
        # objects의 create 메서드를 테스트하기 위한 코드 기재
        user = User.objects.create_user(**self.test_user)
        restaurant = Restaurant.objects.create(**self.restaurant_info)
        review = Review.objects.create(user=user, restaurant=restaurant, **self.test_review)

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.user, user)
        self.assertEqual(review.restaurant, restaurant)
        self.assertEqual(review.title, self.test_review['title'])
        self.assertEqual(review.comment, self.test_review['comment'])
        self.assertEqual(str(review), f"{restaurant.name} 리뷰")