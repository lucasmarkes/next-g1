import { Link } from 'react-router-dom';
import { useUser } from './Context/UserContext';
import './Style.css'
import { FaUser, FaBook, FaFilePdf, FaSearch } from "react-icons/fa";



const NovoSidebar = () => {
  const handleExportPDF = () => {
    alert('Exportar PDF');
  };

  const {userData} = useUser()
  
  return (
    <div
      className='sidebar'
    >
      <img src={userData.avatar_url} className='img-sidebar'/>
      <h2 className='user-sidebar'>{userData.name}</h2>
      <p className='local-sidebar'>{userData.location}</p>


      <Link to="/user" style={linkStyle}>
        <FaUser style={{ marginRight: '10px' }} />
        Perfil
      </Link>

      <Link to="/user/repos" style={linkStyle}>
        <FaBook style={{ marginRight: '10px' }} />
        Repositórios
      </Link>

      <button onClick={handleExportPDF} style={buttonStyle}>
        <FaFilePdf style={{ marginRight: '10px' }} />
        Exportar PDF
      </button>

        <Link to="/" style={linkStyleTest}>
        <FaSearch style={{ marginRight: '10px'}} />
        Nova Busca
      </Link>


    </div>
  );
};

const linkStyle = {
  color: 'white',
  textDecoration: 'none',
  margin: '0.7rem 1.5rem',
  fontWeight: 500,
  justifyContent: 'flex-start', 
  display: 'flex', 
};

const linkStyleTest = {
  color: 'white',
  textDecoration: 'none',
  margin: '0 1.5rem', 
  fontWeight: 500,
  justifyContent: 'flex-start', 
  display: 'flex', 
  marginTop: '170px',
  
};

const buttonStyle = {
  background: 'none',
  border: 'none',
  color: 'white',
  margin: '0.5rem 1.1rem',
  fontWeight: 500,
  cursor: 'pointer',
  whiteSpace: 'nowrap',
  
  
  
};

export default NovoSidebar;