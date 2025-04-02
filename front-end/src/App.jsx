import { UserProvider } from "./Context/UserContext.jsx"
import Router from "./router/index.jsx"


function App() {
 

  return (
    
    <UserProvider>
      <Router/>
    </UserProvider>
    
  )
}

export default App
