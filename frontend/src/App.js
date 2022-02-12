import './App.css';
import Cabecera from './components/Cabecera'
import Mapa from './components/Mapa';
import Tabla from './components/Tabla';

function App() {
  return (
    <div className="App">
      <Cabecera />
      <form>
      <div className='container-fluid' >
        <div className="row row-cols-2" style={{height: '80vh'}}>
          <div className="col-6 p-3"><input type="text" value="lat">Latitud</input></div>
          <div className="col-6 p-3 "><input type="text" value="lon">Longitud</input></div>
          <div className="col-4 p-3"><label id="total_sin">Prediccion: </label></div>
          <div className="col-8 p-3 "><Mapa id="mapa"/></div>
          <div className="col-4 p-3"></div>
          <div className="col-8 p-3 "><Tabla/></div>
        </div>
      </div>
      </form>
    </div>
  );
}

export default App;
