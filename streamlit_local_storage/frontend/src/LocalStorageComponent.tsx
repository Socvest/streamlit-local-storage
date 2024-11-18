import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useEffect, useMemo, useState } from "react"
import useLocalStorageState from 'use-local-storage-state'

const LocalStorageComponent: React.FC<ComponentProps> = (props: any) => {

  const { args } = props
  const method: any = args["method"]
  const itemKey: any = args["itemKey"]
  const itemValue: any = args["itemValue"]
  const localStorageOptions: any = args["localStorageOptions"] || { defaultValue: null }
  const [localStorageItems, setLocalStorageItems, { removeItem, isPersistent }] = useLocalStorageState<any>(itemKey, localStorageOptions)

  const setItemF = (itemKey: any, itemValue: any) => {

    let toSave = { [itemKey]: itemValue }
    setLocalStorageItems(toSave)
  }

  const deleteAll = () => {
    localStorage.clear();
    return true
  }

  const eraseItem = (itemKey: any) => {
    localStorage.removeItem(itemKey)
  }

    const getAll = () => {
    const allKeys = Object.keys(localStorage);
    const results = { ...localStorage };
    const updatedLocalStorage: any = {};
  
    allKeys.forEach((key: string) => {
      try {
        const value = results[key];
        const parsedValue = JSON.parse(value);
        
        if (parsedValue !== null && typeof parsedValue === 'object' && key in parsedValue) {
          updatedLocalStorage[key] = parsedValue[key];
        } else {
          updatedLocalStorage[key] = parsedValue;
        }
      } catch (error) {
        // If JSON parsing fails, store the original string value
        updatedLocalStorage[key] = results[key];
      }
    });
  
    setAllLocalStorage(updatedLocalStorage);
    return updatedLocalStorage;
  };

  useEffect(() => {

    Streamlit.setFrameHeight(0)
  })

  useEffect(() => {

    switch (method) {
      case "getItem":

        Streamlit.setComponentReady()
        Streamlit.setComponentValue(localStorageItems)

        break
      case "setItem":

        setItemF(itemKey, itemValue)
        break
      case "deleteItem":

        removeItem()
        break

      case "eraseItem":

        eraseItem(itemKey)
        break

      case "deleteAll":
        deleteAll()
        break

      case "getAll":
        const allStored = getAll()
        Streamlit.setComponentReady()
        Streamlit.setComponentValue(allStored)

        break

      default:
        break
    }


  }, [method, setLocalStorageItems, localStorageItems])


  return (
    <div style={{ display: "none" }} >
    </div>
  )
}

export default withStreamlitConnection(LocalStorageComponent)
