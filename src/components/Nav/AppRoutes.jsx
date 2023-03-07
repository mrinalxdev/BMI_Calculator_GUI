import React from 'react'
import ReactDOM from 'react-dom'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

import SignIn from '../components/Auth/SignIn'
import SignUp from '../components/Auth/SignUp'
import Explore from '../components/Explore/Explore'




const AppRoutes = () => {
  return (
    <BrowserRouter>

        <Routes>

            <Route path = '/explore' element = {
                <Explore />
            } />

            <Route path = '/signin' element = {
                <SignIn />
            } />

            <Route path = '/signup' element = {
                <SignUp />
            } />

        </Routes>

    </BrowserRouter>
  )
}

export default AppRoutes