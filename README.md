# vaccine_app
# 설명
- 인도의 백신 접종자수와 백신 접종 부작용에 관한 데이터를 분석한 웹대시보드입니다.
- 백신 접종자의 종합적인 최대/최소 데이터를 알수 있으며, 각 컬럼별 기준으로 히스토그램과 파이차트를 확인할수 있습니다.
- 마지막으로 접종자수를 입력하면 인공지능으로 부작용수를 예측하여 보여줄수 있습니다.

# 진행과정

## 1. jupyter notebook에서 진행한 내용

  - csv형식의 데이터를 jupyter notebook으로 불러 작업하였습니다.
  - 데이터를 가공하는 과정에서 꼭 컬럼을 인덱싱으로 부르고 다시 데이터프레임에 저장하여 작업하였습니다.
  - 데이터의 상관분석과 차트를 만들어 진행하였습니다.
  - 인공지능파일을 pkl파일로 로컬에 보내서 작업하였습니다.

## 2. visual studio code 에서 작업

  - visual studio code에서 작업하여 streamlit라이브러리로 웹대시보드를 로컬에서 생성하여 작업하였습니다.
  - 데이터를 설명하는 과정에서 포켓몬 공식사이트에서 이미지를 연결하여 어떤데이터에 어떤 포켓몬이 있는지 알수 있게 하였습니다.
  - 기존 plt차트에서 발전된 plotly차트를 사용하여 사용하는 유저가 차트에 데이터를 마우스만 올리면 볼 수 있게 하였습니다.
  - 상관분석을 통해 각 컬럼간에 데이터는 어떤 상관관계가 있는지 분석해보았고 분석 결과 상관관계가 높지 않아서 인공지능은 사용하지 않았습니다.
  - 마지막으로 인공지능 과정에서 pkl 파일을 활용하여 인공지능을 진행하였습니다.

## 3. github에서 작업 
  
   - visual studio code에서 작업한 내용을 githubdesktop를 이용해 push하여 github레포지토리로 보냈습니다.
   - github 레포지토리를 ec2에 clone하여 서버에서 웹대시보드를 실행하게 하였습니다. 
   - github Actions 기능을 이용하여 visual studio code에서 작업한 내용을 ec2서버에 바로 pull되어 수정사항을
     서버에 실시간으로 보낼수 있게 하였습니다.


## 4. aws ec2에서 작업

  - aws에서 ec2를 생성하여 프리 티어 서버를 생성하였습니다.
  - 터미널 플랫폼 putty로 ec2에 접속하여 원격으로 작업하여 파이썬 환경을 구축하여 streamlit를 서버에서도 실행할 수 있게 하였습니다.
  - Ec2 서버에서 서버 연결이 끊겨도 접속이 가능하게 하였습니다.
  - github 레포지토리에 있던 인공지능파일인 pkl파일을 ec2로 pull하여 서버에서도 인공지능이 실행될 수 있게 하였습니다. 


## 문제해결
  - 웹대시보드에서 차트 부분에 영어로된 컬럼의 기준을 선택할때 한글로 선택할 수 있게 하였습니다. 
  - 인공지능 예측데이터가 음수가 나오는 상황이 발생하여 인공지능 파일의 MSE를 다시 체크하고 음수가
    나오면 값을 예측할수 없다는 안내를 붙혀 예측이 올바르게 될수 있도록 유도하였습니다.


# 스크린샷

![image](https://user-images.githubusercontent.com/120348521/208614180-3b997370-ee9d-4b42-bd7c-b55e5776b2e4.png)

![image](https://user-images.githubusercontent.com/120348521/208614244-05e4851f-6327-484f-a42d-3acb292b7b52.png)

![image](https://user-images.githubusercontent.com/120348521/208614339-57ad7fa2-abb5-446b-96d8-e57c01cbce3c.png)

![image](https://user-images.githubusercontent.com/120348521/208614452-3cb12449-6943-498c-b518-69233ed43561.png)

![image](https://user-images.githubusercontent.com/120348521/208614961-6f264aad-0dbe-475d-a490-9a97ad8c2c0e.png)

![image](https://user-images.githubusercontent.com/120348521/208615121-218671c2-6d1d-4111-b8d7-0e27882ef3c7.png)


$ 데이터 레퍼런스
https://www.kaggle.com/datasets/nitishabharathi/cowin-vaccination-data?resource=download&select=india_vaccine.csv
