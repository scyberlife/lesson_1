import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt


URL = 'https://www.mashina.kg'

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                  " AppleWebKit/605.1.15 (KHTML, like Gecko)"
                  " Version/16.4 Safari/605.1.15",
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = bs(html, "html.parser")
    items = soup.find_all('div', class_='list-item list-label')
    car_lists = []

    for item in items:
        car_lists.append(
            {
                'title_name': item.find('span', class_='white font-big').get_text(),
                'title_url': URL + item.find('a').get('href'),
                'image': URL + item.find('div', class_='image-wrap').find('img').get('src'),
            }
        )
    return car_lists


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code ==200:
        car_list2 = []
        for page in range(0, 1):
            html = get_html(f'https://www.mashina.kg/new/search?'.strip(), params=page)
            car_list2.extend(get_data(html.text))
        return car_list2
    else:
        raise Exception('Error in parser')