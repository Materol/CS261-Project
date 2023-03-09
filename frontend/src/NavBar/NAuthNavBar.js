import { Navbar, Nav, Container } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

// navbar component
export default function NoAuthNavBar() {
    return (
        <Navbar className='navbar' bg="dark" variant="dark">
            <Container className='nav'>
                <Navbar.Brand>SofTrack</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/login">Login</Nav.Link>
                    <Nav.Link href="/register">Register</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );
}