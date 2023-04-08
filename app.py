import streamlit as st
# from img_classification import teachable_machine_classification
# from PIL import Image, ImageOps
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import requests

# authentification
with open('./bla.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    page = st.sidebar.selectbox("探索", ("历史上","小数学事实","随机事实","年事实"))


    if page == "历史上":
        st.title("历史上")
        mm = st.slider("月",1,12,1,1)
        dd = st.slider("日",1,31,1,1)
        # yyyy = st.number_input("日",0,2050,2023,1)
        url = "https://numbersapi.p.rapidapi.com/"+str(mm)+"/"+str(dd)+"/date"
        querystring = {"fragment":"true","json":"true"}

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        st.text(response.text)

    elif page == "小数学事实":
        st.title("小数学事实")
        url = "https://numbersapi.p.rapidapi.com/1729/math"

        querystring = {"fragment":"true","json":"true"}

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        st.text(response.text)
        # print(response.text)
    elif page == "随机事实":
        st.title("随机事实")
        url = "https://numbersapi.p.rapidapi.com/random/trivia"
        mmm = st.slider("最小",1,1000,1,1)
        ddd = st.slider("最大",1,1000,1,1)

        querystring = {"min":str(mmm),"max":str(ddd),"fragment":"true","json":"true"}

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        st.text(response.text)
        print(response.text)


    elif page == "小数学琐事事实":
        mmmm = st.slider("数",1,1000,1,1)
        url = "https://numbersapi.p.rapidapi.com/"+str(mmmm)+"/trivia"
        querystring = {"fragment":"true","notfound":"floor","json":"true"}

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        st.text(response.text)
        print(response.text)
    elif page == "年事实":
        mmmmmm = st.slider("年",1,2050,1,1)
        url = "https://numbersapi.p.rapidapi.com/"+str(mmmmmm)+"/year"

        querystring = {"fragment":"true","json":"true"}

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        st.text(response.text)
        print(response.text)




elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')








