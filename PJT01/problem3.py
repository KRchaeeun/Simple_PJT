import pprint
import requests

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

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
  #key 값이 "result" 인 데이터를 출력하고 그 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
  option_list = response["result"]["optionList"]

  #option_list의 길이(개수)
  len_option = len(option_list)

  #비어있는 results 리스트 생성
  results = []

  #금융상품코드, 저축금리, 저축 기간, 저축금리유형, 저축금리유형명, 최고 우대금리를 key로 갖고 그에 맞는 value를 가질 수 있게 for 구문 사용
  for i in range(len_option):
    edit_data = {'금융상품코드' : option_list[i]['fin_prdt_cd'],
               '저축 금리' : option_list[i]['intr_rate'],
               '저축 기간': option_list[i]['save_trm'],
               '저축금리유형': option_list[i]['intr_rate_type'],
               '저축금리유형명': option_list[i]['intr_rate_type_nm'],
               '최고 우대금리': option_list[i]['intr_rate2']}
    
    #비어있는 results 리스트에 edit_data 삽입
    results.append(edit_data)
  

  return results

    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
