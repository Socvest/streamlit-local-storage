import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useEffect } from "react"

const LocalStorageComponent:React.FC<ComponentProps> = (props) => {

  const { args } = props
  
  const saveItems = (items:any) => {
    if (items.length > 0){
      items.map((obj:any) => {
        localStorage.setItem(obj.key, JSON.stringify(obj.toStore));
      })
      return true
    }
  }

  const saveItem = (itemKey:any, itemValue:any) => {
    localStorage.setItem(itemKey, JSON.stringify(itemValue))
    return true
  }

  const getItemsList = (items:any) => {
    if (items.length > 0){

      const toSendToStreamlit:any[] = []
      items.map((obj:any) => {
        const saved:any = localStorage.getItem(obj.key)
        const initial = JSON.parse(saved)
        toSendToStreamlit.push({"key":obj.key, "stored": initial}) 
      })
      return toSendToStreamlit
    }
  }
  

  const getItem_ = (itemKey:any) => {
    const saved:any = localStorage.getItem(itemKey)
    const initial = JSON.parse(saved)
    return initial
  }

  const deleteItemsList = (items:any) => {
    if (items.length > 0 ) {
      items.map((obj:any) => {
        localStorage.removeItem(obj.key)
      })
      return true
    }
  }

  const deleteItem = (itemKey:any) => {
      localStorage.removeItem(itemKey)
      return true
  }

  const deleteAll = () => {
    localStorage.clear();
    return true
}

const getAll = () => {
  const toSendToStreamlit = {...localStorage}
  return toSendToStreamlit
}

  const method = args["method"]

  useEffect(() => { 
    
    let output = null
    const items = args["items"]
    const itemKey = args["itemKey"]
    const itemValue = args["itemValue"]

    switch(method) {
      case "setList":
        output = saveItems(items)  
        break
      case "set":
        output = saveItem(itemKey, itemValue)
        break
      case "getList":
        output = getItemsList(items)
        Streamlit.setComponentValue(output)
        Streamlit.setComponentReady()
        break
      case "get":
        output = getItem_(itemKey)
        Streamlit.setComponentValue(output)
        Streamlit.setComponentReady()
        break
      case "deleteList":
        output = deleteItemsList(items)
        break
      case "deleteItem":
        output = deleteItem(itemKey)
        break
      case "deleteAll":
        output = deleteAll()
        break
      case "getAll":
        output = getAll()
        Streamlit.setComponentValue(output)
        Streamlit.setComponentReady()
        break
    }

    

  }, [method])


  return (      
        <div style={{display:"none"}}></div>
  )
}

export default withStreamlitConnection(LocalStorageComponent)
