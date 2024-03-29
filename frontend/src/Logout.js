// logout component
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

//import axios to use backend data
import axiosInstance from "./axiosApi";

export default function Logout(props) {
  const navigate = useNavigate();

  // when ran, logout unless already logged out, then just redirect to login
  useEffect(() => {
    if (localStorage.getItem("access_token") != null) {
      // insert axios call to logout in django backend to blacklist the token
      const response = axiosInstance.post("user/logout/blacklist/", {
        refresh_token: localStorage.getItem("refresh_token"),
      });

      localStorage.clear("access_token");
      localStorage.clear("refresh_token");
      localStorage.clear("user");
      localStorage.clear("email");

      axiosInstance.defaults.headers["Authorization"] = null;
      props.setIsLoggedIn(false);
    }
    props.setIsLoggedIn(false);
    navigate("/login", { replace: true });
  }, [navigate, props]);

  return (
    <div>
      <h1>Logging Out...</h1>
    </div>
  );
}
