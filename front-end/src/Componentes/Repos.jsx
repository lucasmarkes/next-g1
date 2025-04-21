//Componente resposável por apresentar cards com repositórios
// para direcionar o usuário as estatísticas do repositório escolhido
import { useNavigate } from "react-router-dom"
import { useUser } from "../Context/UserContext"

function Repos() {
    const {userRepos} = useUser()
    console.log(userRepos)

    const navigate = useNavigate()

    return(
        <div className="repos">
            <h1 className="title-repo">Lista de Repositórios</h1>
                <div className="list-repo">
                    <div>
                        {userRepos.map(
                            (repo) => (
                                <div className="repo-card" key={repo.id}>
                                    <button onClick={() => navigate(`/user/repo/${repo.name}`)}>click</button>
                                    <p>{repo.name}</p>                                    
                                </div>
                            )
                        )}
                    </div>
                </div>
        </div>
    )

}

export default Repos