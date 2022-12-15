import streamlit as st
import numpy as np
import pandas as pd
import joblib

def run_ml_app():

    man=st.number_input("남자",67000000,78000000)
    women=st.number_input("여자",61000000,69000000)
    covishield=st.number_input("백신1 아스트라 제네카",142000000,168000000)
    covaxin=st.number_input("백신2 covaxin 인도산 백신 ",14800000,20000000)


    new_data=np.array([man,women,covishield,covaxin])
    
    new_data=new_data.reshape(1,4)
    
    regressor = joblib.load('regressor.pkl')

    y_pred2=regressor.predict(new_data)

    y_pred2=round(y_pred2[0])
    
    if y_pred2>1000:
        st.info('예측한 부작용자 수는{}명 입니다.'.format(y_pred2))

    else:
        st.info('입력한 데이터로는 예측하기 어렵습니다.')