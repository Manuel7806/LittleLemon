from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse


class MenuViewTest(TestCase):
    def create_item(self, title='burger', price=6.50, inventory=100) -> Menu:
        return Menu.objects.create(title=title, price=price, inventory=inventory)

    def test_getall(self):
        item = self.create_item()
        url = reverse('menu')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(item.title, resp.content)

    def test_url_exist_at_location(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
