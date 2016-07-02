from django.test import TestCase
from crud_app.models import User
from django.utils import timezone


# Create your tests here.
class UserTest(TestCase):

    def create_user(self, email="shahjalal.tipu@gmail.com", first_name="Shahjalal", last_name="Hossain", street="Kamal Road", house_no="112", postal_code="1215", town="Dhaka", country="Bangladesh", newsletter="yes"):
        return User.objects.create(email=email, first_name=first_name, last_name=last_name, street=street, house_no=house_no, postal_code=postal_code, town=town, country=country, newsletter=newsletter, created_date=timezone.now(), modified_date=timezone.now())

    def test_whatever_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.email, "shahjalal.tipu@gmail.com")
        self.assertEqual(u.first_name, "Shahjalal")
        self.assertEqual(u.last_name, "Hossain")
