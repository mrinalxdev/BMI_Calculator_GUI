import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import SignIn from '../components/SignIn'
import Projects from '../components/Projects'
import Contact from '../components/Contact'




const AppRoute = () => {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/sign-in" element = {
                <SignIn />
            }/>
            <Route path="/projects" element = {
                <Projects />
            }/>
            <Route path="/contact" element = {
                <Contact />
            }/>
        </Routes>
    
    </BrowserRouter>
  )
}

export default AppRoute