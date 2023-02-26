import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import NavBar from './NavBar';

function App() {
  return (
    <div className='App'>
      <Router>
        <NavBar />
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
