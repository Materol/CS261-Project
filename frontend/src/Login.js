import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Login.css'
// import { useAuth } from './AuthContext';
import { Link } from 'react-router-dom';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

// login function component
export default function Login() {
    // state variables
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    // nav hook
    const navigate = useNavigate();
    // useAuth hook
    // const { login } = useAuth();
    // event handlers
    async function handleSubmit(e) {
        e.preventDefault();
        try {
        setError('');
        setLoading(true);
        // await login(email, password);
        // navigate('/');
        } catch {
            setError('Failed to log in');
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

