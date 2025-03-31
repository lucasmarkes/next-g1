import { useLocation } from "react-router-dom"

function Users() {
    const location = useLocation()

    const data = location.state?.response
    console.log(data)

    return(
        <div>
            <img src ={data.avatar_url}/>
            <h1>{data.name}</h1>
            <p>{data.bio}</p>
        </div>
        
    )

}

export default Users