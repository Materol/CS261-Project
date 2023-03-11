// component to delete a project given its ID
import React, { useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";

//import axios to use backend data
import axiosInstance from "./axiosApi";

export default function Delete(props) {
  const navigate = useNavigate();
  const location = useLocation();
  const id = location.state.id;
  // when ran, delete the project
  useEffect(() => {
    // delete the project through django using project id, then redirect to dashboard.
    axiosInstance.delete("admin/delete/" + id);
    props.setFetchProjects(true);
    navigate("/dashboard", { replace: true });
  }, []);
}
