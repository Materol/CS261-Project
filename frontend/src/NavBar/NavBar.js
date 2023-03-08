import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import '../style/NavBar.css';
import AuthNavBar from './AuthNavBar';
import NAuthNavBar from './NAuthNavBar';

export default function NavBar(props){
    return(
        <>
            { (props.isLoggedIn) ? <AuthNavBar /> : <NAuthNavBar />}
        </>
    )
}
