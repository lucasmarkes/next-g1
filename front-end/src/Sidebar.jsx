import { Link } from 'react-router-dom';
import { useUser } from './Context/UserContext';
import './Style.css'

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

      <Link to="/user" style={linkStyle}>Perfil</Link>
      <Link to="/user/repos" style={linkStyle}>Repositórios</Link>
      <button onClick={handleExportPDF} style={buttonStyle}>
        Exportar PDF
      </button>
      <Link to="/" style={linkStyle}>Nova Busca</Link>
    </div>
  );
};

const linkStyle = {
  color: 'white',
  textDecoration: 'none',
  margin: '0.5rem 0',
  fontWeight: 500,
};

const buttonStyle = {
  background: 'none',
  border: 'none',
  color: 'white',
  margin: '0.5rem 0',
  fontWeight: 500,
  cursor: 'pointer',
};

export default NovoSidebar;