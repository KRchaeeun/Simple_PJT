# 01-pjt



## 학습한 내용   
 
1. 서버: 부탁을 받으면 처리해주거나, 원하는 값을 돌려줌  
2. 클라이언트: 부탁하는 역할  
3. API: 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램, 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둡니다.  
4. 오픈 API: 외부에서 사용할 수 있도록 무료로 개방(Open)된 API  
오픈 API특징 및 주의사항  
- 악성 사용자가 계정을 많이 생성해 API에 요청을 보내면 서버가 견디지 못하므로 AIP KEY를 활용하여 사용자를 확인한다.  
- 일부 오픈 API는 사용량이 제한되어 있다. 사용량이 초과될 경우 요금이 청구 될 수 있다.
5. Parsing: 데이터를 의미 있는 구조로 분석하고 해석하는 과정, 파싱은 원하는 형태로 추출, 변화하는 것도 포괄적으로 포함  
6. json.loads(): JSON 형식의 문자열을 파싱하여 python Dictionary로 변환  
7. url: 요청을 보내는 서버의 주소  
8. requests.get(url): 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수  
9. .json(): 내부의 데이터를 JSON(파이썬의 딕셔너리와 비슷함) 형태를 변환해주는 함수
  
서버에서 정보 받는 방법  
- 클라이언트는 request라는 python 라이브러리를 통해 요청을 보낼 수 있다  
- 웹브라우저(크롬)을 켜서 주소창에 주소 (URL)을 입력한다.  
  
    
      
API KEY 발급  
1. 사이트에 접속하고 회원가입 진행  
2. API Keys 탭으로 이동  
3. API Key 복사  
  
  

## PJT  
  
A. 데이터 추출 - Key 값 출력하기  
전체 정기예금의 응답을 json 형태로 변환 후 아래와 같이 Key 값만 출력하도록 구성합니다.  
```
dict_keys(['prdt_div', 'total_count', 'max_page_no', 'now_page_no', 'err_cd', 'err_msg', 'baseList', 'optionList'])  
```  
공식 문서의 요청 변수 및 예제 요청결과(JSON) 부분을 참고합니다.  
[힌트] 모든 데이터는 JSON 객체의 "result" 키 값으로 조회할 수 있습니다.  
  

B. 데이터 추출 - 전체 정기예금 상품 리스트  
- 응답 중 정기예금 상품 리스트 정보만 출력하도록 구성합니다.  
- 출력 예시  
```
{'dcls_end_day': None,
  'dcls_month': '202307',
  'dcls_strt_day': '20230721',
  'etc_note': '※ 기본금리 및 최고 우대금리 항목은 가입기간이 아닌 ‘회전주기’기간
별 금리를 공시\n'
              ' - 회전주기는 1개월 이상 12개월 이내 월단위로 선택 가능\n'       
              '※ 전월취급평균금리는 본 홈페이지에 공시되지 않는 회전기간 6개월  
미만의 계좌들도 포함하여 산출하기 때문에 '
              '회전기간별로 공시된 기본금리보다 낮게 보여질 수 있음',
  'fin_co_no': '0013175',
  'fin_co_subm_day': '202307211039',
  'fin_prdt_cd': '10-003-1225-0001',
  'fin_prdt_nm': 'NH왈츠회전예금 II',
  'join_deny': '1',
  'join_member': '개인',
  'join_way': '영업점,인터넷,스마트폰',
  'kor_co_nm': '농협은행주식회사',
  'max_limit': None,
  'mtrt_int': '만기 후 3개월 : 기본금리의 50%\n'
              '만기 후 6개월 : 기본금리의 20%\n'
              '만기 후 6개월 초과 : 기본금리의 10%\n'
              '\n'
              '* 기본금리 : 만기시점의 일반정기예금 계약기간별 금리',
  'spcl_cnd': '1. 급여이체실적(50만원 이상)이 있는 경우 : 0.1%p\n'
              '2. 트리플 회전 우대이율 :  4회전기간부터 0.1%p'}  
```  
  

C. 데이터 가공 - 전체 정기예금 옵션 리스트  
- 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.  
- 이 때, 원하는 데이터만 추출하여 출력되는 결과를 아래와 같이 변경하여 반화하는 함수를 작성하시오.  
- 출력 결과 예시  
```
 {'금융상품코드': '10-01-20-388-0002',
  '저축 금리': 3.5,
  '저축 기간': '36',
  '저축금리유형': 'S',
  '저축금리유형명': '단리',
  '최고 우대금리': 3.5}
  ```  
- [참고] Python Dictionary 원하는 키 값으로 데이터 추가하기  
```
new_dict = {}  
new_dict['추가'] = "test"  
print(new_dict)
```  
```
##출력 결과  
{'추가': 'test'}
```  
  

D. 데이터 가공 - 새로운 값을 만들어 반환하기  
- 상품과 옵션 정보들을 담고 있는 새로운 값을 만들어 딕셔너리 형태로 반환하도록 구성한다.  
- 다음과 가틍 ㄴ값만 추출하여 새로운 값에 포함합니다.  
   금융 상품: '금융회사명', '금융상품명', '금리정보'  
   해당 금융 상품의 금리 정보(옵션): '저축금리유형', '저축금리유형명', '저축기간', '저축 금리', '최고 우대 금리'  
   하나의 금융 상품에 대해 여러 개의 옵션을 가질 수 있습니다.  
[힌트] 금융 상품 코드가 가은 금융 상품과 옵션을 하나의 딕셔너리로 만듭니다.  
- 출력 결과 예시  
```
{'저축 금리': 3.5,
            '저축 기간': '36',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.5}],
  '금융상품명': '카카오뱅크 정기예금',
  '금융회사명': '주식회사 카카오뱅크'}]
```
  
  
  
## 어려웠던 부분  
항상 반복문을 사용할 때 comprehension을 잘 생각해 내지 못해서 코드가 복잡해져서 길을 자주 잃어 버린다. 물론 너무 comprehension을 남용하면 좋지 않지만 그래도 적절하게 사용하면 더 효율적이게 문제를 해결 할 수 있을 거 같다.  
너무 세세하게 조건을 나누려고 한다. 생각해보면 반복되는 것은 간단하게 구현 할 수 있기 때문에 앞으로는 생각을 좀 간단하게 정리하는게 좋을 거 같다.  
실습 때 풀었던 내용에 조금 변형되서 풀어야 하는 문제였는데 항상 복습을 꼭 해야겠다.  
  
  


## 새로 배운 것들 및 느낀점  
4일 동안 배웠던 문제들이 나와서 새로 배운 내용은 없지만 복습을 꼭 하고 실습 문제들은 여러번 풀어봐야겠다고 생각했다.