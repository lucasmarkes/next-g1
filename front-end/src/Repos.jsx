import { useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"

function Repos() {
    const {userRepos} = useUser()
    console.log(userRepos)

    const navigate = useNavigate()

    return(
        <div style={{backgroundColor: 'white'}}>
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
    )

}

export default Repos