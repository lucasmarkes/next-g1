// componente responsável por estabelecer a sidebar fixa e servindo de navegação na aplicação
import { Outlet } from 'react-router-dom';
import NovoSidebar from './Sidebar';

const Layout = () => {
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <NovoSidebar />
      <div style={{ flex: 1, backgroundColor: '#f9f9f9' }}>
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
