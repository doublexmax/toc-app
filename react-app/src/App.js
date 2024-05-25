import {useEffect, useState} from "react";
import DFA from "./DFA";

import './App.css';

function App() {
  const [machine, setMachine] = useState('DFA'); 

  useEffect(() => {
    console.log('triggered', machine);
  })

  return (
    <div className="App">
      <header className="App-header">
          <nav className="navbar-brand m-0"> DiagramDeph </nav>
          <hr className="header-separator"></hr>
          <div className="btn-toolbar mb-2" role="toolbar">
            <div className="btn-group-sm" role="group">
              {machine === 'DFA' ? 
                <button type="button" className="btn btn-secondary mr-4 machine-btn active" onClick={() => setMachine('DFA')}>DFA</button>
                :
                <button type="button" className="btn btn-secondary mr-4 machine-btn" onClick={() => setMachine('DFA')}>DFA</button>
              }
              {machine === 'NFA' ? 
                <button type="button" className="btn btn-secondary mr-4 machine-btn active" onClick={() => setMachine('NFA')}>NFA</button>
                :
                <button type="button" className="btn btn-secondary mr-4 machine-btn" onClick={() => setMachine('NFA')}>NFA</button>
              }
              {machine === 'PDA' ? 
                <button type="button" className="btn btn-secondary mr-4 machine-btn active" onClick={() => setMachine('PDA')}>PDA</button>
                :
                <button type="button" className="btn btn-secondary mr-4 machine-btn" onClick={() => setMachine('PDA')}>PDA</button>
              }
            </div>
          </div>
      </header>
      <div className="m-0 p-0">
          {machine==='DFA' && <DFA />}
      </div>
    </div>
  );
}

export default App;
