import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.

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

  #API 요청 보내기, 응답을 json 형태로 변환하고 JSON 객체의 result 안에 있는 key 값 반환
  response = requests.get(url, params = params).json()["result"]
  
  #위 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
  base_list = response["baseList"] 

  #위 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
  option_list = response["optionList"]

  #비어있는 results 리스트 생성
  result = []

  
  for item in base_list:
     
    #비어있는 results 리스트 생성
    inside_base = []

    #금리정보, 금융상품명, 금융회사명의 큰 key(?)들을 넣어 큰 틀을 잡기
    return_final = {'금리정보': inside_base,
                     '금융상품명': item['fin_prdt_nm'],
                     '금융회사명': item['kor_co_nm']}
    
    # 금리정보 안에 들어갈 key와 value들을 넣기
    for para in option_list:
        
        #위에 for구문과 이번 for구문이 같지 않으면 계속 반복되므로 필요함.
        if item['fin_prdt_cd']==para['fin_prdt_cd']:
           detail_base = {'저축 금리' : para['intr_rate'],
               '저축 기간': para['save_trm'],
               '저축금리유형': para['intr_rate_type'],
               '저축금리유형명': para['intr_rate_type_nm'],
               '최고 우대금리': para['intr_rate2']}
           
           #비어있는 inside_base에 detail_base 삽입
           inside_base.append(detail_base)

    #비어있는 result에 return_final 삽입
    result.append(return_final)
           
  return result
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)