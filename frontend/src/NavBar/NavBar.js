import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import "../style/NavBar.css";
import AuthNavBar from "./AuthNavBar";
import NAuthNavBar from "./NAuthNavBar";

export default function NavBar(props) {
  return <>{props.isLoggedIn ? <AuthNavBar {...props} /> : <NAuthNavBar />}</>;
}
