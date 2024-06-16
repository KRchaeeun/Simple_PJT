import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params_arti = {
        'q': f'artist:{artist}',  # 필수 파라미터 artist 설정
        'type': 'artist',     # 필수 파라미터 artist 선택
        'market': 'KR',
        'limit' : 1           # 필요한 만큼의 정보만 받음
    }
    params_trak = {
        'q': f'track:{track}',  # 필수 파라미터 track 설정
        'type': 'track',     # 필수 파라미터 트랙을 선택
        'market': 'KR',
        'limit' : 1
    }

    # 필요한 artist 값을 호출
    response_arti = requests.get(f'{URL}/search', headers=headers, params=params_arti)
    response_arti = response_arti.json()
    data_arti = response_arti.get('artists').get('items')[0]
    artist_id = data_arti.get('id')

    # 필요한 track 값을 호출
    response_trak = requests.get(f'{URL}/search', headers=headers, params=params_trak)
    response_trak = response_trak.json()
    data_trak = response_trak.get('tracks').get('items')[0]
    track_id = data_trak.get('id')

    # 정리한 정보를 바탕으로 파라미터 설정
    params_rcm = {
        'limit' : 5,
        'market': 'KR',
        'seed_artists' : artist_id,
        'seed_genres': f'{genre}',
        'seed_tracks' : track_id
    }
    # recommendation에서 값 호출
    response_rcm = requests.get(f'{URL}/recommendations', headers=headers, params=params_rcm)
    response_rcm = response_rcm.json()
    data_rcm = response_rcm.get('tracks')

    res = []
    for info in data_rcm:
        res.append(info['name'])

    return res

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
