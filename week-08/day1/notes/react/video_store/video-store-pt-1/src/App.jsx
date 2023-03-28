import HomePage from './components/HomePage';
import './App.css';
import inventory from './data/inventory.json';

export default function App() {
  return (
    <div id="app_root">
      <header>
        <marquee scrollamount="30" behavior="alternate">Video Store!!!</marquee>
      </header>
      <main>
        <HomePage inventory={inventory} />
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}