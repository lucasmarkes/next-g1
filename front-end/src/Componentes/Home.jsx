import { createContext, useEffect, useState } from 'react'
import logo from '../assets/RetrospectGit.png'
import { getRepos, getUser } from '../API/API'
import { useNavigate } from 'react-router-dom'
import '../Style.css'
import { useUser } from '../Context/UserContext'

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
                <img src={logo} width='350'/>
                {/* <h1 style={{color: '#64027c'}}>Retrospecgit</h1> */}
                <h1>
                    <input
                        type="text"
                        placeholder="Digite o nome do usuário"
                        value={user}
                        className="search-container"
                        onChange={(e) => setUser(e.target.value)}
                        onKeyDown={(e) => {
                        if (e.key === 'Enter' && user.length > 0) {
                            handleSearch();
                        }
                        }}
                    />
                </h1>

                <h1>
                    <button
                        onClick={handleSearch}
                        disabled={user.length === 0}>
                        Buscar
                    </button>
                </h1>

            </div>
        </>
    )

}

export default Home