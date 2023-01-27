from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def menu_test(self):
        item = Menu.objects.create(
            title='Chef Salad', price=5.50, inventory=100)
        self.assertEqual(item, 'Chef Salad : 5.50')
