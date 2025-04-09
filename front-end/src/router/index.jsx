import {Routes, Route, BrowserRouter} from 'react-router-dom'
import Home from '../Home'
import Users from '../Users'
import Repos from '../Repos'
import Layout from '../Layout'
import StatisticRepo from '../StatisticRepo'

function Router() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Home/>}/>
                <Route path='/user' element = {<Layout/>}>
                    <Route index element={<Users/>}/>
                    <Route path='repos' element={<Repos/>}/>
                    <Route path='repo/:id' element={<StatisticRepo/>}/>
                </Route>
                
            </Routes>
        </BrowserRouter>
    )

}

export default Router