import streamlit as st
import pandas as pd
import numpy as np

# Set up a shared Google Sheet URL or local storage for demonstration
DATA_URL = "data.csv"  # Replace with a Google Sheet API or use Streamlit Cloud for real-time updates

# Initialize the app
st.title("지진 데이터 공유 및 분석 플랫폼")
st.write("학생들이 조별로 지진 데이터를 입력하고, 함께 분석할 수 있는 플랫폼입니다.")

# Data input section
st.header("📥 조별 지진 데이터 입력")
with st.form("data_input_form"):
    group = st.text_input("조 이름 또는 번호", "")  # 조 입력 필드
    name = st.text_input("작성자 이름", "")
    region = st.text_input("지진 발생 지역", "")
    magnitude = st.number_input("지진 규모", min_value=0.0, step=0.1, format="%.1f")
    date = st.date_input("지진 발생 날짜")
    submit = st.form_submit_button("데이터 제출")

    if submit:
        if not group or not name or not region:
            st.error("조 이름, 작성자 이름, 지진 발생 지역은 필수 입력 항목입니다!")
        else:
            new_data = {
                "조": [group],
                "작성자": [name],
                "지역": [region],
                "규모": [magnitude],
                "날짜": [date],
            }
            new_df = pd.DataFrame(new_data)
            try:
                existing_data = pd.read_csv(DATA_URL)
                updated_data = pd.concat([existing_data, new_df], ignore_index=True)
                updated_data.to_csv(DATA_URL, index=False)
                st.success("데이터가 성공적으로 추가되었습니다!")
            except FileNotFoundError:
                new_df.to_csv(DATA_URL, index=False)
                st.success("데이터 파일이 생성되고 데이터가 추가되었습니다!")

# Data sharing section
st.header("📊 실시간 데이터 공유")
try:
    data = pd.read_csv(DATA_URL)
    st.write("현재까지 입력된 데이터를 확인하세요:")
    st.dataframe(data)
    
    # Visualization
    st.header("📈 데이터 시각화")
    if not data.empty:
        st.write("지역별 지진 발생 횟수:")
        region_counts = data["지역"].value_counts()
        st.bar_chart(region_counts)

        st.write("지역별 평균 지진 규모:")
        avg_magnitude = data.groupby("지역")["규모"].mean()
        st.bar_chart(avg_magnitude)

        st.write("조별 데이터 분석:")
        group_summary = data.groupby("조").size()
        st.bar_chart(group_summary)
except FileNotFoundError:
    st.warning("아직 데이터가 없습니다. 데이터를 먼저 입력해 주세요.")

# Allow download of the collected data
st.header("📥 데이터 다운로드")
try:
    if not data.empty:
        st.download_button(
            label="전체 데이터 다운로드",
            data=data.to_csv(index=False),
            file_name="earthquake_data.csv",
            mime="text/csv"
        )
except NameError:
    st.warning("다운로드할 데이터가 없습니다. 데이터를 먼저 입력해 주세요.")