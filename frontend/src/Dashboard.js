// create dashbaord component
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Row, Col, Carousel, Button, Stack } from 'react-bootstrap';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import './style/Dashboard.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-circular-progressbar/dist/styles.css';
// dashboard component
export default function Dashboard(props) {
    // state variables
    const [projects, setProjects] = useState([]);

    // nav hook
    const navigate = useNavigate();

    // handler to check if user is already logged in
    useEffect(() => {
        if (props.isLoggedIn == false) {
            navigate('/login');
        }
        // fetch user's projects
        // insert axios call to get user's projects from django backend
        // store in following format into projects via 'setProjects':
        // {id (int), name (string), description (string), successChance (int/100)}


    }, []);
    // function to calculate ring colour based on percentage
    const percentToColor = (percent) => {
        const x = percent / 100;
        const r = Math.min(2 - (2 * x), 1) * 255;
        const g = Math.min(2 * x, 1) * 255;
        return `rgba(${r}, ${g}, 100, 0.6)`;
    }

    return (
        <>  
            <div className='projectsContainer'>
                <div className='dashboardHeader'>
                    <span className='projectsTitle'>
                        <h1 >{props.user}'s Projects 📝</h1>
                        <div className='splitter'/>
                    </span>
                    <Button className='newProjectButton' variant='success' onClick={() => navigate('/dashboard/newproject')}>New Project</Button>
                </div>
                {projects.length != 0 ?
                    <Carousel variant="dark" className='projectsSlider'>
                        {
                            // map through projects and pair projects into rows of 2 if possible, otherwise put them in a row of 1
                            projects.map((project, index) => {
                                if (index % 2 == 0) {
                                    return (
                                        <Carousel.Item key={project.id}>
                                            <Row className="justify-content-md-center" xs={1} md={((index + 1) < projects.length) ? 2 : 1}>
                                                <Col md='auto'>
                                                    <Card className='project'>
                                                        <Card.Body>
                                                            <Card.Title className='projectName'>{project.name}</Card.Title>
                                                            <hr className='bt-3'/>
                                                            <Row md={2}>
                                                                <Col>
                                                                    {console.log(percentToColor(project.successChance))}
                                                                    <CircularProgressbar 
                                                                        styles={ buildStyles({
                                                                            pathColor: percentToColor(project.successChance),
                                                                            textColor: 'black'
                                                                        })
                                                                        } 
                                                                        value={project.successChance} text={`${project.successChance}%`} 
                                                                    />
                                                                    <p className='text-center m-0 fs-10'><i>Success Chance</i></p>
                                                                </Col>
                                                                <Col>
                                                                    <p>{project.description}</p>
                                                                    <Button variant='info' onClick={() => 
                                                                        navigate('/dashboard/projectview', {state: {projectId: project.id}})
                                                                    }>View Project</Button>
                                                                </Col>
                                                            </Row>
                                                        </Card.Body>
                                                    </Card>
                                                </Col>
                                                {/*Here we check if there is another project left, if so add to displayed pair.*/}
                                                {((index + 1) < projects.length) &&
                                                    <Col md='auto'>
                                                        <Card className='project'>
                                                            <Card.Body>
                                                                <Card.Title className='projectName'>{projects[index+1].name}</Card.Title>
                                                                <hr className='bt-3'></hr>
                                                                <Row md={2}>
                                                                    <Col>
                                                                    <CircularProgressbar 
                                                                        styles={ buildStyles({
                                                                            pathColor: percentToColor(projects[index+1].successChance),
                                                                            textColor: 'black'
                                                                        })
                                                                        } 
                                                                        value={projects[index+1].successChance} text={`${projects[index+1].successChance}%`} 
                                                                    />
                                                                        <p className='text-center m-0 fs-10'><i>Success Chance</i></p>
                                                                    </Col>
                                                                    <Col>
                                                                        <p>{projects[index+1].description}</p>
                                                                        <Button variant='info' onClick={() => 
                                                                            navigate('/dashboard/projectview', {state: {projectId: projects[index+1].id}})
                                                                        }>View Project</Button>
                                                                    </Col>
                                                                </Row>
                                                            </Card.Body>
                                                        </Card>
                                                    </Col>
                                                }
                                            </Row>  
                                        </Carousel.Item>
                                    );
                                }
                            })           
                        }
                    </Carousel>
                :
                    <div className='noProjects'>
                        <h1>You have no projects yet!</h1>
                        <Button variant='success' onClick={() => navigate('/dashboard/newproject')}>Make one now! 🖥️</Button>
                    </div>
                }
            </div>
        </>
    );
}