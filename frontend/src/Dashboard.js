// create dashbaord component
import 'bootstrap/dist/css/bootstrap.min.css';
import { useEffect, useState } from 'react';
import { Button, Card, Carousel, Col, Row, Spinner } from 'react-bootstrap';
import { buildStyles, CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { useNavigate } from 'react-router-dom';
import './style/Dashboard.css';
import { percentToColor } from './Utils';
// dashboard component

//import axios to use backend data
import axiosInstance from './axiosApi';



export default function Dashboard(props) {
    // state variables
    const [projects, setProjects] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    // nav hook
    const navigate = useNavigate();

    // handler to check if user is already logged in
    useEffect(() => {
        if (props.isLoggedIn == false) {
            navigate('/login');
        }
        console.log("Token: " + localStorage.getItem('access_token'));
        // fetch user's projects using their token (localStorage.getItem('access_token'))
        // insert axios call to get user's projects from django backend
        // store in following format into projects via 'setProjects':
        // {id (int), name (string), description (string), successChance (int/100)}

        //Get projects from backend and format to frontend values
        if(props.fetchProjects == true){
            axiosInstance.get('/projects/' + props.email).then((res) => {
                console.log("res.data:" + res.data)
                //array of all project objects returned
                const allProjects = res.data;

                //temp values
                let tempProject = {id:0, name: "", description:"", successChance:0};
                const tempProjects = []

                //Iterate through each project and get the data needed for front-end
                allProjects.forEach(myFunction);

                function myFunction(item){
                    console.log("item: " + item);
                    const overall = ((item.currentMetric.overall_success/5) * 100).toFixed(1);
                    tempProject = {id: item.id, name: item.name, description: item.description, successChance: overall};
                    tempProjects.push(tempProject)
                }
                console.log("tempProjects:")
                console.log(tempProjects);
                //Set dashboard projects to projects returned
                setProjects(tempProjects);
                setIsLoading(false);
		    });
            props.setFetchProjects(false);
        }
    }, [props.fetchProjects]);

    if (isLoading) {
        return(
            <div className='projectsContainer'>
                <div className='dashboardHeader'>
                    <span className='projectsTitle'>
                        <h1 >{props.user}'s Projects 📝</h1>
                        <div className='splitter'/>
                    </span>
                    <Button className='newProjectButton' variant='success' onClick={() => navigate('/dashboard/createproject')}>New Project</Button>
                </div>
                <div className='projectsSlider'>
                    <Row md='auto' className='justify-content-md-center'>
                        <Col><Spinner size="lg" animation="grow" />;</Col>
                    </Row>
                </div>
            </div>
        )
    }
    return (
        <>
            <div className='projectsContainer'>
                <div className='dashboardHeader'>
                    <span className='projectsTitle'>
                        <h1 >{props.user}'s Projects 📝</h1>
                        <div className='splitter'/>
                    </span>
                    <Button className='newProjectButton' variant='success' onClick={() => navigate('/dashboard/createproject')}>New Project</Button>
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
                                                            <hr className='bt-3' />
                                                            <Row md={2}>
                                                                <Col>
                                                                    <CircularProgressbar
                                                                        styles={buildStyles({
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
                                                                        navigate('/dashboard/project',
                                                                        { state: {
                                                                            projectId: project.id,
                                                                            projectName: project.name,
                                                                            projectDescription: project.description,
                                                                        }})
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
                                                                <Card.Title className='projectName'>{projects[index + 1].name}</Card.Title>
                                                                <hr className='bt-3'></hr>
                                                                <Row md={2}>
                                                                    <Col>
                                                                        <CircularProgressbar
                                                                            styles={buildStyles({
                                                                                pathColor: percentToColor(projects[index + 1].successChance),
                                                                                textColor: 'black'
                                                                            })
                                                                            }
                                                                            value={projects[index + 1].successChance}
                                                                            text={`${projects[index + 1].successChance}%`}
                                                                        />
                                                                        <p className='text-center m-0 fs-10'><i>Success Chance</i></p>
                                                                    </Col>
                                                                    <Col>
                                                                        <p>{projects[index + 1].description}</p>
                                                                        <Button variant='info' onClick={() =>
                                                                            navigate('/dashboard/project',
                                                                            { state: {
                                                                                projectId: projects[index + 1].id,
                                                                                projectName: projects[index + 1].name,
                                                                                projectDescription: projects[index + 1].description,
                                                                            }})
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
                        <Button variant='success' onClick={() => navigate('/dashboard/createproject')}>Make one now! 🖥️</Button>
                    </div>
                }
            </div>
        </>
    );
}
