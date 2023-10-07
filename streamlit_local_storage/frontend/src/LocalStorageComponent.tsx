import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useEffect, useMemo, useState } from "react"
import useLocalStorageState from 'use-local-storage-state'

const LocalStorageComponent:React.FC<ComponentProps> = (props:any) => {

  const { args } = props 
  const method:any = args["method"]
  const itemKey:any = args["itemKey"]
  const itemValue:any = args["itemValue"]
  const localStrageOptions:any = args["localStrageOptions"] || { defaultValue: null }
  const [todos, setTodos, {removeItem, isPersistent}] = useLocalStorageState<any>(itemKey, localStrageOptions)

  const setItemF = (itemKey:any, itemValue:any) => {
    let toSave = {item:itemKey, value:itemValue}
    setTodos(toSave)
  }  

  const deleteAll = () => {
    localStorage.clear();
    return true
  }

  const getAll = () => {
    const toSendToStreamlit = {...localStorage}
    return toSendToStreamlit
  }

  useEffect(() => {
    
    switch(method){
      case "getItem":

        Streamlit.setComponentValue({"storage":todos, "dataPersist":isPersistent})
        Streamlit.setComponentReady()
       
        break
      case "setItem":

        setItemF(itemKey, itemValue)
        break
      case "deleteItem":

        removeItem()
        break
      
      case "deleteAll":
        deleteAll()
        break
      
      case "getAll":
        const allStored = getAll()
        Streamlit.setComponentValue(allStored)
        Streamlit.setComponentReady()
        break

      default:
        break
    }


  }, [method, setTodos, todos])
  
  
  return ( 
    <div style={{display:"none"}} >
    </div>     
  )
}

export default withStreamlitConnection(LocalStorageComponent)


