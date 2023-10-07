import os
from dataclasses import dataclass
from typing import Literal, Optional, Union
import streamlit as st
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
    """
    Component to help manager local storage for streamlit apps
    """

    def __init__(self):
        self.localStorageManager = _st_local_storage
            
    def setItem(self, itemKey:str=None, itemValue:Union[str, int, float, bool]=None, key:str="set"):
        """
        Set individual items to local storage with a given name (itemKey) and value (itemValue)

        Args:
            itemKey: Name of the item to set
            itemValue: The value to save. Can be string, int, float, bool, dict, json but will be stored as a string
        """

        if (itemKey is None or itemKey == "") or (itemValue is None or itemValue == ""):
            return
        
        try:
            self.localStorageManager(method="setItem", itemKey=itemKey, itemValue=itemValue, key=key)
            return True
        except:
            return False   
        
    def deleteItem(self, itemKey:str, key:str="deleteItem"): 
        """
        Delete individual item from local storage

        Args:
            itemKey: item key to delete from local storage
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.
        """

        if itemKey is None or itemKey == "":
            return
        
        self.localStorageManager(method="deleteItem", itemKey=itemKey, key=key) 
        
        return True
    
    def getItem(self, itemKey:str=None, key:str="get"):
        """
        Get individual items stored in local storage.

        Args:
            itemKey: name of item to get from local storage
        """

        if itemKey is None or itemKey == "":
            return
        
        saved_key = self.localStorageManager(method="getItem", itemKey=itemKey, key=key) 
        return saved_key
        
    def getAll(self, key:str="getAll"):
        """
        Get all items saved on local storage.

        Args:
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.
        """

        saved_key = self.localStorageManager(method="getAll", key=key)
        return saved_key
        
    def deleteAll(self, key:str="deleteAll"):
        """
        Delete all items you saved on local storage

        Args:
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.
        """

        self.localStorageManager(method="deleteAll", key=key) 

       
        
    
   
    
    