import pandas as pd
import matplotlib.pyplot as plt

# 폰트 세팅 모듈
from matplotlib import font_manager, rc
font_path = "/Users/hongjimin/kosta/Python/Project/NanumSquareR.ttf"
plt.rcParams['axes.unicode_minus'] = False
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

# CSV 파일 읽기
data = pd.read_csv('delivery.csv', header=None)

# 열 이름 설정
data.columns = ['광역시도명', '시군구명', '날짜', '시간대별 시간', '강수 유형명', '습도값', '강수량 값', '기온값', '풍속값', '바람강도 유형명', 
                '동쪽서쪽바람유형명', '풍향값', '풍향카테고리명', '한식_배달건수', '분식_배달건수', '카페/디저트_배달건수', 
                '돈까스/일식_배달건수', '회_배달건수', '치킨_배달건수', '피자_배달건수', '아시안/양식_배달건수', '중식_배달건수', 
                '족발/보쌈_배달건수', '야식_배달건수', '찜탕_배달건수', '도시락_배달건수', '패스트푸드_배달건수']

# 날짜 데이터를 Datetime 형식으로 변환
data['날짜'] = pd.to_datetime(data['날짜'])



# 1. 기온이 배달 주문량에 어떤 영향을 미치는가?

# 시각
plt.figure(figsize=(15, 9))
plt.scatter(data['기온값'], data['치킨_배달건수'], alpha=0.5, c='gold')
plt.xlabel('기온 (℃)')
plt.ylabel('치킨 배달건수')
plt.title('기온이 배달 주문량에 어떤 영향을 미치는가?')
plt.show()




# 2. 지역별로 날씨에 따른 주문 패턴의 차이는 있는가?

# 지역별로 배달 건수 합산
delivery_by_region = data.groupby(['광역시도명'])[['한식_배달건수', '분식_배달건수', '카페/디저트_배달건수', 
                                                           '돈까스/일식_배달건수', '회_배달건수', '치킨_배달건수', '피자_배달건수', 
                                                           '아시안/양식_배달건수', '중식_배달건수', '족발/보쌈_배달건수', 
                                                           '야식_배달건수', '찜탕_배달건수', '도시락_배달건수', '패스트푸드_배달건수']].sum()

# 시각화
delivery_by_region.plot(kind='bar', figsize=(15, 9), width=0.8)
plt.xlabel('지역')
plt.ylabel('배달건수')
plt.title('지역별 배달 카테고리별 건수')
plt.legend(title='배달 카테고리', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()




# 3. 날씨에 따라 배달 건수의 차이가 있는가?

# 각 날씨 종류별 전체 배달 건수
weather_total_orders = data.groupby('강수 유형명')[['한식_배달건수', '분식_배달건수', '카페/디저트_배달건수', 
                '돈까스/일식_배달건수', '회_배달건수', '치킨_배달건수', '피자_배달건수', '아시안/양식_배달건수', '중식_배달건수', 
                '족발/보쌈_배달건수', '야식_배달건수', '찜탕_배달건수', '도시락_배달건수', '패스트푸드_배달건수']].sum()

# 시각화 (꺾은선 그래프)
weather_total_orders.plot(kind='line', figsize=(15, 9), marker='o')
plt.xlabel('날씨')
plt.ylabel('전체 배달건수(백만)')
plt.title('날씨에 따라 배달 건수의 차이가 있는가?')
plt.grid(True)
plt.tight_layout()
plt.show()
