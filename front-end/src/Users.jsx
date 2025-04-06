import { useLocation, useNavigate } from "react-router-dom"
import { useUser } from "./Context/UserContext"
import './Style.css'
import { Menu, Layout } from "antd";
import {
    UserOutlined,
    FolderOutlined,
    FilePdfOutlined,
    ArrowLeftOutlined
} from "@ant-design/icons";


const { Sider, Content } = Layout;


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
       <Layout style={{ minHeight: "100vh" }}>
        <Sider
        width={200}
        style={{
            backgroundColor: "rgba(100, 2, 124, 1)",
            position: "fixed",
            height: "100vh",
            left: 0,
        }}
        >
        <div style={{ color: "white", textAlign: "center", padding: "20px" }}>
            <img
            src={userData.avatar_url}
            alt="Avatar"
            style={{
                width: "115px",
                height: "115px",
                borderRadius: "50%",
                border: "5px solid rgba(0,0,0,1)",
                background: "#fff",
                padding: "8px",
                boxShadow: "0 0 20px rgba(0,0,0,1)",
            }}
            />
            <h1 style={{ fontSize: "16px", marginTop: 18 }}>{userData.name}</h1>
            <p>Localidade</p>
        </div>

        <Menu
            className="custom-menu"
            theme="dark"
            mode="inline"
            defaultSelectedKeys={["1"]}
            style={{
            marginTop: "20px",
            backgroundColor: "rgba(100, 2, 124, 1)",
            }}
        >
            <Menu.Item key="1" icon={<UserOutlined />} onClick={() => navigate("/user")}>
            Perfil
            </Menu.Item>
            <Menu.Item key="2" icon={<FolderOutlined />} onClick={() => navigate("/repos")}>
            Repositórios
            </Menu.Item>
            <Menu.Item key="3" icon={<FilePdfOutlined />}>Exportar PDF</Menu.Item>
            <Menu.Item
            key="4"
            icon={<ArrowLeftOutlined />}
            onClick={() => navigate("/")}
            style={{ marginTop: "200px" }}
            >
            Nova busca
            </Menu.Item>
        </Menu>
        </Sider>


        <Layout style={{ marginLeft: 200 }}>
        <Content
            style={{
            padding: "24px",
            overflowY: "auto",
            height: "100vh",
            background: "#f5f5f5",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: "50px",
            }}
        >
        
            <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
            <h1 className="texto-roxo"> Título gráfico 1</h1>
            </div>

            <div
            style={{
                background: "rgba(217, 217, 217, 1)",
                minHeight: "292px",
                width: "950px",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                borderRadius: "10px",
                marginTop: "-50px",
            }}
            ></div>

            <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
            <h1 className="texto-roxo">Estatísticas do Usuário</h1>
            </div>

           
            <div
            style={{
                background: "rgba(217, 217, 217, 1)",
                minHeight: "200px",
                width: "950px",
                display: "flex",
                justifyContent: "space-around",
                alignItems: "center",
                borderRadius: "10px",
                marginTop: "-50px",
                padding: "20px"
            }}
            >
            <div className="container-flex">
                <div className="caixa"></div>
                <p className="titulo">Repo</p>
            </div>
            <div className="container-flex">
                <div className="caixa"></div>
                <p className="titulo">Followers</p>
            </div>
            <div className="container-flex">
                <div className="caixa"></div>
                <p className="titulo">Forks</p>
            </div>
            <div className="container-flex">
                <div className="caixa"></div>
                <p className="titulo">Commits</p>
            </div>
            </div>

            <div style={{ alignSelf: "flex-start", marginLeft: "80px" }}>
            <h1 className="texto-roxo">Linguagens usadas</h1>
            </div>
            
            <div
            style={{
                background: "rgba(217, 217, 217, 1)",
                minHeight: "150px",
                width: "500px",
                display: "flex",
                justifyContent:"space-around" ,
                alignItems: "center",
                borderRadius: "10px",
                marginTop: "-50px",
                padding: "20px",
                gap: "20px", 
                flexWrap: "wrap", 
                marginLeft: "-450px"
            }}
            >
            <div className="container-flex">
                <div className="circulo" st></div>
            </div>
            <div className="container-flex">
                <div className="circulo"></div>
            </div>
            <div className="container-flex">
                <div className="circulo"></div>
            </div>
            <div className="container-flex">
                <div className="circulo"></div>
            </div>
            </div>
        


    
        </Content>
        </Layout>
  </Layout>
    )

}

export default Users