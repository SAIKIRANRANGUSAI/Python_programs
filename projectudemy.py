import requests as r
from dataclasses import dataclass


@dataclass
class Quote:
    quote: str
    author: str


url: str = 'https://api.quotable.io/random'
def get_Quote(url: str)-> Quote:
    request: r.Response = r.get(url=url)
    data: dict = request.json()

    content: str = data.setdefault('content', '...')
    author: str = data.setdefault('author','...')

    return Quote(content, author)


if __name__ == '__main__':
    url: str = 'https://api.quotable.io/random'

    for i in range(3):
        print()
        quote: Quote = get_Quote(url)

        print('quote:', quote.Quote)
        print('author:', quote.author)

