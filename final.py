

import streamlit as st

# 페이지 설정
st.set_page_config(page_title="세상을 지키는 데이터", page_icon="🌍")


import base64

# 배경 이미지 적용 함수
def set_bg(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 배경 이미지 설정
set_bg("background.png")  # PNG 파일 사용



# 기본 페이지 메뉴 숨기기
hide_menu_style = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none; /* 사이드바 상단 메뉴 숨기기 */
    }
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 사이드바 커스텀 메뉴
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #4b8bbe;
        text-align: center;
    }
    </style>
    <p class="sidebar-title">🌍 세상을 지키는 데이터 🌍</p>
""", unsafe_allow_html=True)

# Streamlit 페이지 링크 설정
st.sidebar.page_link("pages/1차시.py", label="1차시: 데이터 탐색 및 정리")
st.sidebar.page_link("pages/2차시.py", label="2차시: 데이터 시각화 및 분석")
st.sidebar.page_link("pages/3차시.py", label="3차시: 대책 설계 및 발표")

# 메인 페이지 내용
st.title("🌍 세상을 지키는 데이터 - 지진 분석과 예측 🌍")
st.write("### 중학교 3학년을 위한 프로젝트 수업입니다.")
st.write("실제 데이터를 탐구하고 이를 활용하여 지진 예방과 대비책을 설계하고, 데이터를 시각화하고 이를 분석하며 지진학자로서의 역할을 수행해 지역사회의 문제를 해결해 보도록 합시다.")
st.write("---")

# 사용자 입력 받기
st.subheader("📝 반, 조, 이름을 입력해 주세요")

# 반과 조는 스크롤 선택
class_number = st.selectbox("반", [f"{i}반" for i in range(1, 11)], index=0)  # 1반~10반
team = st.selectbox("조", [f"{i}조" for i in range(1, 7)], index=0)  # 1조~6조

# 이름 입력
name = st.text_input("이름", placeholder="예: 홍길동")

# 전송 버튼
if st.button("전송"):
    if class_number and team and name:
        st.success(f"✅ 입력이 완료되었습니다: **{class_number} {team} {name}**")
    else:
        st.warning("⚠️ 모든 항목을 입력해 주세요.")

st.subheader("📚 차시별 내용")
with st.expander("1️⃣ **1차시: 데이터 탐색 및 정리**"):
    st.write("""
    - 한반도 주요 지진 사례를 탐색합니다.  
    - 데이터를 정리하고 주요 변수를 선별합니다.  
    - 데이터의 유효성과 분석 방법을 이해합니다.  
    """)

with st.expander("2️⃣ **2차시: 데이터 시각화 및 분석**"):
    st.write("""
    - 지진 데이터를 시각화하고 분석합니다.  
    - 히스토그램과 산점도를 작성하여 데이터 특성을 이해합니다.  
    - 분석 결과를 바탕으로 지진 경향을 해석합니다.  
    """)

with st.expander("3️⃣ **3차시: 대책 설계 및 발표**"):
    st.write("""
    - 분석된 데이터를 바탕으로 지진 위험 지역을 선정합니다.  
    - 안전한 지역 설계 및 대피소, 병원 배치를 계획합니다.  
    - 팀별 발표 자료를 제작하고 공유합니다.  
    """)

st.write("---")
st.info("📢 데이터와 기술적 어려움이 있다면 언제든 선생님께 질문하세요.")

