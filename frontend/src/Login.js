import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Login.css'
import { Link } from 'react-router-dom';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


//import axios to use backend data
import axiosInstance from './axiosApi';


// login function component
export default function Login(props) {
    // state variables
    // const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    // check to see if logged in
    useEffect(() => {
        if (props.isLoggedIn) {
            navigate('/dashboard');
        }
    }, [navigate]);

  //On submit it gives the tokens to the user for auth purposes
	const handleSubmit = (e) => {
        e.preventDefault();
        try {
            axiosInstance
            .post(`token/`, {
                email: props.email,
                password: password,
            })
            //Storing tokens locally for auth
            .then((res) => {
                localStorage.setItem('access_token', res.data.access);
                localStorage.setItem('refresh_token', res.data.refresh);
                //Send across access token for auth
                axiosInstance.defaults.headers['Authorization'] = 'JWT ' + localStorage.getItem('access_token');
                //If good, navigate to dashboard
                //navigate('/dashboard');
                props.setIsLoggedIn(true);
                props.setUser(username);
                //If good, navigate to dashboard
                props.setFetchProjects(true);
                navigate('/dashboard');
            });
        } catch {
            console.log("Error");
            setError('Password and Email did not match');
        }
        setLoading(false);
    }

    return (
        <>
        <div className='loginCard'>
            <Card>
                <Card.Body>
                <h2 className="text-center mb-4">Log In</h2>
                {error && <Alert variant="danger">{error}</Alert>}
                <Form onSubmit={handleSubmit}>
                    <Form.Group id="email">
                    <Form.Label className='lEmailLabel'>Email</Form.Label>
                    <Form.Control type="email" required onChange={e => props.setEmail(e.target.value)} />
                    </Form.Group>
                    <Form.Group id="username">
                    <Form.Label className='rUsernameLabel'>Username</Form.Label>
                    <Form.Control type="text" required onChange={e => setUsername(e.target.value)} />
                    </Form.Group>
                    <Form.Group id="password">
                    <Form.Label className='lPasswordLabel'>Password</Form.Label>
                    <Form.Control type="password" required onChange={e => setPassword(e.target.value)} />
                    </Form.Group>
                    <Button disabled={loading} className="w-100" type="submit">Log In</Button>
                </Form>
                <p hidden={error==''}>{error}</p>
                <div className="w-100 text-center mt-3">
                    <Link to="/forgot-password">Forgot Password?</Link>
                </div>
                </Card.Body>
            </Card>
            <div className="w-100 text-center mt-2">
                Need an account? <Link to="/register">Register</Link>
            </div>
        </div>
        </>
    );
    }
