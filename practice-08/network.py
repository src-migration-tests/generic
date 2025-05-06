import requests
import bs4


def find_mass(planet: str):
    response = requests.get(
        url=f'https://ru.wikipedia.org/wiki/{planet}',
        headers={
            'Accept': 'text/html'
        }
    )

    bs = bs4.BeautifulSoup(response.content)
    for row in bs.select('table.infobox tr'):
        header = row.select_one('th')
        if header is not None and 'Объём' in header.text:
            print(f'Объем планеты {planet}: {row.select_one('td').text}')
            return
        

for planet in ['Земля', 'Марс', 'Венера', 'Сатурн', 'Нептун']:
    try:
        find_mass(planet)
    except Exception as e:
        print(f'Для планеты {planet} ошибка: {e}')