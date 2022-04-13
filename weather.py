# Ch. 3-10 언어 및 단위 변경하기
# 화씨는 섭씨로, 영어는 한국어로

# api를 call할 때 한국어 값으로 넘어올 수 있도록 lang 값 추가하기
# 파라미터는 api를 사용하기 위한 약속. 꼭 써야하는 것도 있고, 굳이 쓰지 않아도 되는 것들도 있다.
# 파라미터는 &로 이어진다! lang 안에 일단 변수 lang 적어둠.

import requests
import json

city = "Seoul"
apikey = "b7b91bf00e8d122625fcf8d3c3296e31"
lang = "kr" # lang 파라미터 안에 들어갈 수 있는 나라 코드들은 지정되어 있다.
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
# OpenWeatherMap API를 이용하면 복잡한 수식을 거치지 않고도
# 온도 단위를 화씨에서 섭씨로 변경할 수 있다.(물론 units 파라미터 추가 필요)

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)

# 지역 : name
print(data["name"],"의 날씨입니다.")
# 자세한 날씨 : weather - description
print("날씨는 ", data["weather"][0]["description"],"입니다.")
# 현재 온도 : main - temp
print("현재 온도는 ", data["main"]["temp"],"입니다.")
# 체감 온도 : main - feels_like
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은, ", data["main"]["temp_min"], "입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
# 습도 : main - humidity
print("습도는 ", data["main"]["humidity"], "입니다.")
# 기압 : main - pressure
print("기압은 ", data["main"]["pressure"], "입니다.")
# 풍향 : wind - deg
print("풍향은 ", data["wind"]["deg"], "입니다.")
# 풍속 : wind - speed
print("풍속은 ", data["wind"]["speed"], "입니다.")