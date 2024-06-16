import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_popular_tracks():
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
    # 조건에 맞는 곡 이름들을 list에 append
    for i in data:
        if i['popularity'] >= 90:
            res.append(i['name'])

    return res


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
