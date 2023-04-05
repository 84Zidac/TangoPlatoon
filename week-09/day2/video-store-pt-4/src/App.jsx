import { Outlet } from 'react-router-dom';
import './App.css';

export default function App() {
  return (
    <div id="app_root">
      <header>
        <h1>Video Store</h1>
      </header>
      <main>
        <Outlet />
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}