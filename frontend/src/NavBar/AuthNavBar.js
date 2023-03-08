import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Nav, Navbar } from 'react-bootstrap';
import '../style/NavBar.css';
// navbar component
export default function AuthNavBar() {
    return (
        <Navbar className='navbar' bg="dark" variant="dark">
            <Container className='nav'>
                <Navbar.Brand>SofTrack</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/dashboard">Dashboard</Nav.Link>
                    <Nav.Link href="/logout">Logout</Nav.Link>
                </Nav>
            </Container>
            <Navbar.Collapse className="justify-content-end">
                <Navbar.Text>
                    Signed in as: <b>Placeholder</b>
                </Navbar.Text>
            </Navbar.Collapse>
        </Navbar>
    );
}
