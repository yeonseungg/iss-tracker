import requests
import datetime
import os

def get_iss_location():
    """
    ISS(국제 우주 정거장)의 현재 위치를 가져오는 함수
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        return latitude, longitude, timestamp
    else:
        print("❌ API 요청 실패!", response.status_code)
        return None, None, None

def update_readme(latitude, longitude, timestamp):
    """
    `README.md` 파일을 자동 생성 및 업데이트하는 함수
    """
    content = f"""# 🚀 ISS 위치 추적기

**현재 ISS 위치**  
🌍 위도: `{latitude}`  
🌍 경도: `{longitude}`  
📅 업데이트 시간: `{timestamp}`  

ISS의 현재 위치는 매일 자동 업데이트됩니다! 🌍
"""

    if not os.path.exists("README.md"):
        print("📝 README.md 파일을 새로 생성합니다.")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md 업데이트 완료!")

if __name__ == "__main__":
    lat, lon, time = get_iss_location()
    if lat and lon:
        update_readme(lat, lon, time)
