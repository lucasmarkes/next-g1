import { useParams } from "react-router-dom"
import { getRepoGraphCommits, getReposPdf, getRepoStatistics } from "../API/API"
import { useUser } from "../Context/UserContext"
import { useEffect, useState } from "react"


function StatisticRepo() {
    const { repo } = useParams()
    console.log(repo)

    const { userData } = useUser()

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
            <div>
                <h2 className="statistics-title">{repo}</h2>
                <button onClick={handleExportPDF}>PDF Repositório</button>
            </div>
            <h3>Ultimo Update</h3>
            <h3>{formatted}</h3>
            <div className="summary-user">
                <div>
                    <p>{infos?.estrelas}</p>
                    <p>Estrelas</p>
                </div>
                <div>
                    <p>{infos?.forks}</p>
                    <p>Forks</p>
                </div>
                <div>
                    <p>{infos?.watchers}</p>
                    <p>Watchers</p>
                </div>
                <div>
                    <p>{infos?.tamanho}</p>
                    <p>Tamanho</p>
                </div>

            </div>
            <div>
                <p>Grafico Commit por data</p>
                <img src={graphic} style={{ height: '280px' }} />
            </div>
            <div>
                <p>Linguagens</p>
                <p>{infos?.linguagens_repo.map(
                    (ling, index) => (
                        <div style={{ color: 'black' }} key={index}>
                            <p>{ling}</p>
                        </div>
                    ))}
                </p>
            </div>
            <div>
                <p>Top Contribuidores</p>
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

    )

}

export default StatisticRepo