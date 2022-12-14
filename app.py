import streamlit as st
from app_home import run_home_app
from app_Data import run_Data_app
from app_Chart import run_chart_app
from app_ml import run_ml_app

def main():

    st.title('백신 부작용 예측앱')

    menu = ['Home','Data','Chart','ML']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'Data':
        run_Data_app()
    elif choice == 'Chart':
        run_chart_app()
    elif choice == 'ML':
        run_ml_app ()

if __name__ == '__main__':
    main()