// necessary imports
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Register.css'
// import { useAuth } from './AuthContext';
import { Link } from 'react-router-dom';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


//import axios to use backend data
import axiosInstance from './axiosApi';


// register function component
export default function Register(props) {
    // state variables
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [passwordConfirm, setPasswordConfirm] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    // check to see if logged in, if so, navigate to dashboard
    useEffect(() => {
        if (props.isLoggedIn) {
            navigate('/dashboard');
        }
    }, [navigate]);

    
    //TODO: Add set error / set loading

    //Creates user and logs them in
	const handleSubmit = (e) => {
		e.preventDefault();
        

        // password check
        if (password !== passwordConfirm) {
            return setError('Passwords do not match');
        }
        
		axiosInstance
			.post(`user/create/`, {
				email: email,
                user_name: username,
				password: password,
			})
			.then((res) => {
                props.setUser(username)
                props.setIsLoggedIn(true);
				navigate('/dashboard');
			});
	};


    return (
        <>
        <div className='registerCard'>
            <Card>
                <Card.Body>
                <h2 className="text-center mb-4">Register</h2>
                {error && <Alert variant="danger">{error}</Alert>}
                <Form onSubmit={handleSubmit}>
                    <Form.Group id="email">
                    <Form.Label className='rEmailLabel'>Email</Form.Label>
                    <Form.Control type="email" required onChange={e => setEmail(e.target.value)} />
                    </Form.Group>
                    <Form.Group id="username">
                    <Form.Label className='rUsernameLabel'>Username</Form.Label>
                    <Form.Control type="text" required onChange={e => setUsername(e.target.value)} />
                    </Form.Group>
                    <Form.Group id="password">
                    <Form.Label className='rPasswordLabel'>Password</Form.Label>
                    <Form.Control type="password" required onChange={e => setPassword(e.target.value)} />
                    </Form.Group>
                    <Form.Group id="password-confirm">
                    <Form.Label className='rPasswordConfirmLabel'>Password Confirmation</Form.Label>
                    <Form.Control type="password" required onChange={e => setPasswordConfirm(e.target.value)} />
                    </Form.Group>
                    <Button disabled={loading} className="w-100" type="submit">Register</Button>
                </Form>
                </Card.Body>
            </Card>
            <div className="w-100 text-center mt-2">
                Already have an account? <Link to="/login">Log In</Link>
            </div>
        </div>
        </>
    );
    }

    
