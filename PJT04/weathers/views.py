from django.shortcuts import render
import pandas as pd  # pandas 불러오고 pd로 저장
import matplotlib.pyplot as plt  # matplotlib.pyplot 불러오고 plt로 저장
# io: 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO: 이진 데이터를 다루기 위한 버퍼를 제공
from io import BytesIO  
import base64  # 텍스트 <-> 이진 데이터 변환할 수 있는 모듈

csv_path = 'weathers/data/austin_weather.csv'  # csv파일 위치 불러오기

# PROBLEM1: 데이터 읽어오기
def problem1(request):
    df = pd.read_csv(csv_path)  # csv파일 df에 저장
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)

# PROBLEM1: 일 별 온도 비교
def problem2(request):
    df = pd.read_csv(csv_path, usecols=range(0, 4))   # csv파일 4번재 열까지 df에 저장

    date = pd.to_datetime(df['Date'])  # df['Date'] 날짜 형식으로 변환하여 date로 저장
    high = df['TempHighF']  # df['TempHighF']를 high에 저장
    avg = df['TempAvgF']  # df['TempAvgF']를 avg에 저장
    low = df['TempLowF']  # df['TempLowF']를 low에 저장

    plt.clf()  # 그래프 초기화
    plt.figure(figsize=(12,7))  # 그래프 사이즈 설정

    # 그래프 그리기
    plt.plot(date, high, label='High Temperature')
    plt.plot(date, avg, label='Average Temperature')
    plt.plot(date, low, label='Low Temperature')

    # 스타일
    plt.title('Temperature Variation')  # 그래프 제목 입력
    plt.xlabel('Date')  # x축 제목 입력
    plt.ylabel('Temperate (Fahrenheit)')  # y축 제목 입력
    plt.grid()  # 그리드 그리기
    plt.legend()  # 범례 표시

    buffer = BytesIO()  # 비어있는 버퍼를 생성
    plt.savefig(buffer, format='png')  # 버퍼에 그래프를 저장

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')  # 버퍼의 내용을 base64로 인코딩
    buffer.close()  # 버퍼를 닫아줌

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path, usecols=range(0, 4))  # csv파일 4번재 열까지 df에 저장

    df['Date'] = pd.to_datetime(df['Date'])  # df['Date'] 날짜 형식으로 변환하여 date로 저장
    new = df.groupby(df['Date'].dt.strftime("%Y-%m")).mean()  # 월과 달 별로 Date를 그룹화하여 평균값을 구한 후 new에 저장

    plt.clf()  # 그래프 초기화
    plt.figure(figsize=(12,7))  # 그래프 사이즈 설정

    # 그래프 그리기
    plt.plot(new['Date'], new['TempHighF'], label='High Temperature')
    plt.plot(new['Date'], new['TempAvgF'], label='Average Temperature')
    plt.plot(new['Date'], new['TempLowF'], label='Low Temperature')

    # 그래프 스타일 
    plt.title('Temperature Variation')  # 그래프 제목 입력
    plt.xlabel('Date')  # x축 제목 입력
    plt.ylabel('Temperate (Fahrenheit)')  # y축 제목 입력
    plt.grid()  # 그리드 그리기
    plt.legend()  # 범례 표시

    buffer = BytesIO()  # 비어있는 버퍼를 생성
    plt.savefig(buffer, format='png')  # 버퍼에 그래프를 저장

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')  # 버퍼의 내용을 base64로 인코딩
    buffer.close()  # 버퍼를 닫아줌

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)  # csv파일 df에 저장
    # 아래처럼 했더니 SettingWithCopyWarning 경고문구가 떠서 loc을 사용함
    '''
    df_split = df.variable.str.split(',')
    table 
    for i in range(len(df_split)):
        df_split.get(i)
    for i in range(len(df)):
        if df['Events'][i] == ' ':
            df.loc['Events'][i] = 'No Events'
    '''

    # 결측치 이름 No Events로 바꾸기
    mask = df['Events'] == ' '
    df.loc[mask, 'Events'] = 'No Events'
    
    all_events = df['Events'].str.split(' , ').explode()  # 2개 이상 있는 경우 ,로 나누어져있으로 따로따로 저장하여 all_events에 저장

    event_counts = all_events.value_counts()  # all_events에 있는 변수에 따라 개수 세주기 

    plt.clf()  # 그래프 초기화
    plt.figure(figsize=(12,7))  # 그래프 사이즈 설정

    # 그래프 그리기(히스토그램)
    plt.bar(event_counts.index, event_counts.values)

    # 그래프 스타일   
    plt.title('Event Counts')  # 그래프 제목 입력
    plt.xlabel('Events')  # x축 제목 입력
    plt.ylabel('Count')  # y축 제목 입력
    plt.grid()  # 그리드 그리기
    plt.tight_layout()  # 각각의 히스토그램들이 붙어있지않고 떨어지도록 설정

    buffer = BytesIO()  # 비어있는 버퍼를 생성
    plt.savefig(buffer, format='png')  # 버퍼에 그래프를 저장

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')  # 버퍼의 내용을 base64로 인코딩
    buffer.close()  # 버퍼를 닫아줌

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem4.html', context)