import {Routes, Route, BrowserRouter} from 'react-router-dom'
import Home from '../Home'
import Users from '../Users'
import Repos from '../Repos'

function Router() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Home/>}/>
                <Route path='/user' element={<Users/>}/>
                <Route path='/repos' element={<Repos/>}/>
            </Routes>
        </BrowserRouter>
    )

}

export default Router