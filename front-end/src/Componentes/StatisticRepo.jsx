//Componente que apresenta as informações estatísticas do repositório escolhido no componente Repos
import { useParams } from "react-router-dom"
import { getRepoGraphCommits, getReposPdf, getRepoStatistics } from "../API/API"
import { useUser } from "../Context/UserContext"
import { useEffect, useState } from "react"
import Loading from "../assets/Loading.webp"


function StatisticRepo() {
    const { repo } = useParams()
    console.log(repo)

    const { userData } = useUser()

    //Nesse trecho, temos as funções que estabelecerão as comunicações com as APIs com gráficos e informações estatísticas
    const [graphic, setGraphic] = useState()
    const [infos, setInfos] = useState()
    const [load, setLoad] = useState()
    useEffect(() => {
        async function getData() {
            setLoad(true)
            const response = await getRepoGraphCommits(userData.login, repo)
            setGraphic(response)
            const responseRepo = await getRepoStatistics(userData.login, repo)
            setInfos(responseRepo)
            setLoad(false)
        }
        getData()
    }, [])

    if (load){
        return (
            <div className="user, center-container">
                <h1>Carregando</h1>
                <img src={Loading} width="50" height="50"/>
            </div>
         )
    }

    //Essa função gera o relatório pdf do repositório
    const handleExportPDF = () => {
        getReposPdf(userData.login,repo)
      };

    const isoDate = new Date(infos?.ultima_atualizacao)
    const formatted = isoDate.toLocaleDateString("pt-BR",
        {
            day: "2-digit",
            month: "2-digit",
            year: "numeric"
        }
    )

    return (
        <div className="repo-statistics">
            <div style={{direction: 'rtl', display: 'flex'}}><button className= "pdf-repo" onClick={handleExportPDF}>PDF Repositório</button></div>
            <div>
                <h2 className="statistics-repo-title">{repo}</h2>
            </div>
            <div className="date">
                <h3>:Ultimo Update</h3>
                <h3>{formatted}</h3>
            </div>
            <div className="summary-user">
                <div>
                    <div className="dados">{infos?.estrelas}</div>
                    <p>Estrelas</p>
                </div>
                <div>
                    <div className="dados">{infos?.forks}</div>
                    <p>Forks</p>
                </div>
                <div>
                    <div className="dados">{infos?.watchers}</div>
                    <p>Watchers</p>
                </div>
                <div>
                    <div className="dados" style={{fontSize: 'smaller'}}>{infos?.tamanho}</div>
                    <p>Tamanho</p>
                </div>

            </div>
            <div style={{display: 'flex', justifyContent: 'space-around'}}>
                <div className="graphics1-repo">
                    <h2 className="title-infos">Grafico Commit por data</h2>
                    <div className="grafics3-user">
                        <img src={graphic} style={{ height: '280px' }} /> 
                    </div>
                    
                </div>
                <div style={{display: 'grid'}}>
                    <div>
                        <h2 className="title-infos">Linguagens</h2>
                        <div className="list-repos-statis">
                           <p>{infos?.linguagens_repo.map(
                                (ling, index) => (
                                <div style={{ color: 'black' }} key={index}>
                                    <p>{ling}</p>
                                </div>
                                ))}
                            </p> 
                        </div>
                    </div>
                    <div>
                        <h2 className="title-infos">Top Contribuidores</h2>
                        <div className="list-repos-statis">
                            <p>
                                {infos?.contribuidores?.length>0?infos?.contribuidores.map(
                                    (contri, index) =>(
                                        <div key={index}>
                                            <p>{contri}</p>
                                        </div>
                                    )
                                ):"Sem Contribuidores"}
                            </p>
                        </div>
                    </div>
                </div>
                
            </div>

        </div>

    )

}

export default StatisticRepo