import streamlit as st
import pydeck as pdk
import pandas as pd

class Time:
    """A class that represents the time of day."""
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return f'T{self.hour:02}_{self.minute:02}_{self.second:02}'
    
    def to_seconds(self):
        return (self.hour * 60 + self.minute)*60 + self.second
    
    def from_seconds(self, seconds):
        self.minute, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(self.minute, 60)
        return self
    
    def __add__(self, other):
        return Time().from_seconds(self.to_seconds() + other.to_seconds())

    def __repr__(self):
        return f'T{self.hour:02}_{self.minute:02}_{self.second:02}'

st.write("""
# YouBike站點分析 :bike:

將滑鼠移動到站點上可以顯示及時站點資訊喔

""")


# Data from OpenStreetMap, accessed via osmpy
DATA_URL = "station_name1.json"
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

r = pdk.Deck(layers=[icon_layer], initial_view_state=view_state, tooltip={"text": "{station_name}\n可借數量：{rentable}\n車位：{space}", "style": {"color": "white"}})
st.pydeck_chart(r)

data2 = pd.read_json(DATA_URL)

time = st.select_slider(
    '請拉動時間軸',
    options=['06:00:00', '06:05:00', '06:10:00', '06:15:00', '06:20:00', '06:25:00', '06:30:00', '06:35:00', '06:40:00', '06:45:00', '06:50:00', '06:55:00', '07:00:00', '07:05:00', '07:10:00', '07:15:00', '07:20:00', '07:25:00', '07:30:00', '07:35:00', '07:40:00', '07:45:00', '07:50:00', '07:55:00', '08:00:00', '08:05:00', '08:10:00', '08:15:00', '08:20:00', '08:25:00', '08:30:00', '08:35:00', '08:40:00', '08:45:00', '08:50:00', '08:55:00', '09:00:00', '09:05:00', '09:10:00', '09:15:00', '09:20:00', '09:25:00', '09:30:00', '09:35:00', '09:40:00', '09:45:00', '09:50:00', '09:55:00', '10:00:00', '10:05:00', '10:10:00', '10:15:00', '10:20:00', '10:25:00', '10:30:00', '10:35:00', '10:40:00', '10:45:00', '10:50:00', '10:55:00', '11:00:00', '11:05:00', '11:10:00', '11:15:00', '11:20:00', '11:25:00', '11:30:00', '11:35:00', '11:40:00', '11:45:00', '11:50:00', '11:55:00', '12:00:00', '12:05:00', '12:10:00', '12:15:00', '12:20:00', '12:25:00', '12:30:00', '12:35:00', '12:40:00', '12:45:00', '12:50:00', '12:55:00', '13:00:00', '13:05:00', '13:10:00', '13:15:00', '13:20:00', '13:25:00', '13:30:00', '13:35:00', '13:40:00', '13:45:00', '13:50:00', '13:55:00', '14:00:00', '14:05:00', '14:10:00', '14:15:00', '14:20:00', '14:25:00', '14:30:00', '14:35:00', '14:40:00', '14:45:00', '14:50:00', '14:55:00', '15:00:00', '15:05:00', '15:10:00', '15:15:00', '15:20:00', '15:25:00', '15:30:00', '15:35:00', '15:40:00', '15:45:00', '15:50:00', '15:55:00', '16:00:00', '16:05:00', '16:10:00', '16:15:00', '16:20:00', '16:25:00', '16:30:00', '16:35:00', '16:40:00', '16:45:00', '16:50:00', '16:55:00', '17:00:00', '17:05:00', '17:10:00', '17:15:00', '17:20:00', '17:25:00', '17:30:00', '17:35:00', '17:40:00', '17:45:00', '17:50:00', '17:55:00', '18:00:00', '18:05:00', '18:10:00', '18:15:00', '18:20:00', '18:25:00', '18:30:00', '18:35:00', '18:40:00', '18:45:00', '18:50:00', '18:55:00', '19:00:00', '19:05:00', '19:10:00', '19:15:00', '19:20:00', '19:25:00', '19:30:00', '19:35:00', '19:40:00', '19:45:00', '19:50:00', '19:55:00', '20:00:00', '20:05:00', '20:10:00', '20:15:00', '20:20:00', '20:25:00', '20:30:00', '20:35:00', '20:40:00', '20:45:00', '20:50:00', '20:55:00', '21:00:00', '21:05:00', '21:10:00', '21:15:00', '21:20:00', '21:25:00', '21:30:00', '21:35:00', '21:40:00', '21:45:00', '21:50:00', '21:55:00', '22:00:00']
    )


timechange = 'T' + time.replace(':',"_",2)

colorchange ='[-'+timechange+' * 8 +255, 170, 100, 140]' 

past_layer = pdk.Layer(
    type="ColumnLayer",
    data = data,
    get_position=["lng", "lat"],
    get_elevation= timechange,
    elevation_scale = 20,
    radius = 20,
    get_fill_color= colorchange,
    pickable=True,
    auto_highlight = True
)

past = pdk.Deck(layers=[past_layer], initial_view_state=view_state)
st.pydeck_chart(past)


option = st.sidebar.selectbox(
    '可以在此選擇你想看的站點資訊',
    ('YouBike2.0_臺大醫學院附設癌醫中心', 'YouBike2.0_臺大環研大樓', 'YouBike2.0_臺大永齡生醫工程館', 'YouBike2.0_臺大男七舍前', 'YouBike2.0_臺大男一舍前', 'YouBike2.0_臺大男六舍前', 'YouBike2.0_臺大動物醫院前', 'YouBike2.0_臺大土木研究大樓前', 'YouBike2.0_臺大萬才館前', 'YouBike2.0_臺大國青大樓宿舍前', 'YouBike2.0_臺大社科院圖書館前', 'YouBike2.0_臺大法人語言訓練中心前', 'YouBike2.0_臺大綜合體育館停車場前', 'YouBike2.0_捷運公館站(3號出口)', 'YouBike2.0_臺大資訊大樓', 'YouBike2.0_捷運公館站(1號出口)', 'YouBike2.0_捷運公館站(4號出口)', 'YouBike2.0_捷運臺大醫院站(4號出口)', 'YouBike2.0_捷運臺大醫院站(1號出口)', 'YouBike2.0_臺大醫院兒童醫院', 'YouBike2.0_臺大水源舍區A棟', 'YouBike2.0_臺大卓越研究大樓', 'YouBike2.0_臺大水源修齊會館', 'YouBike2.0_臺大檔案展示館', 'YouBike2.0_臺大水源舍區B棟', 'YouBike2.0_臺大男八舍東側', 'YouBike2.0_臺大禮賢樓東南側', 'YouBike2.0_臺大農業陳列館北側', 'YouBike2.0_臺大管理學院二館北側', 'YouBike2.0_臺大土木系館', 'YouBike2.0_臺大大一女舍北側', 'YouBike2.0_臺大女九舍西南側', 'YouBike2.0_臺大小福樓東側', 'YouBike2.0_臺大立體機車停車場', 'YouBike2.0_臺大工綜館南側', 'YouBike2.0_臺大天文數學館南側', 'YouBike2.0_臺大心理系館南側', 'YouBike2.0_臺大樂學館東側', 'YouBike2.0_臺大農化新館西側', 'YouBike2.0_臺大五號館西側', 'YouBike2.0_臺大舊體育館西側', 'YouBike2.0_臺大共同教室北側', 'YouBike2.0_臺大共同教室東南側', 'YouBike2.0_臺大鹿鳴堂東側', 'YouBike2.0_臺大公館停車場西北側', 'YouBike2.0_臺大第二行政大樓南側', 'YouBike2.0_臺大明達館機車停車場', 'YouBike2.0_臺大二號館', 'YouBike2.0_臺大凝態館南側', 'YouBike2.0_臺大社科院西側', 'YouBike2.0_臺大社會系館南側', 'YouBike2.0_臺大思亮館東南側', 'YouBike2.0_臺大椰林小舖', 'YouBike2.0_臺大計資中心南側', 'YouBike2.0_臺大原分所北側', 'YouBike2.0_臺大生命科學館西北側', 'YouBike2.0_臺大第一活動中心西南側', 'YouBike2.0_臺大博理館西側', 'YouBike2.0_臺大博雅館西側', 'YouBike2.0_臺大森林館北側', 'YouBike2.0_臺大一號館', 'YouBike2.0_臺大小小福西南側', 'YouBike2.0_臺大教研館北側', 'YouBike2.0_臺大四號館東北側', 'YouBike2.0_臺大新生教室南側', 'YouBike2.0_臺大鄭江樓北側', 'YouBike2.0_臺大電機二館東南側', 'YouBike2.0_臺大圖資系館北側', 'YouBike2.0_臺大總圖書館西南側', 'YouBike2.0_臺大黑森林西側', 'YouBike2.0_臺大獸醫館南側', 'YouBike2.0_臺大新體育館東南側', 'YouBike2.0_臺大明達館北側(員工宿舍)'))

for i in range(len(data['station_name'])):
	if data['station_name'][i] == option:
		a = i
		break
	
st.sidebar.write(f"""
# {option}
## 此站點目前車況：
可借： {data['rentable'][a]} \n
可還： {data['space'][a] - data['rentable'][a]}

## 站點過去整天車況：
""")

###sidebar圖表
paststop = []
t = Time(6,0,0)
for i in range(193):
    timestr = str(t)[1:]
    b = timestr.replace('_',':',2)
    paststop += [[b, float(data2[str(t)][a])]]
    t += Time(0,5,0)
df = pd.DataFrame(paststop, columns=['TIME',"PERCENT"])
st.sidebar.line_chart(df, x='TIME', y='PERCENT')
###
