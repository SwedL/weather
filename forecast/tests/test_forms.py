from django.test import TestCase

from forecast.forms import CityNameForm


class CityNameFormTest(TestCase):
    """ Тест формы авторизации пользователя """

    def setUp(self):
        self.form = CityNameForm()

    def test_form_field_label(self):
        # Проверка наименования полей формы
        self.assertTrue(
            self.form.fields['city'].label is None or self.form.fields['city'].label == 'city')
