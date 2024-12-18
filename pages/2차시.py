import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

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

st.title("📈 2차시: 데이터 시각화 및 분석")
st.write("**학습 목표**:")
st.markdown("""
- 지진 데이터를 시각화하고 분석합니다.
- 히스토그램과 산점도를 작성하여 데이터 특성을 이해합니다.
- 분석 결과를 바탕으로 지진 경향을 해석합니다.
""")
st.success("2차시에서는 데이터를 시각화하여 분석 결과를 해석하는 방법을 배웁니다.")


# 타이틀
st.title("📊 **데이터 시각화의 필요성**")
st.write("### 이전 시간 데이터를 바탕으로 시각화의 필요성을 생각해 봅시다!")

# 한글 폰트 설정 (Windows 기준)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 '맑은 고딕'
matplotlib.rcParams['axes.unicode_minus'] = False    # 마이너스 기호 깨짐 방지

# 이전 시간 데이터 요약 (샘플 데이터 사용)
data = {
    "지역": ["포항", "경주", "서울", "대구", "부산"],
    "규모": [5.5, 5.8, 3.2, 4.1, 3.8],
    "발생 빈도": [3, 4, 2, 2, 3]
}
df = pd.DataFrame(data)

st.write("#### 📋 이전 시간 데이터 요약")
st.dataframe(df)  # st.table 대신 st.dataframe 사용

# 시각화 필요성 질문
st.subheader("❓ 시각화는 왜 필요할까요?")
st.write("""
- 데이터를 **표**로만 보면 어떤 점이 불편했나요?  
- **어느 지역이 가장 위험한지** 바로 파악할 수 있나요?  
- **데이터의 경향성**이 보이나요?  
""")

# 생각을 작성할 수 있는 텍스트 영역
st.subheader("✍️ 나의 생각")
user_input = st.text_area("데이터 시각화의 중요성에 대해서 적어보세요.", placeholder="여기에 생각을 적어보세요.")

# 전송 버튼 기능 추가
if st.button("🚀 전송"):
    if user_input:  # 내용이 입력되었는지 확인
        st.success("✅ 입력이 전송되었습니다! 잘 적어주셨습니다.")
    else:
        st.warning("⚠️ 내용을 입력해 주세요!")


st.write("이제 데이터를 그래프로 시각화해서 이해해 봅시다!")

# 시각화 예시 1: 막대그래프 - 지역별 지진 규모 비교
st.subheader("📊 **지역별 지진 규모 비교**")

fig, ax = plt.subplots()
ax.bar(df["지역"], df["규모"], color="skyblue")
ax.set_title("지역별 지진 규모")
ax.set_ylabel("규모")

st.pyplot(fig)

# 시각화 예시 2: 산점도 - 지진 발생 위치 예시 (위도, 경도 가상 데이터)
st.subheader("📍 **지진 발생 위치 시각화**")

# 샘플 데이터 생성
location_data = {
    "위도": [36.02, 35.84, 37.56, 35.87, 35.18],
    "경도": [129.36, 129.20, 126.97, 128.60, 129.07],
    "규모": [5.5, 5.8, 3.2, 4.1, 3.8],
    "지역": ["포항", "경주", "서울", "대구", "부산"]
}
loc_df = pd.DataFrame(location_data)

fig, ax = plt.subplots()
scatter = ax.scatter(loc_df["경도"], loc_df["위도"], s=loc_df["규모"]*50, c=loc_df["규모"], cmap="cool", alpha=0.7)
ax.set_title("지진 발생 위치와 규모")
ax.set_xlabel("경도")
ax.set_ylabel("위도")

plt.colorbar(scatter, label="규모")
st.pyplot(fig)

# 마무리 질문
st.subheader("💬 **생각해 봅시다**")
st.write("""
데이터를 시각화하니 어떤 점이 더 명확해졌나요?  
시각화를 통해 **어떤 결론**을 도출할 수 있을까요?  
""")

# 생각을 작성할 수 있는 텍스트 영역
st.subheader("✍️ 나의 생각")
user_input = st.text_area("시각화를 통해 명확해진 부분을 찾아보세요.", placeholder="여기에 생각을 적어보세요.")

if st.button("🚀 전송", key="submit_button_1"):
    if user_input:  # 내용이 입력되었는지 확인
        st.success("✅ 입력이 전송되었습니다! 잘 적어주셨습니다.")
    else:
        st.warning("⚠️ 내용을 입력해 주세요!")


st.subheader("이제 여러분이 얻은 데이터를 직접 시각화하여 유의미한 데이터 분석을 얻어봅시다!")
st.write("**Google Sheets 데이터**를 복사해서 아래에 붙여넣고 시각화해 보세요!")

# 한글 폰트 설정 (Windows 기준)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'
matplotlib.rcParams['axes.unicode_minus'] = False    # 마이너스 기호 깨짐 방지

# 데이터 입력
st.subheader("📋 데이터를 붙여넣어 주세요")
data_input = st.text_area(
    "데이터 입력 (탭으로 구분된 데이터, 첫 줄은 헤더)",
    placeholder="예시:\n지역\t규모\t위도\t경도\n포항\t5.5\t36.02\t129.36\n경주\t5.8\t35.84\t129.20\n서울\t3.2\t37.56\t126.97\n대구\t4.1\t35.87\t128.60\n부산\t3.8\t35.18\t129.07"
)

# 데이터 불러오기 버튼
if st.button("✅ 데이터 불러오기"):
    if data_input:
        try:
            # 데이터를 DataFrame으로 변환
            df = pd.read_csv(pd.io.common.StringIO(data_input), sep="\t")
            st.session_state["df"] = df  # 세션 상태에 데이터 저장
            st.success("✅ 데이터가 성공적으로 불러와졌습니다!")
        except Exception as e:
            st.error(f"❌ 데이터 형식이 올바르지 않습니다: {e}")
    else:
        st.warning("⚠️ 데이터를 입력해 주세요!")
            
 # 세션 상태에서 데이터 가져오기
df = st.session_state.get("df", None)

if df is not None:
    st.subheader("📋 입력된 데이터")
    st.dataframe(df)
            
           # 히스토그램 설정
    st.subheader("📊 히스토그램")
    selected_hist_col = st.selectbox("히스토그램에 사용할 열을 선택하세요:", df.columns, key="hist_col")
    if st.button("📊 히스토그램 적용", key="update_hist"):
        st.session_state["selected_hist_col"] = selected_hist_col

    # 히스토그램 그리기
    if "selected_hist_col" in st.session_state:
        fig, ax = plt.subplots()
        ax.hist(df[st.session_state["selected_hist_col"]], bins=10, color='skyblue', edgecolor='black')
        ax.set_title(f"{st.session_state['selected_hist_col']} 히스토그램")
        ax.set_xlabel(st.session_state["selected_hist_col"])
        ax.set_ylabel("빈도")
        st.pyplot(fig)

    # 산점도 설정
    st.subheader("📍 산점도")
    x_axis = st.selectbox("X축에 사용할 열을 선택하세요:", df.columns, key="x_axis_select")
    y_axis = st.selectbox("Y축에 사용할 열을 선택하세요:", df.columns, key="y_axis_select")
    if st.button("📍 산점도 적용", key="update_scatter"):
        st.session_state["x_axis"] = x_axis
        st.session_state["y_axis"] = y_axis

    # 산점도 그리기
    if "x_axis" in st.session_state and "y_axis" in st.session_state:
        fig, ax = plt.subplots()
        ax.scatter(df[st.session_state["x_axis"]], df[st.session_state["y_axis"]], color='orange', alpha=0.7)
        ax.set_title(f"{st.session_state['x_axis']} vs {st.session_state['y_axis']} 산점도")
        ax.set_xlabel(st.session_state["x_axis"])
        ax.set_ylabel(st.session_state["y_axis"])
        st.pyplot(fig)

      # 안내 메시지
st.info("**팁**: Google Sheets에서 데이터를 복사한 뒤 바로 붙여넣으면 됩니다! 첫 줄은 열 제목으로 사용됩니다.")

# 그래프 해석 및 협의
st.subheader("📋 그래프 해석 및 협의")
st.write("작성된 그래프를 해석하고, 각 지역의 지진 특성을 협의해 보세요.")

# 협의 섹션
interpretation = st.text_area("그래프 해석을 적어보세요.", placeholder="예: 경주의 지진 규모가 가장 높고, 서울은 가장 낮습니다.")
if st.button("✅ 해석 제출"):
    if interpretation:
        st.success("✅ 해석이 저장되었습니다!")
    else:
        st.warning("⚠️ 내용을 입력해 주세요.")

# 시각화 자료 분석
st.subheader("📊 시각화 자료 분석")
st.write("""
시각화 자료를 바탕으로 다음 질문에 대해 생각해 보세요:
- **어떤 지역이 가장 위험합니까?**
- **지진의 규모가 지역별로 어떤 경향이 있나요?**
- **데이터를 통해 알 수 있는 추가적인 특징은 무엇인가요?**
""")

# 발표 준비 섹션
st.subheader("📢 발표 준비")
st.text_area("발표 자료의 주요 내용을 작성하세요.", placeholder="발표 자료 요약 내용을 적어보세요.")