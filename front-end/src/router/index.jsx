import {Routes, Route, BrowserRouter} from 'react-router-dom'
import Home from '../Home'
import Users from '../Users'

function Router() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Home/>}/>
                <Route path='/user' element={<Users/>}/>
            </Routes>
        </BrowserRouter>
    )

}

export default Router