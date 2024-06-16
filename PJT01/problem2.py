import pprint
import requests

# 전체 정기예금 상품 리스트를 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "baseList" 인 데이터를 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = "51095dd1046709225382ff5ab890353c"

  #JSON url을 위 api_key를 사용하여 데이터를 받아왔다.
  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

  params = {
      'auth': api_key,  #인증키
      'topFinGrpNo': '020000',  #금융회사가 속한 권역코드(020000:은행, 030200:여신전문, 030300: 저축은행, 050000: 보험, 060000: 금융투자)
      'pageNo': 1  #조회하고자 하는 페이지 번호
  }

  #API 요청 보내기, 응답을 json 형태로 변환
  response = requests.get(url, params = params).json()
  
  #key 값이 "result" 인 데이터를 출력합니다.
  base_list = response["result"]["baseList"]

  #key 값이 "baseList" 인 데이터를 출력합니다.
  return base_list

    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)