// page to get the project's name and description
//
import React, { useState } from 'react';
import { Form, Button, Row, Col, Container, ListGroup} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
// create project component
export default function NameAndDetails({handleNext, data, review}) {
    const [name, setName] = useState(data.name);
    const [description, setDescription] = useState(data.description);
    const [members, setMembers] = useState(data.members);  

    const submit = (e) => {
        e.preventDefault();
        handleNext({name, description, members});
    }

    const handleRemove = (index) => {
        const newMembers = [...members];
        newMembers.splice(index, 1);
        setMembers(newMembers);
    }
    
    const handleAdd = () => {
        const newMember = document.getElementById('member').value ;
        if(newMember!==''){
            setMembers([...members, newMember]);
            document.getElementById('member').value ='';
        }
    }

    return(
        <Container>
            <Row>
                <Col>
                    <Form onSubmit={submit}>
                        <Form.Group controlId="formName">
                            {!review && <h2>Let's get started...</h2>}
                            <Form.Label className="mt-2">Project Name</Form.Label>
                            <Form.Control required type="text" placeholder="Enter project name" value={name} onChange={(e) => setName(e.target.value)} />
                        </Form.Group>
                        <Form.Group controlId="formDescription">
                            <Form.Label className="mt-2">Project Description</Form.Label>
                            <Form.Control required as="textarea" placeholder="Describe the project in a few words." 
                                rows={3} 
                                value={description} 
                                onChange={(e) => setDescription(e.target.value)}
                            />
                        <hr/>
                        </Form.Group>
                            <h2>Add Members</h2>
                            <Form.Group>
                            <Form.Control id='member' type="text" name="member" placeholder="Enter a member name" />
                            </Form.Group>
                            <Button className='mt-3' variant="success" onClick={() => handleAdd()}>Add Member</Button>
                            <hr/>
                            <ListGroup>
                                {members.map((member, index) => (
                                <ListGroup.Item key={index}>
                                    <Row sm='auto'>
                                        <Col>
                                            {member}
                                        </Col>
                                        <Col>
                                            <Button variant="danger" size="sm" onClick={() => handleRemove(index)}>Remove</Button>
                                        </Col>
                                    </Row>
                                </ListGroup.Item>
                                ))}
                            </ListGroup>
                        <Button className="mt-3" type="submit">Next</Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    );
}

