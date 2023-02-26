import { Navbar, Nav, Container } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style/NavBar.css';
// navbar component
export default function NavBar() {
    return (
        <Navbar bg="dark" variant="dark">
                <Container className='nav'>
                <Navbar.Brand href="#home">SofTrack</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/login">Login</Nav.Link>
                    <Nav.Link href="/register">Register</Nav.Link>
                    <Nav.Link href="/dashboard">Dashboard</Nav.Link>
                </Nav>
                </Container>
        </Navbar>
    );
}