import streamlit as st
import numpy as np
import pandas as pd
import joblib

def run_ml_app():

    st.subheader('백신 접종자 수를 입력하면 백신 부작용자 수를 예측할수 있습니다.')

    man=st.number_input("남자 백신접종자 수",60000000,78000000)
    women=st.number_input("여자 백신접종자 수",60000000,69000000)
    covishield=st.number_input("백신1 아스트라 제네카 백신접종자 수",14000000,168000000)
    covaxin=st.number_input("백신2 covaxin 인도산 백신접종자 수 ",14000000,20000000)


    new_data=np.array([man,women,covishield,covaxin])
    
    new_data=new_data.reshape(1,4)
    
    regressor = joblib.load('regressor.pkl')

    y_pred2=regressor.predict(new_data)

    y_pred2=round(y_pred2[0])
    
    if y_pred2>0:
        st.info('예측한 부작용자 수는{}명 입니다.'.format(y_pred2))

    else:
        st.warning('입력한 데이터로는 예측하기 어렵습니다.')