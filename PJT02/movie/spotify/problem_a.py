import requests
from pprint import pprint
from examples.spotify_config import getHeaders

def get_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': 'genre:k-pop',  # 필수 파라미터 genre를 k-pop으로 설정
        'type': 'track',     # 필수 파라미터
        'market': 'KR',
        'limit': 20
    }

    # api를 이용해 값을 호출
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    data = response.get('tracks').get('items')

    # 결과값을 넣을 list 생성
    res = []
    # 곡 이름들을 list에 append
    for i in data:
        res.append(i['name'])

    return res

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    장르가 k-pop인 음악트랙 20개 가져오기
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_tracks())
    """
    ['Cupid - Twin Ver.',
    'Take Two',
    'Like Crazy',
    'MONEY',
    'OMG',
    'Like Crazy',
    'Ditto',
    'Bite Me',
    'FLOWER',
    'UNFORGIVEN (feat. Nile Rodgers)',
    'Super',
    'Hype Boy',
    'The Planet',
    'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]',
    'Like Crazy (English Version)',
    'Cupid',
    'Run BTS',
    'Eve, Psyche & The Bluebeard’s wife',
    'Tally',
    'Spicy']
    """
