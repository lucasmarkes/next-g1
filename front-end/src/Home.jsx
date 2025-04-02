import { createContext, useEffect, useState } from 'react'
import logo from './assets/RetroGit.png'
import { getRepos, getUser } from './API/API'
import { useNavigate } from 'react-router-dom'
import './Style.css'
import { useUser } from './Context/UserContext'

function Home() {
    const [user, setUser] = useState("")
    const [data, setData] = useState()
    const {setUserData, setUserRepos} = useUser()

    const navigate = useNavigate()

    const handleSearch = async () => {
        try {
            const response = await getUser(user)
            const responseRepos = await getRepos(user)
            setUserData(response)
            setUserRepos(responseRepos)
            navigate("/user")

        } catch (error) {
            console.log(error)
        }
    }

    return (
        <>
            <div className="App">
                <img src={logo} />
                <h1>Retrospecgit</h1>
                <div>
                    <input
                        type="text"
                        placeholder="Digite o nome do usário"
                        value={user}
                        onChange={(e => setUser(e.target.value))} />
                    <button
                        onClick={handleSearch}
                        disabled={user.length === 0}>Busca</button>

                </div>

            </div>
        </>
    )

}

export default Home