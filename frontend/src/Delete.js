// component to delete a project given its ID
import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

export default function Delete() {
    const navigate = useNavigate();
    const location = useLocation();
    const id = location.state.id
    // when ran, delete the project
    useEffect(() => {
        // delete the project through django using project id, then redirect to dashboard.
        navigate('/dashboard', { replace: true });
    }, []);
}