import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"

function Users() {
    const location = useLocation()

    const navigate = useNavigate()

    const {userData} = useUser()

    //const data = location.state?.response
    //console.log(userRepos)

    return(
        <div>
            <img src ={userData.avatar_url}/>
            <h1>{userData.name}</h1>
            <p>{userData.bio}</p>
            <button onClick={() => navigate("/repos")}>Repositorio</button>
        </div>
        
    )

}

export default Users