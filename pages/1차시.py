import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="세상을 지키는 데이터", page_icon="🌍")

# 페이지 배경 색상 설정
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D8E6EA;  /* 연한 하늘색 배경 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 기본 페이지 메뉴 숨기기
hide_menu_style = """
    <style>
    [data-testid="stSidebarNav"] {
        display: none; /* 사이드바 상단 메뉴 숨기기 */
    }
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 사이드바 CSS 스타일링
st.sidebar.markdown("""
    <style>
    /* 제목 스타일 */
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        color: #4b8bbe;
        text-align: center;
        margin-bottom: 20px;
    }

    /* 링크 버튼 스타일 */
    .sidebar-link {
        font-size: 18px;
        font-weight: bold;
        color: white;
        margin: 10px 0;
        padding: 10px;
        display: block;
        text-align: center;
        text-decoration: none;
        border-radius: 10px;
        background-color: #4b8bbe;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s, box-shadow 0.3s;
    }

    /* 링크 호버 효과 */
    .sidebar-link:hover {
        background-color: #0050b3;
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.2);
        color: #e6f7ff;
    }

    /* 링크 간격 */
    .sidebar-gap {
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 사이드바 제목
st.sidebar.markdown('<p class="sidebar-title">🌍 세상을 지키는 데이터 </p>', unsafe_allow_html=True)

# 메인 페이지 링크
st.sidebar.markdown("""
    <a href="/" target="_self" class="sidebar-link">메인 페이지로 이동</a>
""", unsafe_allow_html=True)

# 간격 추가
st.sidebar.markdown('<div class="sidebar-gap"></div>', unsafe_allow_html=True)

# Streamlit 페이지 링크 설정
st.sidebar.page_link("pages/1차시.py", label="1차시: 데이터 탐색 및 정리")
st.sidebar.page_link("pages/2차시.py", label="2차시: 데이터 시각화 및 분석")
st.sidebar.page_link("pages/3차시.py", label="3차시: 대책 설계 및 발표")

# 페이지 타이틀
st.title("🌍 한반도 주요 지진 사례")
st.write("### 포항과 경주 지진 사례를 통해 데이터 분석의 중요성을 생각해 봅시다!")

# 포항 지진 사례
st.subheader("📍 2017 포항 지진")
col1, col2 = st.columns(2)  # 사진 두 개를 나란히 배치
with col1:
    st.image("pohang1.png", caption="포항 지진 - 피해 건물 1", use_container_width=True)
with col2:
    st.image("pohang2.png", caption="포항 지진 - 피해 건물 2", use_container_width=True)

st.write("""
- **발생일**: 2017년 11월 15일  
- **규모**: 5.4  
- **위치**: 경상북도 포항시 북구  
- **피해**: 건물 파손, 부상자 발생, 학교 및 공공시설 피해  
""")

# 경주 지진 사례
st.subheader("📍 2016 경주 지진")
col3, col4 = st.columns(2)  # 사진 두 개를 나란히 배치
with col3:
    st.image("gyeongju1.png", caption="경주 지진 - 피해 현장 1", use_container_width=True)
with col4:
    st.image("gyeongju2.png", caption="경주 지진 - 피해 현장 2", use_container_width=True)

st.write("""
- **발생일**: 2016년 9월 12일  
- **규모**: 5.8  
- **위치**: 경상북도 경주시 남남서쪽  
- **피해**: 문화재 손상, 건물 균열, 여진 다수 발생  
""")

# 섹션 타이틀
st.subheader("❓ 데이터 분석의 필요성")
st.write("""
지진 피해를 줄이기 위해 데이터를 분석하는 것이 왜 중요할까요?  
**힌트를 확인**해 보세요!
""")

# 힌트 확인 버튼
if st.button("💡 힌트 확인"):
    st.info("데이터를 분석하면 **지진이 자주 발생하는 지역**과 **규모의 경향**을 이해할 수 있습니다.")

# 생각을 작성할 수 있는 텍스트 영역
st.subheader("✍️ 나의 생각")
user_input = st.text_area("데이터 분석의 중요성에 대해 적어보세요.", placeholder="여기에 생각을 적어보세요.")

# 전송 버튼 기능 추가
if st.button("🚀 전송"):
    if user_input:  # 내용이 입력되었는지 확인
        st.success("✅ 입력이 전송되었습니다! 잘 적어주셨습니다.")
    else:
        st.warning("⚠️ 내용을 입력해 주세요!")

        # 섹션 타이틀
st.title("🌍 **지진학자 역할 부여**")
st.write("### 여러분은 오늘부터 **지진학자**입니다!")

# 프로젝트 목표 설명
st.markdown("""
<style>
    .role-card {
        background-color: #F0F8FF; /* 부드러운 파란색 배경 */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 18px;
        color: #333333;
        margin: 10px 0;
    }
    .goal-card {
        background-color: #FAFAD2; /* 밝은 노란색 배경 */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        font-size: 16px;
        color: #555555;
        margin: 10px 0;
    }
    .emoji {
        font-size: 24px;
    }
</style>
""", unsafe_allow_html=True)

# 지진학자 역할 부여 카드
st.markdown("""
<div class="role-card">
    <span class="emoji">👩‍🔬👨‍🔬</span>  
    여러분은 이제 지진학자입니다!
    데이터를 탐구하고 분석하며,  
    지진의 위험성을 이해하고 해결책을 설계하는 중요한 역할을 수행합니다.
</div>
""", unsafe_allow_html=True)

# Google Sheets 링크
sheet_url = "https://docs.google.com/spreadsheets/d/1gND_Z1wN4CxVfZS4djqW0kcs6eq4IiVv7hz2zpaT2SY/edit?usp=sharing"

# 다음 단계 안내
st.write("---")
st.write("👉 **이제 준비되셨나요?** 탐구를 시작해 봅시다! 기상청 기상자료개방포털에서 원하는 기간, 규모를 설정하여 그에 해당하는 시간, 규모, 진앙, 위도, 경도, 위치에 대한 지진 자료를 얻은 뒤, 이를 Google sheets에 입력해봅시다! 아래 링크를 클릭하면 **Google Sheets**에 접속하여 데이터를 입력하거나 확인할 수 있습니다. 데이터를 입력한 후 실시간으로 업데이트되는 결과를 확인해 봅시다!")


# Google Sheets 링크 버튼
st.markdown(f"""
    <a href="{sheet_url}" target="_blank" style="
        display: inline-block;
        padding: 10px 20px;
        margin: 20px 0;
        font-size: 18px;
        color: white;
        background-color: #4CAF50;
        text-align: center;
        text-decoration: none;
        border-radius: 10px;">
        📝 Google Sheets 열기
    </a>
""", unsafe_allow_html=True)

import pandas as pd

# 한글 폰트 설정 (Windows 기준)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 '맑은 고딕'
matplotlib.rcParams['axes.unicode_minus'] = False    # 마이너스 기호 깨짐 방지


# 페이지 타이틀
st.title("📊 주요 변수 선별 및 분석 방법 안내")
st.write("### 데이터를 시각화하여 **규모**와 **발생 빈도**를 분석해 봅시다!")

# 예제 데이터 (교사 제공용)
data = {
    "지역": ["포항", "경주", "서울", "부산", "대구"],
    "규모": [5.4, 5.8, 3.2, 4.1, 3.8],
    "발생 빈도": [3, 4, 2, 3, 2]
}
df = pd.DataFrame(data)

# 주요 변수 시각화
st.subheader("📌 주요 변수 시각화")

# 히스토그램: 지진 규모
st.write("**1. 지진 규모 분포**")
fig, ax = plt.subplots()
ax.bar(df["지역"], df["규모"], color='skyblue')
plt.title("지역별 지진 규모")
plt.xlabel("지역")
plt.ylabel("규모")
st.pyplot(fig)

# 막대 그래프: 발생 빈도
st.write("**2. 발생 빈도 분석**")
fig2, ax2 = plt.subplots()
ax2.bar(df["지역"], df["발생 빈도"], color='orange')
plt.title("지역별 발생 빈도")
plt.xlabel("지역")
plt.ylabel("발생 빈도")
st.pyplot(fig2)

# 데이터 유효성과 분석 방법 설명
st.subheader("📖 교사의 데이터 분석 설명")

# 힌트 버튼으로 유효성 설명 추가
with st.expander("🔍 데이터의 유효성과 분석 방법을 확인해 보세요!"):
    st.info("""
    - **데이터 유효성**:  
      수집된 데이터의 출처와 신뢰성을 검토하고 누락된 값이나 오류를 확인합니다.  
      (예: 기상청 데이터 활용, 이상치 제거)

    - **분석 방법**:  
      - **히스토그램**: 지진 규모를 시각화하여 경향을 파악합니다.  
      - **막대 그래프**: 지역별 발생 빈도를 비교하여 위험 지역을 확인합니다.  

    - **결론 도출**:  
      데이터를 통해 지진 발생의 **주요 지역**과 **빈도**, **규모**의 경향을 이해할 수 있습니다.  
    """)

# 마무리 질문
st.subheader("❓ 분석 결과를 토대로 어떤 결론을 도출할 수 있을까요?")
st.write("학생 여러분이 분석한 내용을 정리해 보세요!")
user_input = st.text_area("여기에 생각을 적어보세요.", placeholder="결론을 작성해 보세요.")

if st.button("🚀 제출"):
    if user_input:
        st.success("✅ 잘 작성했습니다! 결론이 전송되었습니다.")
    else:
        st.warning("⚠️ 내용을 입력해 주세요!")

    
st.subheader("여러분들이 얻어낸 결론을 토대로 유의미한 데이터 분석을 위해 조별로 다시 데이터를 수집하거나, 조별로 수집한 데이터를 검토해 봅시다!")