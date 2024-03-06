import time 
import streamlit as st
from __init__ import LocalStorage
# from streamlit_local_storage import LocalStorage

st.set_page_config(layout="wide")

if "set_cookie_placement" not in st.session_state:
    st.session_state["set_cookie_placement"] = None

if "get_cookie_placement" not in st.session_state:
    st.session_state["get_cookie_placement"] = None

if "delete_cookie_placement" not in st.session_state:
    st.session_state["delete_cookie_placement"] = None

if "get_storage_list_placement" not in st.session_state:
    st.session_state["get_storage_list_placement"] = None

if "delete_storage_list_placement" not in st.session_state:
    st.session_state["delete_storage_list_placement"] = None

if "getAll_items" not in st.session_state:
    st.session_state["getAll_items"] = False

if "del_list_click" not in st.session_state:
    st.session_state["del_list_click"] = False


localS = LocalStorage() 

cols = st.columns(3)

def setCookie():
    with st.session_state["set_cookie_placement"][0]:
        keyItem = st.session_state["set_storage_item"] 
        keyValue = st.session_state["set_storage_value"] 
        localS.setItem(keyItem, keyValue)


with cols[0].form("set_storage"):
    st.subheader("Set Storage")
    st.text_input("key", key="set_storage_item")
    st.text_input("value", key="set_storage_value")
    st.form_submit_button("set this", on_click=setCookie)
    st.session_state["set_cookie_placement"] = st.columns(1)

# def get_one_item():
#     with st.session_state["get_cookie_placement"][0]:
#         get_item = localS.getItem(st.session_state["get_storage_item"])
#     st.write(get_item)

if "get_storage_item_dummy" not in st.session_state:
    st.session_state["get_storage_item_dummy"] = ""

with cols[1].form("get_storage", clear_on_submit=True):
    st.subheader("Get Storage")
    st.text_input("key", value=st.session_state["get_storage_item_dummy"], key="get_storage_item")
    st.form_submit_button("get this") #, on_click=get_one_item) #, on_click=setCookie)
    st.session_state["get_cookie_placement"] = st.columns(1)

if st.session_state["get_storage_item"] != "":
    get_item = localS.getItem(st.session_state["get_storage_item"]) #, default="James")
    st.write(get_item)


def deleteItem():
    with st.session_state["delete_cookie_placement"][0]:
        localS.deleteItem(st.session_state["delete_storage_item"])

with cols[2].form("delete_item_in_storage"):
    st.subheader("Delete Storage")
    st.text_input("key", key="delete_storage_item")
    st.form_submit_button("delete this", on_click=deleteItem)
    st.session_state["delete_cookie_placement"] = st.columns(1)

def getAllStorage(): 
    st.session_state["getAll_items"] = not st.session_state["getAll_items"]
    # with st.session_state["get_storage_list_placement"][0]:
    #     localS.deleteAll()
    

with cols[1].form("get_all_storage"):
    st.subheader("Get all of storage")
    st.form_submit_button("Get all storage", on_click=getAllStorage)
    st.session_state["get_storage_list_placement"] = st.columns(1)


if st.session_state["getAll_items"]:
    all_storage_ = localS.getAll()
    st.write(all_storage_) 

def deleteFromStorage(): 
    st.session_state["del_list_click"] = not st.session_state["del_list_click"]
    # with st.session_state["get_storage_list_placement"][0]:
    #     localS.deleteAll()
    

with cols[2].form("delete_all_storage"):
    st.subheader("Delete all of storage")
    st.form_submit_button("Delete all storage", on_click=deleteFromStorage)
    st.session_state["delete_storage_list_placement"] = st.columns(1)


if st.session_state["del_list_click"]:
    
    localS.deleteAll()


