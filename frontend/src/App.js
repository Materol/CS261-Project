import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Register from './Register';

function App() {
  return (
    <div className='App'>
      <Router>
        <Routes>
          <Route path='/' element={<h1>Home</h1>} />
          <Route path='/login' element={<Login />} exact />
          <Route path='/register' element={<Register />} exact />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
