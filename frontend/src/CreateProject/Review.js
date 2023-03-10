// page to review the user's answers
//
import React, { useState, useEffect } from 'react';
import { Button, Row, Col, Card, Container, Accordion, Table, ListGroup } from 'react-bootstrap';
import { IoCreateOutline } from 'react-icons/io5';
import 'bootstrap/dist/css/bootstrap.min.css';
// create project component
export default function Review({handleSubmit, setPage, data}) {
    const [name, setName] = useState(data.name);
    const [description, setDescription] = useState(data.description);
    const [members, setMembers] = useState(data.members);
    const [CSFs, setCSFs] = useState(data.CSFs);

    const scoreLabels = {
        1: "Poor",
        2: "Below Average",
        3: "Above Average",
        4: "Excellent",
    };
    const colourMap = {
        1: "rgb(255, 0, 0, 0.5)",
        2: "rgb(255, 255, 0, 0.5)",
        3: "rgb(0, 255, 0, 0.5)",
        4: "rgb(0, 255, 255, 0.5)",
    }

    return (
        <Container>
            <Row sm={3}>
                <Col>
                    <Card style={{borderColor: '#9D231B'}}>
                        <Card.Title>
                            <h1 className='text-center'>Description</h1>
                        </Card.Title>
                        <Card.Body className='text-center' style={{fontSize: '20px'}}>
                            {description}
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card style={{borderColor: '#9D231B'}}>
                        <Card.Title>
                            <h1 className='text-center'>Title</h1>
                        </Card.Title>
                        <Card.Body style={{fontSize: '20px'}} className='text-center'>
                            {name}
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card style={{borderColor: '#9D231B'}}>
                        <Card.Title>
                            <h1 className='text-center'>Members</h1>
                        </Card.Title>
                        <Card.Body>
                            <ListGroup>
                                {members.map((member, index) => {
                                    return (
                                        <ListGroup.Item key={index}>{member}</ListGroup.Item>
                                    )
                                })}
                            </ListGroup>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
            <Row className='d-flex justify'>
                <Col sm = {4}/>
                <Col>
                    <Button className='editButton' onClick={() => setPage(0)}>Edit</Button>
                </Col>
                <Col sm = {4}/>
            </Row>
            <hr />
            <h2 className='tm-4 mb-4'>Critical Success Factors:</h2>
            <Accordion>
                <Accordion.Item key={0}>
                <Accordion.Header>Organizational Factors</Accordion.Header>
                    <Accordion.Body>
                        <Table striped>
                            <thead>
                                <tr>
                                    <th>CSF</th>
                                    <th>Score</th>
                                </tr>
                            </thead>
                            <tbody>
                                {CSFs.map((csf, index) => {
                                    if(index < 6){
                                        return (
                                            <tr>
                                                <td>{csf.question}</td>
                                                <td style={{backgroundColor: colourMap[csf.score]}}>{scoreLabels[csf.score]}</td>
                                            </tr>
                                        )
                                    }
                                })}
                            </tbody>
                        </Table>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item key={1}>
                <Accordion.Header>Team Factors</Accordion.Header>
                    <Accordion.Body>
                        <Table striped>
                            <thead>
                                <tr>
                                    <th>CSF</th>
                                    <th>Score</th>
                                </tr>
                            </thead>
                            <tbody>
                                {CSFs.map((csf, index) => {
                                    if(index >= 6 && index < 13){
                                        return (
                                            <tr>
                                                <td>{csf.question}</td>
                                                <td style={{backgroundColor: colourMap[csf.score]}}>{scoreLabels[csf.score]}</td>   
                                            </tr>
                                        )
                                    }
                                })}
                            </tbody>
                        </Table>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item key={2}>
                <Accordion.Header>Customer Factors</Accordion.Header>
                    <Accordion.Body>
                        <Table striped>
                            <thead>
                                <tr>
                                    <th>CSF</th>
                                    <th>Score</th>
                                </tr>
                            </thead>
                            <tbody>
                                {CSFs.map((csf, index) => {
                                    if(index >= 13 && index < 17){
                                        return (
                                            <tr>
                                                <td>{csf.question}</td>
                                                <td style={{backgroundColor: colourMap[csf.score]}}>{scoreLabels[csf.score]}</td>  
                                            </tr>
                                        )
                                    }
                                })}
                            </tbody>
                        </Table>
                    </Accordion.Body>
                </Accordion.Item >
                <Accordion.Item key={3}>
                <Accordion.Header>Project Factors</Accordion.Header>
                    <Accordion.Body>
                        <Table striped>
                            <thead>
                                <tr>
                                    <th>CSF</th>
                                    <th>Score</th>
                                </tr>
                            </thead>
                            <tbody>
                                {CSFs.map((csf, index) => {
                                        if(index >= 17 && index < 24){
                                            return (
                                                <tr>
                                                    <td>{csf.question}</td>
                                                    <td style={{backgroundColor: colourMap[csf.score]}}>{scoreLabels[csf.score]}</td>
                                                </tr>
                                            )
                                        }
                                    })}
                            </tbody>
                        </Table>
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
            <Row>
                <Col sm={4}/>
                <Col>
                    <Button className='editButton' onClick={() => setPage(1)}>Redo CSFs</Button>
                </Col>
                <Col sm={4}/>
            </Row>
            <hr />
            <Row>
                <Col sm={3}/>
                <Col>
                    <Button className='editButton' onClick={handleSubmit} variant='success'>Create Project {IoCreateOutline}</Button>
                </Col>
                <Col sm={3}/>
            </Row>
        </Container>
    )
}