import streamlit as st

# 페이지 설정
st.set_page_config(page_title="세상을 지키는 데이터", page_icon="🌍")\

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

# Streamlit 페이지 링크 설정\
st.sidebar.page_link("pages/1차시.py", label="1차시: 데이터 탐색 및 정리")
st.sidebar.page_link("pages/2차시.py", label="2차시: 데이터 시각화 및 분석")
st.sidebar.page_link("pages/3차시.py", label="3차시: 대책 설계 및 발표")

st.title("🛡️ 3차시: 대책 설계 및 발표")
st.write("**학습 목표**:")
st.markdown("""
- 분석된 데이터를 바탕으로 지진 위험 지역을 선정합니다.
- 안전한 지역 설계 및 대피소, 병원 배치를 계획합니다.
- 팀별 발표 자료를 제작하고 공유합니다.
""")
st.warning("3차시에서는 데이터를 기반으로 실제 대책을 설계하고 발표하는 활동을 진행합니다.")

st.write("""
### **역할 부여**  
여러분은 이제 **'지진학자'**가 되어 데이터를 바탕으로 **안전한 지역**을 주제로 시민들에게 강의를 해야합니다.  
- 데이터 분석 결과를 활용해 지진으로부터 안전한 지역과 대피 등에 대해 강의해 주세요. 
- 주변 인프라와 생활권을 고려해 지진으로부터의 대피나 동선 등에 대한 강의도 좋습니다.
""")

# 역할 강조 카드
st.markdown("""
<div style="background-color:#E6F7FF; padding:15px; border-radius:10px; box-shadow:0px 2px 4px rgba(0,0,0,0.1);">
    <h3 style="text-align:center; color:#0073E6;">👷‍♂️ **여러분은 '지진학자'입니다!** 👷‍♀️</h3>
    <p style="text-align:center; color:#333333;">
        데이터를 분석하고 창의적인 아이디어를 통해 지진으로부터 안전한 도시를 설계해 봅시다.  
        팀원과 협력하여 해결책을 만들어 보세요!
    </p>
</div>
""", unsafe_allow_html=True)

# 활동 설명
st.write("---")
st.subheader("📋 **활동 목표**")
st.markdown("""
1. **데이터 분석**:  
   - 지진 규모, 발생 빈도, 위치 데이터를 기반으로 위험 지역을 파악합니다.  

2. **안전한 지역 설계**:  
   - 위험 요소를 고려하여 안전한 지역을 설계하고 필요한 인프라를 제안합니다.  

3. **발표 자료 준비**:  
   - 설계 결과를 정리하고, 시각적 자료를 포함해 발표 준비를 합니다.
""")

# 생각 작성 섹션
st.subheader("✍️ **아이디어 정리**")
st.write("아래에 안전한 지역 설계를 위한 아이디어를 작성해 보세요.")

idea_input = st.text_area("안전한 지역 설계를 위한 아이디어를 적어보세요.", placeholder="예: 위험 지역을 피하고, 병원과 학교를 중심으로 안전 구역을 설정합니다.")

if st.button("🚀 아이디어 제출"):
    if idea_input:
        st.success("✅ 아이디어가 성공적으로 제출되었습니다! 팀원들과 협력해 구체화해 봅시다.")
    else:
        st.warning("⚠️ 아이디어를 입력해 주세요!")

# 팀 협의 및 발표 준비 섹션
st.subheader("💬 **팀 협의 및 발표 준비**")
st.write("""
- 팀원과 협의하여 설계 아이디어를 발전시켜 보세요.  
- 결과물을 정리하고 발표 자료를 만들어 봅시다.
""")

st.text_area("팀 협의 내용 작성", placeholder="팀원들과 논의한 내용을 정리해 보세요.")

if st.button("📢 발표 준비 완료"):
    st.success("🎉 발표 준비가 완료되었습니다! 최종 발표를 기대합니다.")

     # 발표 후 동료 피드백 요약
st.subheader("🗣️ **발표 후 동료 피드백 요약**")
feedback_summary = st.text_area(
    "동료들로부터 받은 피드백을 요약해 보세요.",
    placeholder="예: 설계 아이디어는 좋았지만 데이터 분석이 부족하다는 피드백이 있었습니다."
)

# 동료 피드백 요약 버튼
if st.button("✅ 피드백 제출"):
    st.success("🎉 피드백을 체줄합니다.")
    st.balloons()


# 개선점 및 성찰 작성
st.subheader("💡 **개선할 점과 성찰**")
improvement_reflection = st.text_area(
    "발표를 마친 후 개선하면 좋을 점, 성찰 및 느낀 점을 작성해 보세요.",
    placeholder="예: 데이터 시각화를 더 명확히 하고 분석 결과를 구체적으로 설명할 필요가 있었습니다."
)

# 최종 제출 버튼
if st.button("✅ 최종 제출"):
    st.success("🎉 최종 내용이 저장되었습니다! 오늘의 학습을 마무리했습니다.")
    st.balloons()
