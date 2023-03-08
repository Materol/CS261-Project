import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Nav, Navbar } from 'react-bootstrap';

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
