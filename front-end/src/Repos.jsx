import { useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"

function Repos() {
    const {userRepos} = useUser()
    console.log(userRepos)

    const navigate = useNavigate()

    return(
        <div className="repos">
            <h1 className="title-repo">Lista de Repositórios</h1>
                <div className="list-repo">
                    <ul>
                        {userRepos.map(
                            (repo) => (
                                <li onClick={() => navigate(`/user/repo/${repo.name}`)} style={{color: 'black'}} key={repo.id}>
                                    <p>{repo.name}</p>
                                </li>
                            )
                        )}
                    </ul>
                </div>
        </div>
    )

}

export default Repos