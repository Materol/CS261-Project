// logout component
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Logout(props) {
    const navigate = useNavigate();

    // when ran, logout unless already logged out, then just redirect to login
    useEffect(() => {
        if (localStorage.getItem('access_token') != null) {

            // insert axios call to logout in django backend to blacklist the token

            localStorage.clear('access_token');
            localStorage.clear('refresh_token');
            props.setIsLoggedIn(false);
        }
        props.setIsLoggedIn(false);
        navigate('/login', { replace: true });
    }, []);

    return (
        <div>
            <h1>Logging Out...</h1>
        </div>
    );
}
