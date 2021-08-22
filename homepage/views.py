from django.shortcuts import render
from django.views import View
import datetime as dt


class HomepageView(View):
    country_codes_db = {
            'CZ': '',
            'SK': '',
            'UK': ''
        }

    def get(self, request):
        dates_db = {}
        country_codes = ''
        dates = ''

        today = dt.datetime.now().date()
        for i in range(0, 16, 1):
            dates_db[f'{today + dt.timedelta(days=i)}'] = today + dt.timedelta(days=i)

        for country_code in self.country_codes_db:
            country_codes += (
                f'<input type="radio" name="country_code"'
                f' required value="{country_code}">{country_code}<br>')

        for date in dates_db:
            dates += (
                f'<input type="radio" name="date"'
                f' required value="{date}">{date}<br>')

        context = {
            'dates': dates,
            'country_codes': country_codes,
        }

        return render(request, 'homepage/index.html', context)
