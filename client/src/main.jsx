import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { createHashRouter, RouterProvider } from 'react-router-dom'

import Search from './Search'
import Account from './Account'
import Profile from './Profile'
import Player from './Player'

const router = createHashRouter([
  {
    path: '/',
    element: <App />,
    children: [
      {
        path: '/',
        element: <Search />
      },
      {
        path: '/account',
        element: <Account />
      },
      {
        path: '/profile',
        element: <Profile />
      },
      {
        path: '/player/:username',
        element: <Player />
      },
    ]
  },
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)