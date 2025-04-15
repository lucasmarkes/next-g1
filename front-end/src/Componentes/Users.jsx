import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "../Context/UserContext"
import '../Style.css'
import { Layout } from "antd";
import { getUserGraphCommits, getUserStatistics } from "../API/API";
import { useEffect, useState } from "react";
import Loading from "../assets/Loading.webp";

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

    console.log(statistcs, graphic)
    if (load){
        return (
            <div className="user">
                <h1>Carregando</h1>
                <img src={Loading} width="50" height="50"/>
            </div>
         )
    }

    if((statistcs === undefined || graphic === undefined) || (statistcs.detail || graphic.detail)){
        return(
            <div className="user">
                <h1>Volte Mais Tarde</h1>
            </div>
        )
    }

            
    return(
        <div>
            <div className="user">
                {/* {load && <img src={Loading} width="100" height="100"/>} */}
                <div>
                    <h2 className="statistics-title">Estatística do Usuário</h2>
                    <div className="summary-user">
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">{userData.public_repos}</b>
                            <p>Repos</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {userData.followers}
                            </b>
                            <p>Followers</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {statistcs?.forks}
                            </b>
                            <p>Forks</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {statistcs?.commits}
                            </b>
                            <p>Commits</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {userData.following}
                            </b>
                            <p>Follows</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {statistcs?.estrelas}
                            </b>
                            <p>Stars</p>
                        </div>
                        <div style={{textAlign: 'center' }}>
                            <b className="dados">
                                {statistcs?.branches}
                            </b>
                            <p>Branches</p>
                        </div>
                        <div className="summary-pr">
                            <div>
                                <b className="dados">
                                    {statistcs?.prs_abertas}
                                </b>
                                <p>PR Abertas</p>
                            </div>
                            <div>
                                <b className="dados">
                                    {statistcs?.prs_fechadas}
                                </b>
                                <p>PR Fechadas</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="statistics-user">
                    <div className="grafics-user">
                        <div className="grafics1-user">
                            <h2>Quantidade de Commits por Repo</h2>
                            <div className="grafics3-user">
                            <img src={graphic} style={{height:'300px'}}/> 
                            </div>
                        </div>
                        
                        <div className="grafics2-user">
                            <h2>Linguagem Usadas</h2>
                            <div className="languages-user">
                                <div className="languages-list">
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
        </div>
 
    )

}

export default Users