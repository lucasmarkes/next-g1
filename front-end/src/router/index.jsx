import {Routes, Route, BrowserRouter} from 'react-router-dom'
import Users from '../Componentes/Users'
import Repos from '../Componentes/Repos'
import Layout from '../Componentes/Layout'
import StatisticRepo from '../Componentes/StatisticRepo'
import Home from '../Componentes/Home'

function Router() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Home/>}/>
                <Route path='/user' element = {<Layout/>}>
                    <Route index element={<Users/>}/>
                    <Route path='repos' element={<Repos/>}/>
                    <Route path='repo/:repo' element={<StatisticRepo/>}/>
                </Route>
                
            </Routes>
        </BrowserRouter>
    )

}

export default Router