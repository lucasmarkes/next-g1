import { useEffect, useState } from 'react'
import logo from './assets/RetroGit.png'
import { getUser } from './API/API'
import { useNavigate } from 'react-router-dom'

function Home() {
    const [user, setUser] = useState("")
    const [data, setData] = useState()

    const navigate = useNavigate()

    const handleSearch = async () => {
        try { 
            const response = await getUser(user)
            setData(response)
            navigate("/user", {state: {response}})
            
        } catch (error) {
            console.log(error)
        }
    }

    return(
        <>
            <div style={{
                            height: '100%',
                            width: '100%',
                            textAlign: 'center',
                            minHeight: '100vh',
                            display: 'flex',
                            flexDirection: 'column',
                            justifyContent: 'center'
                        }} >
                <img src={logo} />
                <h1 style={{color:"white", textAlign: 'center'}}>Retrospecgit</h1>
                <div>
                    <input 
                        type="text" 
                        placeholder="Digite o nome do usário" 
                        value={user} 
                        onChange={(e => setUser(e.target.value))}/>
                    <button 
                    onClick={handleSearch} 
                    disabled={user.length === 0 }>Busca</button>
                </div>
                
            </div>
        </>
    )

}

export default Home