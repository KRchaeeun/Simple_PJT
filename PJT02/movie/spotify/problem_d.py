import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'artist:{name}',  # 필수 파라미터 artist name을 input으로 받아
        'type': 'artist',     # 필수 파라미터
        'market': 'KR',
        'limit': 1
    }
    params2 = {
        'q': f'artist:{name}',  # 필수 파라미터 artist name을 input으로 받아
        'type': 'artist',     # 필수 파라미터
        'market': 'KR',
        'limit': 1
    }

    # api를 이용해 값을 호출
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    # 바뀐 type에 따라 key값들을 변경
    data = response.get('artists').get('items')
    # id의 값을 가져올 수 있는 경우
    try:
        id = data[0]['id']

        # id 를 기반으로 검색
        response2 = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers, params=params2)
        data2 = response2.json()
        data2 = data2.get('artists')

        res = []

        # 관련있는 name들을 결과에 append
        for i in data2:
            res.append(i['name'])

        return res
    # id의 값을 가져올 수 없는 경우
    except:
        return

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    print(get_related_artists('NewJeans'))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists('OldShirts'))
    # None
