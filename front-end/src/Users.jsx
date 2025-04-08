import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"
import './Style.css'
import { Layout } from "antd";



const { Content } = Layout;


 function Users() {
    //const location = useLocation()

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
       
        //<Layout style={{ marginLeft: 200 }}>
        // <Content
        //     style={{
        //     //padding: "24px",
        //     overflowY: "auto",
        //     height: "100vh",
        //     background: "#f5f5f5",
        //     display: "flex",
        //     flexDirection: "column",
        //     alignItems: "center",
        //     gap: "50px",
        //     }}
        // >
        
        //     <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
        //     <h1 className="texto-roxo"> Título gráfico 1</h1>
        //     </div>

        //     <div
        //     style={{
        //         background: "rgba(217, 217, 217, 1)",
        //         minHeight: "292px",
        //         width: "950px",
        //         display: "flex",
        //         justifyContent: "center",
        //         alignItems: "center",
        //         borderRadius: "10px",
        //         marginTop: "-50px",
        //     }}
        //     ></div>

        //     <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
        //     <h1 className="texto-roxo">Estatísticas do Usuário</h1>
        //     </div>

           
        //     <div
        //     style={{
        //         background: "rgba(217, 217, 217, 1)",
        //         minHeight: "200px",
        //         width: "950px",
        //         display: "flex",
        //         justifyContent: "space-around",
        //         alignItems: "center",
        //         borderRadius: "10px",
        //         marginTop: "-50px",
        //         padding: "20px"
        //     }}
        //     >
        //     <div className="container-flex">
        //         <div className="caixa"></div>
        //         <p className="titulo">Repo</p>
        //     </div>
        //     <div className="container-flex">
        //         <div className="caixa"></div>
        //         <p className="titulo">Followers</p>
        //     </div>
        //     <div className="container-flex">
        //         <div className="caixa"></div>
        //         <p className="titulo">Forks</p>
        //     </div>
        //     <div className="container-flex">
        //         <div className="caixa"></div>
        //         <p className="titulo">Commits</p>
        //     </div>
        //     </div>

        //     <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
        //     <h1 className="texto-roxo">Linguagens usadas</h1>
        //     </div>
            
        //     <div
        //     style={{
        //         background: "rgba(217, 217, 217, 1)",
        //         minHeight: "150px",
        //         width: "500px",
        //         display: "flex",
        //         justifyContent:"space-around" ,
        //         alignItems: "center",
        //         borderRadius: "10px",
        //         marginTop: "-50px",
        //         padding: "20px",
        //         gap: "20px", 
        //         flexWrap: "wrap", 
        //         marginLeft: "-450px"
        //     }}
        //     >
        //     <div className="container-flex">
        //         <div className="circulo" st></div>
        //     </div>
        //     <div className="container-flex">
        //         <div className="circulo"></div>
        //     </div>
        //     <div className="container-flex">
        //         <div className="circulo"></div>
        //     </div>
        //     <div className="container-flex">
        //         <div className="circulo"></div>
        //     </div>
        //     </div>
        


    
        // </Content>
        //</Layout>
        
        <div className="user">
            <div>
                <h2 className="statistics-title-user">Estatística do Usuário</h2>
                <div className="summary-user">
                   <p>Repos</p>
                   <p>Followers</p>
                   <p>Forks</p>
                   <p>Commits</p>
                   <p>Follows</p>
                   <p>Stars</p>
                   <p>Branches</p>
                   <p>PRs</p> 
                </div>
            </div>

            <div className="statistics-user">
                <div className="grafics-user">
                    <div className="grafics1-user">
                        <h2>Título do Gráfico 2</h2>
                        <div className="grafics3-user">Grafico de Bia</div>
                    </div>
                    
                    <div className="grafics2-user">
                        <h2>Linguagem Usadas</h2>
                        <div className="languages-user">Linguagens de Bia</div>
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
 
    )

}

export default Users