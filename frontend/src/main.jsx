import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

//hooks up index.html with React code
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
