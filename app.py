import streamlit as st
import pandas as pd
import time
import folium
from streamlit_folium import st_folium

# Simulated user database
USER_DB = {"test_user": "password123", "admin": "adminpass"}

# Sample data for visualization
DATA = pd.DataFrame({
    "Location": ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon"],
    "Latitude": [37.5665, 35.1796, 37.4563, 35.8714, 36.3504],
    "Longitude": [126.9780, 129.0756, 126.7052, 128.6014, 127.3845],
    "Value": [100, 150, 200, 120, 130]
})

# Login page
def login_page():
    st.title("로그인 페이지")
    username = st.text_input("사용자 이름")
    password = st.text_input("비밀번호", type="password")
    login_button = st.button("로그인")

    if login_button:
        if username in USER_DB and USER_DB[username] == password:
            st.success("로그인 성공!")
            with st.spinner("페이지로 이동 중..."):
                time.sleep(2)
            st.session_state["logged_in"] = True
        else:
            st.error("사용자 이름 또는 비밀번호가 잘못되었습니다.")

# Data analysis page
def data_analysis_page():
    st.title("데이터 분석 페이지")
    st.progress(100)

    # Display data
    st.header("📊 데이터 프레임")
    st.dataframe(DATA)

    # Add a graph
    st.header("📈 속성에 따른 그래프")
    selected_value = st.selectbox("그래프 속성 선택", ["Value"])
    st.bar_chart(DATA[selected_value])

    # Display map with location data
    st.header("🗺 지도에 위치 표시")
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=7)
    for i, row in DATA.iterrows():
        folium.Marker([row["Latitude"], row["Longitude"]], popup=row["Location"]).add_to(m)

    st_folium(m, width=700, height=500)

# Main app logic
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    data_analysis_page()