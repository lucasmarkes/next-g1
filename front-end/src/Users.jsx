import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"
import './Style.css'


function Users() {
    const location = useLocation()

    const navigate = useNavigate()

    const {userData} = useUser()
    const {userRepos} = useUser()

    //const languages = []
    //for (const c of (userRepos.map(
    //    (repo) => ({repo.id => repo.language})
    //))){
    //    languages += x
    //}
    //console.log(languages)

    const languages = userRepos.map(repo => repo.language)
    .filter((lang,index,self) => lang && self.indexOf(lang) == index)

    //const data = location.state?.response
    //console.log(userRepos)

    return(
        <div>
            <img src ={userData.avatar_url}/>
            <h1>{userData.name}</h1>
            <p>{userData.bio}</p>
            <p>{userData.public_repos}</p>
            <p className="language">
                <ul>
                    {languages.map(
                        (lang, index) => (
                            <li key={index}>
                                {lang}
                            </li>
                        )
                        
                    )}
                </ul>
            </p>
            <button onClick={() => navigate("/repos")}>Repositorio</button>
        </div>
        
    )

}

export default Users