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

 
    st.subheader('데이터 요약')
    st.dataframe(df.describe())

     # 컬럼을 선택할수 있게 한다. 하나의 컬럼을 선택하면,
    # 해당 컬럼의 최대값 최소값 데이터를 화면에 보여준다.

    st.subheader('최대/최소 데이터 확인하기')

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


    st.subheader('컬럼 별 히스토그램')

    column_list = df.columns[1:]

    histogram_coulmn=st.selectbox('히스토그램 확인 할 컬럼을 선택하세요',column_list)

    #plotly 라이브러리
    import plotly.express as px
    fig=px.histogram(df, x=histogram_coulmn ,color_discrete_sequence=['seagreen'])
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig)

    df2=df[['Vaccine_male','Vaccine_female','Vaccine_covishield','Vaccine_covaxin','Vaccine_aefi']].sum()
    st.subheader('파이 차트')
    fig1 = px.pie(df2,names=['남자가 백신맞은 비율','여자가 백신맞은 비율','아스트라제네카백신을 맞은 비율','covaxin백신 맞은 비율','백신 부작용 비율'],values=df2.values,title='파이차트')
    st.plotly_chart(fig1)



    st.subheader('상관 관계 분석')

    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)
    if len(selected_list) >= 2:
        fig2=px.scatter_matrix(df,dimensions=selected_list,color='Date')
        fig2.update_layout(
        title='Data set',
        width=1500,
        height=1000,
        )
        st.plotly_chart(fig2)

        df_corr=df[selected_list].corr()

        fig3 = plt.figure()
        sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
        vmin = -1,vmax=1,linewidths=0.5)
        st.pyplot(fig3)








