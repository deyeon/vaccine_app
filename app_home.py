import streamlit as st

def run_home_app():
    st.markdown('인도의 코로나 백신 부작용 데이터 분석 입니다. 코로나 백신에 관한 부작용이 얼마나 일어났는지 데이터를 분석하고 알려줍니다.')
    st.markdown('백신 접종자의 종합적인 최대/최소 데이터를 알수 있으며, 각 컬럼별 기준으로 히스토그램과 파이차트를 확인할수 있습니다.')
    st.markdown('마지막으로 접종자수를 입력하면 인공지능으로 부작용수를 예측하여 보여줄수 있습니다.')
    st.image('https://cdn.pixabay.com/photo/2020/03/22/13/33/man-4957154_960_720.jpg')