import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './Login';
import Register from './Register';
import Dashboard from './Dashboard';
import NavBar from './NavBar/NavBar';
import Logout from './Logout';
import ProjectView from './ProjectView';

function App() {
  // store state in local storage to prevent loss after mounting (refresh/redirect)
  const [isLoggedIn, setIsLoggedIn] = useState(
    JSON.parse(localStorage.getItem('isLoggedIn')) || false
  );
  const [user, setUser] = useState(
    localStorage.getItem('user') || 'Jonathan Joestar'
  );
  // when mounting, check if user is logged in in local storage and update state
  useEffect(() => {
    localStorage.setItem('isLoggedIn', JSON.stringify(isLoggedIn));
  }, [isLoggedIn]);
  // render
  return (
    <div className='App'>
      <Router>
        <NavBar isLoggedIn={isLoggedIn} user={user} />
        <Routes>
          <Route path='/' element={<h1>Home</h1>} />
          <Route path='/login' element={<Login setIsLoggedIn={setIsLoggedIn} isLoggedIn={isLoggedIn} />} exact />
          <Route path='/register' element={<Register setIsLoggedIn={setIsLoggedIn} isLoggedIn={isLoggedIn} />}  exact />
          <Route path='/dashboard' element={<Dashboard isLoggedIn={isLoggedIn} user={user} />} exact />
          <Route path='/dashboard/project' element={<ProjectView isLoggedIn={isLoggedIn} />} exact />
          <Route path='/logout' element={<Logout setIsLoggedIn={setIsLoggedIn} />} exact />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
