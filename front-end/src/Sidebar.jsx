import { Link } from 'react-router-dom';

const NovoSidebar = () => {
  const handleExportPDF = () => {
    alert('Exportar PDF');
  };

  return (
    <div
      style={{
        width: '300px',
        backgroundColor: '#4B006E',
        color: 'white',
        padding: '2rem 1rem',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          width: '100px',
          height: '100px',
          backgroundColor: '#ddd',
          borderRadius: '50%',
          marginBottom: '1rem',
        }}
      />
      <h2 style={{ fontSize: '1rem', textAlign: 'center' }}>Nome do Usuário</h2>
      <p style={{ fontSize: '0.875rem', color: '#ccc', marginBottom: '2rem' }}>
        Localidade
      </p>

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