import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _st_local_storage = components.declare_component(

        "st_local_storage",

        url="http://localhost:3001",
    )
else:

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_local_storage = components.declare_component("st_local_storage", path=build_dir)


class LocalStorage:

    def __init__(self):
        self.localStorageManager = _st_local_storage

    def setList(self, items:list = None, key:str="setList"):
        if items is None or items == "" or len(items) == 0:
            return
        
        try:
            self.localStorageManager(method="setList", items=items, key=key)
            return True
        except:
            return False
    
    def set(self, itemKey:str=None, itemValue:any=None, key:str="set"):

        if (itemKey is None or itemKey == "") or (itemValue is None or itemValue == ""):
            return
        
        try:
            self.localStorageManager(method="set", itemKey=itemKey, itemValue=itemValue, key=key)
            return True
        except:
            return False
    
    def getList(self, items:list=None, key:str="getList"):

        if items is None or items == "" or len(items) == 0:
            return
        
        try:
            saved_list = self.localStorageManager(method="getList", items=items, key=key) 
            return saved_list
        except:
            return False
    
    def get(self, itemKey:any=None, key:str="get"):

        if itemKey is None or itemKey == "":
            return
        
        try:
            saved_key = self.localStorageManager(method="get", itemKey=itemKey, key=key) 
            return saved_key
        except:
            return False
    
    def deleteList(self, items:list=None, key:str="deleteList"): 

        if items is None or items == "" or len(items) == 0:
            return
        
        try:
            saved_key = self.localStorageManager(method="deleteList", items=items, key=key) 
            return saved_key
        except:
            return False
        
    def deleteItem(self, itemKey:any, key:str="deleteItem"): 

        if itemKey is None or itemKey == "":
            return
        
        try:
            saved_key = self.localStorageManager(method="deleteItem", itemKey=itemKey, key=key) 
            return saved_key
        except:
            return False
    
    def deleteAll(self, key:str="deleteAll"):

        try:
            saved_key = self.localStorageManager(method="deleteAll", key=key) 
            return saved_key
        except:
            return False
        
    def getAll(self, key:str="getAll"):

        try:
            saved_key = self.localStorageManager(method="getAll", key=key) 
            return saved_key
        except:
            return False
