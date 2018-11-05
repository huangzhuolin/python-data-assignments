import requests
from bs4 import BeautifulSoup

PROXY_DICT = {
    'http': 'http://127.0.0.1:1087',
    'https': 'https://127.0.0.1:1087',
}

MOVIES_URL = 'https://www.hbo.com/movies/catalog'

classes = {
    'movie_card': 'modules/cards/CatalogCard--container modules/cards/MovieCatalogCard--container ' +
                  'modules/cards/CatalogCard--notIE modules/cards/CatalogCard--desktop',
    'movie_title': 'modules/cards/CatalogCard--title',
    'movie_detail': 'modules/cards/CatalogCard--details',
}


def parse_movie_item(movie_html):
    title = movie_html.find('p', attrs={'class': classes['movie_title']}).text
    detail = movie_html.find('p', attrs={'class': classes['movie_detail']}).text

    # Some movies may not have classification and their detail doesn't contain '|' character.
    if '|' in detail:
        category, restriction = [word.strip() for word in detail.split('|')]
    else:
        category, restriction = (None, detail)

    return {
        'title': title,
        'category': category,
        'restriction': restriction,
    }


if __name__ == '__main__':
    response = requests.get(
        url=MOVIES_URL,
        proxies=PROXY_DICT
    )
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_card_divs = soup.find_all('div', attrs={'class': classes['movie_card']})
    movies = [parse_movie_item(item) for item in movie_card_divs]
