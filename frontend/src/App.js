import { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CreateProj from "./CreateProject/CreateProj";
import Dashboard from "./Dashboard";
import Delete from "./Delete";
import EditProj from "./EditProject/EditProj";
import Login from "./Login";
import Logout from "./Logout";
import NavBar from "./NavBar/NavBar";
import ProjectView from "./ProjectView";
import Register from "./Register";

function App() {
  // store state in local storage to prevent loss after mounting (refresh/redirect)
  const [fetchProjects, setFetchProjects] = useState(
    JSON.parse(localStorage.getItem("fetchProjects")) || true
  );
  const [isLoggedIn, setIsLoggedIn] = useState(
    JSON.parse(localStorage.getItem("isLoggedIn")) || false
  );
  const [user, setUser] = useState(
    localStorage.getItem("user") || "Jonathan Joestar"
  );
  const [email, setEmail] = useState(
    localStorage.getItem("email") || "jon.joe@star.com"
  );

  // when mounting, check if user is logged in in local storage and update state
  useEffect(() => {
    localStorage.setItem("fetchProjects", JSON.stringify(fetchProjects));
    localStorage.setItem("isLoggedIn", JSON.stringify(isLoggedIn));
    localStorage.setItem("user", user);
    localStorage.setItem("email", email);
  }, [email, fetchProjects, isLoggedIn, user]);
  // render
  return (
    <div className="App">
      <Router>
        <NavBar
          isLoggedIn={isLoggedIn}
          setFetchProjects={setFetchProjects}
          user={user}
        />
        <Routes>
          <Route path="/" element={<h1>Home</h1>} />
          <Route
            path="/login"
            element={
              <Login
                setIsLoggedIn={setIsLoggedIn}
                setFetchProjects={setFetchProjects}
                setUser={setUser}
                setEmail={setEmail}
                email={email}
                isLoggedIn={isLoggedIn}
              />
            }
            exact
          />
          <Route
            path="/register"
            element={
              <Register
                setIsLoggedIn={setIsLoggedIn}
                setFetchProjects={setFetchProjects}
                setUser={setUser}
                setEmail={setEmail}
                email={email}
                isLoggedIn={isLoggedIn}
              />
            }
            exact
          />
          <Route
            path="/dashboard"
            element={
              <Dashboard
                fetchProjects={fetchProjects}
                setFetchProjects={setFetchProjects}
                isLoggedIn={isLoggedIn}
                user={user}
                email={email}
              />
            }
            exact
          />
          <Route
            path="/dashboard/createproject"
            element={
              <CreateProj
                setFetchProjects={setFetchProjects}
                isLoggedIn={isLoggedIn}
                email={email}
              />
            }
            exact
          />
          <Route
            path="/dashboard/project"
            element={<ProjectView isLoggedIn={isLoggedIn} />}
            exact
          />
          <Route
            path="/dashboard/project/edit"
            element={
              <EditProj
                setFetchProjects={setFetchProjects}
                isLoggedIn={isLoggedIn}
              />
            }
            exact
          />
          <Route
            path="/dashboard/project/delete"
            element={<Delete setFetchProjects={setFetchProjects} />}
            exact
          />
          <Route
            path="/logout"
            element={<Logout setIsLoggedIn={setIsLoggedIn} setUser={setUser} />}
            exact
          />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
