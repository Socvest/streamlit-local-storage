# Streamlit local storage

This repo is to help streamlt users manage data in a browser's local storage.

`pip install streamlit-local-storage`


```
from streamlit_local_storage import LocalStorage
localS = LocalStorage()
```

### store an array to local storage

```
localStorageArray = [
    {"key":"Games", "toStore":[{"name":"Basically does this work"}]},
    {"key":"Winners", "toStore":[{"name":"Basically does this work Though"}]}
]
localS.setList(localStorageArray)
```

### store individual items from local storage
```
itemKey = "camera"
itemValue = "Tarah"
localS.set(itemKey, itemValue)
```

### get list of items from local storage

```
data_ = [{"key":"camera"}, {"key":"JamesLook"}]
saved_ = localS.getList(data_)
st.write(saved_)

```

### get all items saved on local storage

```
saved_individual = localS.getAll()
st.write(saved_individual)

```

### delete item and item list from local storage

```
saved_individual = localS.deleteList([{"key": "ThomasKing"}, {"key":"Somethingelse"}])
localS.deleteItem('Tony')

```

### delete all
```
localS.deleteAll()

```

### get all

```
localS.getAll()

```

Remember to refresh browser if it does not pop up instantly. 
