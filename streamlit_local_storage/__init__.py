import os
import ast
import time
from dataclasses import dataclass 
from typing import Literal, Optional, Union, Any, Dict
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
    storedItems: Dict[str, Any]

    def __init__(self, key:str="storage_init"):

        """
        Initialise component

        Args:
            key: unique identified of component when mounted. 
            pause: time to pause after mounting component. Needed sometimes to allow all data to be loaded from browser.
        """

        self.storedKey = key
        if key not in st.session_state:
            self.storedItems:Dict[str, Any] = _st_local_storage(method="getAll", key=key, default={}) 
            while st.session_state[key] is None:
                time.sleep(0.1) 
        else:
            self.storedItems:Dict[str, Any] = st.session_state[key]

            st.session_state[key] = self.storedItems
    
    def getItem(self, itemKey: str):
        """
        Get individual items stored in local storage.

        Args:
            itemKey: name of item to get from local storage
        
        Returns:
            Singular item stored in local storage via the itemKey
        """
        if itemKey not in self.storedItems:
            return
         
        return self.storedItems.get(itemKey)
    
    def refreshItems(self):
        """
            Get all items stored in local storage. Re-store items from browser local storage to session state
        """
        self.storedItems: Dict[str, Any] = _st_local_storage(method="getAll", key=self.storedKey, default={}) 
        while st.session_state[self.storedKey] is None:
            time.sleep(0.1) 
    
    def getAll(self):
        """
        Get all items saved on local storage.

        Returns:
            all items stored in local storage in browser
        """
        return self.storedItems

    def setItem(self, itemKey:str=None, itemValue:Union[str, int, float, bool]=None, key:str="set"):
        """
        Set individual items to local storage with a given name (itemKey) and value (itemValue)

        Args:
            itemKey: Name of the item to set
            itemValue: The value to save. Can be string, int, float, bool, dict, json but will be stored as a string
            key: unique identifier for component when setting item

        Returns:
            nothing
        """

        if (itemKey is None or itemKey == "") or (itemValue is None or itemValue == ""):
            return
        
        _st_local_storage(method="setItem", itemKey=itemKey, itemValue=itemValue, key=key)

        self.storedItems[itemKey] = itemValue
    
    def deleteItem(self, itemKey:str, key:str="deleteItem"): 
        """
        Delete individual item from local storage

        Args:
            itemKey: item key to delete from local storage
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.

        Returns:
            nothing
        """

        if itemKey is None or itemKey == "":
            return
        
        _st_local_storage(method="deleteItem", itemKey=itemKey, key=key) 

        self.storedItems.pop(itemKey) 
    
    def eraseItem(self, itemKey:str, key:str="eraseItem", default=None):
        """
        Erase item from local storage. deleteItem does not remove it from storage, merely changes its default value. This will do so.

        Args:
            itemKey: item key to remove from local storage storage 
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.
        """
        if itemKey is None or itemKey == "":
            return
        
        _st_local_storage(method="eraseItem", itemKey=itemKey, key=key, default=default) 
        
        
    def deleteAll(self, key:str="deleteAll"):
        """
        Delete all items you saved on local storage

        Args:
            key: unique identifier for the function/method in case you wish to execute it again somewhere else in the app.
        
        Returns:
            nothing
        """

        _st_local_storage(method="deleteAll", key=key) 

        self.storedItems.clear() 




            
    