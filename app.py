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
    page = st.sidebar.selectbox("探索", ("QUOTE","历史上的今天","历史上","小数学事实","随机事实","年事实"))

    if page == "QUOTE":
        st.title("名人名言")
        url = "https://quotel-quotes.p.rapidapi.com/search/quotes"
        pagen = st.slider("页",1,10000,1,1)
        numperpage = st.slider("每页结果数",1,30,1,1)
        prompt = st.text_input("提示", value="")
        if st.button("生成"):
            with st.spinner("请稍候..."):

                payload = {
                    "pageSize": numperpage,
                    "page": pagen,
                    "searchString": prompt
                }
                headers = {
                    "content-type": "application/json",
                    "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
                    "X-RapidAPI-Host": "quotel-quotes.p.rapidapi.com"
                }

                response = requests.request("POST", url, json=payload, headers=headers)
                ini_string_s = response.json()
                for dictionary in ini_string_s:
                    try:
                        st.text(str(dictionary["quoteId"]))
                        # for key in dictionary:
                            # print(dictionary[key])
                            # st.text(str(key)+": "+str(dictionary[key]))

                        st.text("引用: "+dictionary["quote"])
                        st.text("国籍: "+dictionary["nationality"])
                        st.text("职业: "+dictionary["profession"])
                        st.text("出生: "+dictionary["born"])
                        st.text("逝世: "+dictionary["died"])
                        st.text("名字: "+dictionary["name"])
                        st.text(" ")
                    except:
                        pass


                # print(response.text)

    elif page == "历史上的今天":
        st.title("历史上的今天")
        url = "https://today-in-history.p.rapidapi.com/thisday"

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "today-in-history.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        st.text(response.text)

    elif page == "历史上":
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








