import React, { useState, useEffect } from 'react';
import AuthNavBar from './AuthNavBar';
import NAuthNavBar from './NAuthNavBar';
import '../style/NavBar.css'
import {Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function NavBar(props){
    return(
        <>
            { (props.isLoggedIn) ? <AuthNavBar {...props} /> : <NAuthNavBar />}
        </>
    )
}