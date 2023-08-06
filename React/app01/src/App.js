import logo from './logo.svg';
import './App.css';
import Header from './header';
import Corpo from './corpo';
import Relogio from './Relogio'

function App() {
  const nome = "Agosto";
  const idade = 19;
  const peso = 68.3;
  return (
    <section>
    <Header/>
    <Corpo 
    nome={nome} 
    idade={idade} 
    peso={peso}
    />
    <Relogio/>
    </section>
  );
}

export default App;