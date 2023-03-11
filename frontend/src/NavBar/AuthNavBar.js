import { Navbar, Nav, Container } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/NavBar.css';
// navbar component
export default function AuthNavBar(props) {
    return (
        <Navbar className='navbar' bg="dark" variant="dark">
            <Container className='nav'>
                <Navbar.Brand>SofTrack</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link onClick={() => props.setFetchProjects(true)} href="/dashboard">Dashboard</Nav.Link>
                    <Nav.Link href="/logout">Logout</Nav.Link>
                </Nav>
            </Container>
            <Navbar.Collapse className="justify-content-end">
                <Navbar.Text>
                    Signed in as: <b>{props.user}</b>
                </Navbar.Text>
            </Navbar.Collapse>
        </Navbar>
    );
}