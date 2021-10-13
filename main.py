import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(url, headers):
    host_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    src_url = {'long_url': url}
    response = requests.post(host_url, headers=headers, json=src_url)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(link, headers):
    parsed_link = urlparse(link)
    if parsed_link.scheme:
        link = f'{parsed_link.netloc}{parsed_link.path}'
    host_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(host_url, headers=headers)
    response.raise_for_status()
    click_count = response.json()['total_clicks']
    return click_count


def is_bitlink(url, headers):
    parsed_url = urlparse(url)
    if parsed_url.scheme:
        url = f'{parsed_url.netloc}{parsed_url.path}'
    host_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}' 
    response = requests.get(host_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_GENERIC_ACCESS_TOKEN']
    headers = {'Authorization': f'Bearer {token}'}
    parser = argparse.ArgumentParser(
        description=
        'It converts url to bitly short link. '
        'If a short link typed, it shows clicks count.'
    )
    parser.add_argument('link', help='URL or bitly short link')
    args = parser.parse_args()
    url = args.link
    if is_bitlink(url, headers):
        try:
            click_count = count_clicks(url, headers)
            print('Clicks count', click_count)
        except requests.exceptions.HTTPError:
            print('Unable to define')
    else:
        try:
            bitlink = shorten_link(url, headers)
            print('Bitlink:', bitlink)
        except requests.exceptions.HTTPError:
            print('Wrong link')


if __name__ == '__main__':
    main()