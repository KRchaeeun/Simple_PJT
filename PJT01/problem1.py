import pprint
import requests

# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

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

  #JSON 객체의 result 안에 있는 key 값 반환
  result_key = response["result"].keys()

  #JSON 객체의 result 안에 있는 key 값 반환
  return result_key
    



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

