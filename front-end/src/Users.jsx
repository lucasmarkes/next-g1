import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"
import './Style.css'
import { Layout } from "antd";
import { getUserStatistics } from "./API/API";
import { useEffect, useState } from "react";
import Loading from "./assets/Loading.webp"



const { Content } = Layout;


 function Users() {
    //const location = useLocation()

    const navigate = useNavigate()

    const {userData} = useUser()
    const {userRepos} = useUser()
    
    const [statistcs, setStatistics] = useState()
    const [load, setLoad] = useState()
    useEffect(() => {
        async function getData(){
            setLoad(true)
            const response = await getUserStatistics(userData.login)
            setStatistics(response)
            setLoad(false)
        }
        getData()
    }, [])

    if (load){
        return <img src={Loading} width="200" height="200"/>
    }
          
    return(
        <div className="user">
            <div>
                <h2 className="statistics-title-user">Estatística do Usuário</h2>
                <div className="summary-user">
                   <p>Repos</p>
                   <p>Followers</p>
                   <p>Forks</p>
                   <p>Commits</p>
                   <p>Follows</p>
                   <div style={{textAlign:'center'}}>
                        <b>{statistcs?.estrelas}</b>
                        <p>Stars</p>
                    </div>
                   <p>Branches</p>
                   <p>PRs</p> 
                </div>
            </div>

            <div className="statistics-user">
                <div className="grafics-user">
                    <div className="grafics1-user">
                        <h2>Título do Gráfico 2</h2>
                        <div className="grafics3-user">Grafico de Bia</div>
                    </div>
                    
                    <div className="grafics2-user">
                        <h2>Linguagem Usadas</h2>
                        <div className="languages-user">
                            <div style={{display: 'flex', gap: '16px', textAlign: 'center'}}>
                                {statistcs?.linguagens.map(
                                (ling) => (
                                    <div style={{color: 'black'}} key={ling.linguagem}>
                                        <p>{ling.porcentagem.toFixed(2)}%</p>
                                        <p>{ling.linguagem}</p>
                                    </div>
                                )
                                )}
                            </div>
                        </div>
                    </div>
                </div>
                <div className="repo-user">
                    <h2>Lista Repositórios</h2>
                    <div className="list-repos-user">
                        <ul>
                            {userRepos.map(
                                (repo) => (
                                    <li style={{color: 'black'}} key={repo.id}>
                                        <p>{repo.name}</p>
                                    </li>
                                )
                            )}
                        </ul>
                    </div>
                </div>

            </div>
        </div>
 
    )

}

export default Users