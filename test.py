import streamlit as st
import pydeck as pdk
import pandas as pd


# Data from OpenStreetMap, accessed via osmpy
DATA_URL = "station_name.json"
ICON_URL = "https://cdn-icons-png.flaticon.com/512/3236/3236695.png"

icon_data = {
    # Icon from Wikimedia, used the Creative Commons Attribution-Share Alike 3.0
    # Unported, 2.5 Generic, 2.0 Generic and 1.0 Generic licenses
    "url": ICON_URL,
    "width": 800,
    "height": 800,
    "anchorY": 800,
}

data = pd.read_json(DATA_URL)
data["icon_data"] = None
for i in data.index:
    data["icon_data"][i] = icon_data

view_state = pdk.ViewState(
    longitude=121.539204, latitude=25.017522, zoom=14.5, min_zoom=12, max_zoom=18, pitch=40.5, bearing=-27.36
)

icon_layer = pdk.Layer(
    type="IconLayer",
    data=data,
    get_icon="icon_data",
    get_size=4,
    size_scale=15,
    get_position=["lng", "lat"],
    pickable=True,
)

r = pdk.Deck(layers=[icon_layer], initial_view_state=view_state, tooltip={"text": "{station_name}\n可借數量：{rentable}\n可還數量：{space}", "style": {"color": "white"}})

option = st.sidebar.selectbox(
    '可以在此選擇你想看的站點資訊',
    ('YouBike2.0_捷運公館站(2號出口)', 'YouBike2.0_公館公園', 'YouBike2.0_臺大醫學院附設癌醫中心', 'YouBike2.0_臺大環研大樓', 'YouBike2.0_臺大永齡生醫工程館', 'YouBike2.0_臺大男七舍前', 'YouBike2.0_臺大男一舍前', 'YouBike2.0_臺大男六舍前', 'YouBike2.0_臺大動物醫院前', 'YouBike2.0_臺大土木研究大樓前', 'YouBike2.0_臺大萬才館前', 'YouBike2.0_臺大國青大樓宿舍前', 'YouBike2.0_臺大社科院圖書館前', 'YouBike2.0_臺大法人語言訓練中心前', 'YouBike2.0_臺大綜合體育館停車場前', 'YouBike2.0_捷運公館站(3號出口)', 'YouBike2.0_臺大資訊大樓', 'YouBike2.0_師範大學公館校區', 'YouBike2.0_師範大學公館校區_1', 'YouBike2.0_師大公館校區學二舍', 'YouBike2.0_捷運公館站(1號出口)', 'YouBike2.0_捷運公館站(4號出口)', 'YouBike2.0_捷運臺大醫院站(4號出口)', 'YouBike2.0_捷運臺大醫院站(1號出口)', 'YouBike2.0_臺大醫院兒童醫院', 'YouBike2.0_臺大水源舍區A棟', 'YouBike2.0_臺大卓越研究大樓', 'YouBike2.0_臺大水源修齊會館', 'YouBike2.0_臺大檔案展示館', 'YouBike2.0_臺大水源舍區B棟', 'YouBike2.0_臺大男八舍東側', 'YouBike2.0_臺大禮賢樓東南側', 'YouBike2.0_臺大農業陳列館北側', 'YouBike2.0_臺大管理學院二館北側', 'YouBike2.0_臺大土木系館', 'YouBike2.0_臺大大一女舍北側', 'YouBike2.0_臺大女九舍西南側', 'YouBike2.0_臺大小福樓東側', 'YouBike2.0_臺大立體機車停車場', 'YouBike2.0_臺大工綜館南側', 'YouBike2.0_臺大天文數學館南側', 'YouBike2.0_臺大心理系館南側', 'YouBike2.0_臺大樂學館東側', 'YouBike2.0_臺大農化新館西側', 'YouBike2.0_臺大五號館西側', 'YouBike2.0_臺大舊體育館西側', 'YouBike2.0_臺大共同教室北側', 'YouBike2.0_臺大共同教室東南側', 'YouBike2.0_臺大鹿鳴堂東側', 'YouBike2.0_臺大公館停車場西北側', 'YouBike2.0_臺大第二行政大樓南側', 'YouBike2.0_臺大明達館機車停車場', 'YouBike2.0_臺大二號館', 'YouBike2.0_臺大凝態館南側', 'YouBike2.0_臺大社科院西側', 'YouBike2.0_臺大社會系館南側', 'YouBike2.0_臺大思亮館東南側', 'YouBike2.0_臺大椰林小舖', 'YouBike2.0_臺大計資中心南側', 'YouBike2.0_臺大原分所北側', 'YouBike2.0_臺大生命科學館西北側', 'YouBike2.0_臺大第一活動中心西南側', 'YouBike2.0_臺大博理館西側', 'YouBike2.0_臺大博雅館西側', 'YouBike2.0_臺大森林館北側', 'YouBike2.0_臺大一號館', 'YouBike2.0_臺大小小福西南側', 'YouBike2.0_臺大教研館北側', 'YouBike2.0_臺大四號館東北側', 'YouBike2.0_臺大新生教室南側', 'YouBike2.0_臺大鄭江樓北側', 'YouBike2.0_臺大電機二館東南側', 'YouBike2.0_臺大圖資系館北側', 'YouBike2.0_臺大總圖書館西南側', 'YouBike2.0_臺大黑森林西側', 'YouBike2.0_臺大獸醫館南側', 'YouBike2.0_臺大新體育館東南側', 'YouBike2.0_臺大明達館北側(員工宿舍)'))

for i in range(len(data['station_name'])):
	if data['station_name'][i] == option:
		a = i
		break
	
st.sidebar.write(f"""
# {option}
## 此站點目前車況：
可借： {data['rentable'][a]} \n
可還： {data['space'][a]}

## 站點過去整天車況：
""")

st.write("""
# YouBike站點分析 :bike:

將滑鼠移動到站點上可以顯示及時站點資訊喔

""")
st.pydeck_chart(r)