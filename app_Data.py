import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_Data_app():
    df=pd.read_csv('data/india_vaccine.csv')

    df.rename(columns = {'Unnamed: 0':'dex'},inplace=True)

    df.set_index('dex',inplace=True)

    df = df.loc[:,['Date','Vaccine_male','Vaccine_female','Vaccine_covishield','Vaccine_covaxin','Vaccine_aefi','aefiPercentage']]

 
    st.subheader('데이터 요약')
    st.text('백신 접종과 부작용에 대한 데이터 요약표입니다.')
    st.text('각 컬럼은 Vaccine_male = 남자 백신 접종자수, Vaccine_female = 여자 백신 접종자수')
    st.text('Vaccine_covishield = 아스트라제네카 접종자수, Vaccine_covaxin = 인도산 백신 접종자수')
    st.text('Vaccine_aefi = 백신 부작용자수, aefiPercentage = 부작용 비율을 나타냅니다.')
    st.text('                                  ')
    st.text('각각 count = 총갯수,mean= 평균,std= 표준편차, min= 최소값, 25%= 4분위수의 25%값,')
    st.text('50%= 4분위수의 50%값, 75% = 4분위수의 75%값, max= 최대값을 나타냅니다.')
    st.dataframe(df.describe())

     # 컬럼을 선택할수 있게 한다. 하나의 컬럼을 선택하면,
    # 해당 컬럼의 최대값 최소값 데이터를 화면에 보여준다.

    st.subheader('최대/최소 데이터 확인하기')
    st.text('백신 접종 데이터에서 종합적인 최대최소 데이터와 부작용 비율 최대최소 데이터입니다.')
    status =st.radio('설정을 선택하세요',['종합','부작용 비율'])
    if status == '종합' :
        df_max1=df.loc[df['Vaccine_male']==df['Vaccine_male'].max(),]
        df_min1=df.loc[df['Vaccine_male']==df['Vaccine_male'].min(),]

        st.text('종합 최대')
        st.dataframe(df_max1)
        st.text('종합 최소')
        st.dataframe(df_min1)
    
    elif status == '부작용 비율':
        df_max2=df.loc[df['aefiPercentage']==df['aefiPercentage'].max(),]
        df_min2=df.loc[df['aefiPercentage']==df['aefiPercentage'].min(),]

        st.text('부작용 비율 최대')
        st.dataframe(df_max2)
        st.text('부작용 비율 최소')
        st.dataframe(df_min2)











