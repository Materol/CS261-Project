import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Login.css'
import { Link } from 'react-router-dom';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

// login function component
export default function Login(props) {
    // state variables
    const [email, setEmail] = useState('');
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
    // handle login request
    async function handleSubmit(e) {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            setError('');
            setLoading(true);

            // insert axios call to login in django backend, if successful, navigate to dashboard otherwise show error
            // also, change the state of isLoggedIn to true
            
            props.setIsLoggedIn(true);
        } catch {
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
                    <Form.Control type="email" required onChange={e => setEmail(e.target.value)} />
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
            <Button onClick={() => {props.setIsLoggedIn(!props.isLoggedIn); navigate('/dashboard');}}>Debug Login</Button>
        </div>
        </>
    );
    }

