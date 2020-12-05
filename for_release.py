from bs4 import BeautifulSoup
import requests


def parse(page, headers):
    html = requests.get(page, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup


soup1 = parse('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&rlz=1C1RNDG_enRU801RU801&oq=%D0%BA%D1%83%D1%80%D1%81+&aqs=chrome.1.69i57j35i39j69i59j0j69i61j69i60j69i61j69i65.5866j1j1&sourceid=chrome&ie=UTF-8',
              {'user-agent': 'your_user_agent', 'access': '*/*'})
soup2 = parse('https://yandex.ru/maps/covid19', {'user-agent': 'your_user_agent', 'access': '*/*'})

# доллар в рублях на сегодняшний день
convert = soup1.find('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
# кол-во заболевших
ill_today = soup2.html.body.find(text='Санкт-Петербург').parent.parent.find('span', class_='covid-table-view__item-cases-diff-text').text
# название города
name = soup2.html.body.find(text='Санкт-Петербург')


print(f'курс доллара: {convert.text} рублей')
print(f'{name}: {ill_today} заболевших сегодня')
input()
