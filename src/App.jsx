import { useState } from 'react'
import Navigation from './Navigation'



function App() {
  const [count, setCount] = useState(0)

  return (
    <Navigation />
  )
}

export default App
