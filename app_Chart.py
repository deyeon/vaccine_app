import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

def run_chart_app():
    df=pd.read_csv('data/india_vaccine.csv')

    df.rename(columns = {'Unnamed: 0':'dex'},inplace=True)

    df.set_index('dex',inplace=True)

    df = df.loc[:,['Date','Vaccine_male','Vaccine_female','Vaccine_covishield','Vaccine_covaxin','Vaccine_aefi','aefiPercentage']]

    st.subheader('컬럼 별 히스토그램')

    st.text('각 컬럼별 특정 수의 그룹의 분포를 히스토그램으로 나타내었습니다.')
    st.text('                                                       ')
    show_list = ['남자 백신 접종자수','여자 백신 접종자수','아스트라제네카 접종자수','인도산 백신 접종자수','백신 부작용자수','부작용 비율']
 

    histogram_coulmn=st.selectbox('히스토그램 확인 할 컬럼을 선택하세요',show_list)
    
    if histogram_coulmn == '남자 백신 접종자수':
        #plotly 라이브러리
        
        fig=px.histogram(df, x=df['Vaccine_male'],title=show_list[0]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig)
    
    elif histogram_coulmn == '여자 백신 접종자수':
        #plotly 라이브러리
        
        fig1=px.histogram(df, x=df['Vaccine_female'],title=show_list[1]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig1.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig1)

    elif histogram_coulmn == '아스트라제네카 접종자수':
        #plotly 라이브러리
        
        fig2=px.histogram(df, x=df['Vaccine_covishield'],title=show_list[2]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig2.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig2)

    elif histogram_coulmn == '인도산 백신 접종자수':
        #plotly 라이브러리
        
        fig3=px.histogram(df, x=df['Vaccine_covaxin'],title=show_list[3]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig3.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig3)

    elif histogram_coulmn == '백신 부작용자수':
        #plotly 라이브러리
        
        fig4=px.histogram(df, x=df['Vaccine_aefi'],title=show_list[4]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig4.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig4)

    elif histogram_coulmn == '부작용 비율':
        #plotly 라이브러리
        
        fig5=px.histogram(df, x=df['aefiPercentage'],title=show_list[5]+" 히스토그램",color_discrete_sequence=['seagreen'])
        fig5.update_layout(bargap=0.2,plot_bgcolor='#ffffff')
        st.plotly_chart(fig5)

    
    
    

    

    df2=df[['Vaccine_male','Vaccine_female','Vaccine_covishield','Vaccine_covaxin','Vaccine_aefi']].sum()
    st.subheader('파이 차트')
    st.text('백신접종의 비율을 파이차트로 나타내었습니다.')
    fig6 = px.pie(df2,names=['남자가 백신맞은 비율','여자가 백신맞은 비율','아스트라제네카백신을 맞은 비율','covaxin백신 맞은 비율','백신 부작용 비율'],values=df2.values,title='백신 접종 비율')
    st.plotly_chart(fig6)



    st.subheader('상관 관계 분석')
   
    if st.checkbox('컬럼별 정보 보기/숨기기'):
        st.text('각 컬럼은 Vaccine_male = 남자 백신 접종자수, Vaccine_female = 여자 백신 접종자수')
        st.text('Vaccine_covishield = 아스트라제네카 접종자수, Vaccine_covaxin = 인도산 백신 접종자수')
        st.text('Vaccine_aefi = 백신 부작용자수, aefiPercentage = 부작용 비율을 나타냅니다.')
    else :
        st.write("")

    st.text('각 컬럼별간의 상관관계를 확인하고 싶은 컬럼을 선택하여 확인 할 수 있습니다.')

    column_list = df.columns[1:6+1]
    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)
    if len(selected_list) >= 2:
        fig7=px.scatter_matrix(df,dimensions=selected_list,color='Date')
        fig7.update_layout(
        title='Data set',
        width=1500,
        height=1000,
        )
        st.plotly_chart(fig7)

        df_corr=df[selected_list].corr()

        fig8 = plt.figure()
        sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
        vmin = -1,vmax=1,linewidths=0.5)
        st.pyplot(fig8)
