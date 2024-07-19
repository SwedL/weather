from django import forms


class CityNameForm(forms.Form):
    """ Форма ввода названия города по которому необходимо получить прогноз погоды """

    city = forms.CharField(
        max_length=150, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'введите название города'}),
        label='city',
    )
