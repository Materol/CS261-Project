// create dashbaord component
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from 'react';
import { Card } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
// dashboard component
export default function Dashboard(props) {
    // state variables
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    // nav hook
    const navigate = useNavigate();
    // useAuth hook

    // handler to check if user is already logged in
    useEffect(() => {
        if (props.isLoggedIn == false) {
            navigate('/login');
        }
    }, []);

    return (
        <>
            <div className='dashboardCard'>
                <Card>
                    <Card.Body>
                    <h2 className="text-center mb-4">Dashboard</h2>
                    </Card.Body>
                </Card>
            </div>
        </>
    );
}
