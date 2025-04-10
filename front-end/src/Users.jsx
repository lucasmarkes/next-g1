import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"
import './Style.css'
import { Layout } from "antd";
import { getUserGraphCommits, getUserStatistics } from "./API/API";
import { useEffect, useState } from "react";
import Loading from "./assets/Loading.webp";
import circulo from "./assets/circulo.jpg"



const { Content } = Layout;


 function Users() {
    //const location = useLocation()

    const navigate = useNavigate()

    const {userData} = useUser()
    const {userRepos} = useUser()
    
    const [statistcs, setStatistics] = useState()
    const [load, setLoad] = useState()
    const [graphic, setGraphic] = useState()
    useEffect(() => {
        async function getData(){
            setLoad(true)
            const response = await getUserStatistics(userData.login)
            setStatistics(response)
            const responseGraph = await getUserGraphCommits(userData.login)
            setGraphic(responseGraph)
            setLoad(false)
        }
        getData()
    }, [])

    if (load){
        return <img src={Loading} width="50" height="50"/>
    }
          
    return(
        <div className="user">
            <div>
                <h2 className="statistics-title-user">Estatística do Usuário</h2>
                <div className="summary-user">
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>{userData.public_repos}</b>
                        <p>Repos</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                            {userData.followers}
                        </b>
                        <p>Followers</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                            {statistcs?.forks}
                        </b>
                        <p>Forks</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                            {statistcs?.commits}
                        </b>
                        <p>Commits</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                            {userData.following}
                        </b>
                        <p>Follows</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>{statistcs?.estrelas}</b>
                        <p>Stars</p>
                    </div>
                    <div style={{textAlign: 'center' }}>
                        <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                            {statistcs?.branches}
                        </b>
                        <p>Branches</p>
                    </div>
                    <div style={{textAlign: 'center', verticalAlign: 'center'}}>
                        <div style={{textAlign: 'center', justifyContent: 'space-between'}}>
                            <td style={{verticalAlign: 'center'}}>
                                <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                                {statistcs?.prs_abertas}
                                </b>
                                <p>Abertas</p>
                            </td>
                            <td>
                                <b style={{display: 'inline-block', borderColor: 'black', borderRadius:'50%', height: '25px', width: '25px', backgroundColor: 'white', textAlign: 'center', verticalAlign: 'baseline' }}>
                                {statistcs?.prs_fechadas}
                                </b>
                                <p>Fechadas</p>
                            </td>
                        </div>
                        <p>PRs</p> 
                    </div>
                </div>
            </div>

            <div className="statistics-user">
                <div className="grafics-user">
                    <div className="grafics1-user">
                        <h2>Título do Gráfico 2</h2>
                        <div className="grafics3-user">
                           <img src={graphic} style={{height: '280px'}}/> 
                        </div>
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