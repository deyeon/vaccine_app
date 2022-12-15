import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app():
    df=pd.read_csv('data/india_vaccine.csv')

    df.rename(columns = {'Unnamed: 0':'dex'},inplace=True)

    df.set_index('dex',inplace=True)

    df = df.loc[:,['Date','Vaccine_male','Vaccine_female','Vaccine_covishield','Vaccine_covaxin','Vaccine_aefi','aefiPercentage']]

    st.subheader('통계 데이터 확인')
    st.dataframe(df.head(3))
    
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

     # 컬럼을 선택할수 있게 한다. 하나의 컬럼을 선택하면,
    # 해당 컬럼의 최대값 최소값 데이터를 화면에 보여준다.

    st.subheader('최대/최소 데이터 확인하기')

    column_list = df.columns[1:]

    selected_column=st.selectbox('컬럼을 선택하세요',column_list)

    df_max=df.loc[df[selected_column]==df[selected_column].max(),]
    df_min=df.loc[df[selected_column]==df[selected_column].min(),]

    st.text('최대 데이터')
    st.dataframe(df_max)
    st.text('최소 데이터')
    st.dataframe(df_min)

    st.subheader('컬럼 별 히스토그램')

    histogram_coulmn=st.selectbox('히스토그램 확인 할 컬럼을 선택하세요',column_list)

    #plotly 라이브러리
    import plotly.express as px
    fig=px.histogram(df, x=histogram_coulmn ,color_discrete_sequence=['seagreen'])
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig)

    st.subheader('상관 관계 분석')

    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)
    if len(selected_list) >= 2:
        fig1=px.scatter_matrix(df,dimensions=selected_list,color='Date')
        fig1.update_layout(
        title='Data set',
        width=1500,
        height=1000,
        )
        st.plotly_chart(fig1)

        df_corr=df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
        vmin = -1,vmax=1,linewidths=0.5)
        st.pyplot(fig2)








