import streamlit as st
from __init__ import LocalStorage


localStorageArray = [
    {"key":"Hiya", "instruction":"get", "toStore": [{"name":"James"}]},
    {"key":"Jones", "instruction":"get", "toStore": [{"name":"Niger"}]},
    {"key":"Micah", "instruction":"get", "toStore": [{"name":"Thomas"}]},
    {"key":"ChickenTikka", "instruction":"get", "toStore": [{"name":"Thomas"}]},
    {"key":"Mikkassah", "instruction":"get", "toStore": [{"name":"Thomas"}]}
   ]


localS = LocalStorage() 

localStorageArray_dummy = [
    {"key":"Games", "toStore":[{"name":"Basically does this work"}]},
    {"key":"Winners", "toStore":[{"name":"Basically does this work THough"}]}
]

localS.setList(localStorageArray)

itemKey = "Bane"
itemValue = "Tarah"
localS.set(itemKey, itemValue)

data_ = [{"key":"camera"}]

saved_ = localS.getList(data_)
st.write(saved_)

# saved_individual = localS.getAll()
# st.write(saved_individual)

saved_individual = localS.deleteList([{"key": "ThomasKing"}])

localS.deleteItem('Tony')


# localS.deleteAll()
