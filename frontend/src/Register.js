// necessary imports
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Register.css'
// import { useAuth } from './AuthContext';
import { Link } from 'react-router-dom';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

// register function component
export default function Register(props) {
    // state variables
    const [email, setEmail] = useState('');
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

    async function handleSubmit(e) {
        e.preventDefault();
        // password check
        if (password !== passwordConfirm) {
            return setError('Passwords do not match');
        }

        try {
            setError('');
            setLoading(true);

            // insert axios call to register in django backend, 
            // if successful, navigate to dashboard otherwise show error
            
            props.setIsLoggedIn(true);
        } catch {
            setError('Failed to create an account');
        }
        setLoading(false);
    }
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