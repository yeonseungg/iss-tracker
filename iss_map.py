import requests
import folium

def get_iss_location():
    """
    ISS(국제 우주 정거장)의 현재 위치를 가져오는 함수
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        return latitude, longitude
    else:
        print("❌ API 요청 실패!", response.status_code)
        return None, None

def generate_iss_map():
    """
    ISS의 위치를 지도에 표시하여 HTML 파일로 저장하는 함수
    """
    lat, lon = get_iss_location()
    if lat is None or lon is None:
        return

    m = folium.Map(location=[lat, lon], zoom_start=3)
    folium.Marker([lat, lon], tooltip="🚀 ISS 위치", icon=folium.Icon(color="red")).add_to(m)

    m.save("iss_location.html")
    print("✅ ISS 위치가 'iss_location.html'에 저장되었습니다.")

if __name__ == "__main__":
    generate_iss_map()
