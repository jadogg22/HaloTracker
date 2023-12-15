import { Outlet } from 'react-router-dom'
import React from 'react'
import Navbar from './Navbar'

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {

  return (
    <>
      <div>
        <Navbar />
        <Outlet />
      </div>
    </>
  )
}

export default App;