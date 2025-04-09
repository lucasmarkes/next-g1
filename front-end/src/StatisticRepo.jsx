import { useParams } from "react-router-dom"
import { getRepoGraphCommits } from "./API/API"
import { useUser } from "./Context/UserContext"
import { useEffect, useState } from "react"

function StatisticRepo(){
    const {id} = useParams()
    console.log(id)

    const {userData} = useUser()

    const [graphic, setGraphic] = useState()
    const [load, setLoad] = useState()
        useEffect(() => {
            async function getData(){
                setLoad(true)
                const response = await getRepoGraphCommits(userData.login, id)
                setGraphic(response)
                setLoad(false)
            }
            getData()
        }, [])

    return(
        <div>
            <h1>{id}</h1>
            <img src={graphic}/>
        </div>
    )

}

export default StatisticRepo