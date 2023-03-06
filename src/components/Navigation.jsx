import React from 'react'
import AppRoute from '../components/AppRoute'

import '../index.css'

const Navigation = () => {
  return (
    <>
       <h1>Navigation</h1>

       <a href="http://127.0.0.1:5173/sign-in">Sign IN</a>
       <a href="http://127.0.0.1:5173/projects">Project Section</a>
       <a href="http://127.0.0.1:5173/contact">Contact Section</a>

       <AppRoute />
    </>
  )
}

export default Navigation