import { Link } from 'react-router-dom';
import { useUser } from '../Context/UserContext';
import '../Style.css'
import { FaUser, FaBook, FaFilePdf, FaSearch } from "react-icons/fa";
import { getUserPdf } from '../API/API';



const NovoSidebar = () => {
  
  const {userData} = useUser()

  const handleExportPDF = () => {
    getUserPdf(userData.login)
  };
  
  return (
    <div
      className='sidebar'
    >
      <img src={userData.avatar_url} className='img-sidebar'/>
      <h2 className='user-sidebar'>{userData.name}</h2>
      <p className='local-sidebar'>{userData.location}</p>


      <Link to="/user" className='link'>
        <FaUser style={{ marginRight: '10px' }} />
        Perfil
      </Link>

      <Link to="/user/repos" className='link'>
        <FaBook style={{ marginRight: '10px' }} />
        Repositórios
      </Link>

      <button onClick={handleExportPDF} className='pdf-sidebar'>
        <FaFilePdf style={{ marginRight: '10px' }} />
        Exportar PDF
      </button>

        <Link to="/" className='link-search'>
        <FaSearch style={{ marginRight: '10px'}} />
        Nova Busca
      </Link>


    </div>
  );
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

export default NovoSidebar;