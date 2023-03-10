// component to view details of individual project
import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { percentToColor, getSuccessSplit } from './Utils';
import { CircularProgressbar, buildStyles} from 'react-circular-progressbar';
import {IoMdArrowRoundBack, IoMdInformationCircleOutline} from 'react-icons/io';
import { Button, Container, Row, Col, Card, ListGroup, ProgressBar, Accordion, Table, OverlayTrigger, Tooltip, Popover, Pagination} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style/ProjectView.css';

//import axios to use backend data
import axiosInstance from './axiosApi';

// component to view details of individual project
export default function ProjectView(props) {
    
    const navigate = useNavigate();
    const location = useLocation();
    const { projectId, projectName, projectDescription } = location.state;
    const[members, setMembers] = useState(['John', 'Jane', 'Joe']);
    const [metrics, setMetrics] = useState([]);
    const [activeMetric, setActiveMetric] = useState(0);
    const [processM, setProcessM] = useState([[]]);
    const [productM, setProductM] = useState([[]]);
    const [stakeHolderM, setStakeHolderM] = useState([[]]);
    const [overallM, setOverallM] = useState();
    const [processSplit, setProcessSplit] = useState([]);
    const [productSplit, setProductSplit] = useState([]);
    const [stakeHolderSplit, setStakeHolderSplit] = useState([]);
    const [generalFeedback, setGeneralFeedback] = useState("Placeholder");
    let paginationItems = [];

    useEffect(() => {
        if (props.isLoggedIn == false) {
            navigate('/login');
        }

        // insert axios call to get project details using 'id'
        // store in following format into projects via 'setProject':
        // {name: (string), description: (string), generalFeedback: (string), metricHistory: [[{MetricDescription: (string), MetricScore: (float), Feedback: (string)}]], members: [MemberName (string)]}
        // (see below for how there's 2 lists of metrics for each. It should be in ascending order of age)
        // e.g. [0] is oldest, [-1] is newest. Means you can just .push updates to the 'history' list.
        // then they can be split up, first 4 are process, next 10 are product and last 3 are stakeholder.


        //TODO: Format returned project data and set in projects

        //Get project details from backend
        axiosInstance.get('projects/detail/' + projectId).then((res) => {
			console.log(res.data);
		});


        setProcessM([
            [{MetricDescription: 'Metric 1', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 3', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 4', MetricScore: 3.5, Feedback: 'Placeholder'}],
            [{MetricDescription: 'Metric 4', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 3', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 1', MetricScore: 3.5, Feedback: 'Placeholder'}],
        ]);
        setProductM([
            [{MetricDescription: 'Metric 1', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 3', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 4', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 5', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 6', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 7', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 8', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 9', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 10', MetricScore: 3.5, Feedback: 'Placeholder'}],
            [{MetricDescription: 'Metric 10', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 9', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 8', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 7', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 6', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 5', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 4', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 3', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 2.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 1', MetricScore: 3.5, Feedback: 'Placeholder'}]
        ]);
        setStakeHolderM([
            [{MetricDescription: 'Metric 1', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 3', MetricScore: 2.5, Feedback: 'Placeholder'}],
            [{MetricDescription: 'Metric 3', MetricScore: 3.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 2', MetricScore: 4.5, Feedback: 'Placeholder'},
            {MetricDescription: 'Metric 1', MetricScore: 2.5, Feedback: 'Placeholder'}]
        ]);
        setOverallM(40);
    }, []);

    useEffect(() => {
        setProcessSplit(getSuccessSplit(processM));
    }, [processM]);
      
    useEffect(() => {
        setProductSplit(getSuccessSplit(productM));
    }, [productM]);
    
    useEffect(() => {
        setStakeHolderSplit(getSuccessSplit(stakeHolderM));
    }, [stakeHolderM]);

    const renderTooltip = (props) => {
        return (<Tooltip id="button-tooltip" {...props}>
            Green represent a high (3.5-5) score, yellow represents a medium (2.5-3.5) score, and red represents a low (1-2.5) score.
        </Tooltip>
        )
    };

    const renderHistoryTip = (props) => {
        return (<Tooltip id="button-tooltip" {...props}>
            Browse through the metric history to see the progress of the project. The higher the number, the older the metrics.
        </Tooltip>
        )
    };

    const deletePopover = (
        <Popover id="popover-delete">
          <Popover.Header as="h3">Are you sure?</Popover.Header>
          <Popover.Body>
            Once you delete the project, it's <strong>gone forever!</strong>.
            <Button className='editProj' variant='danger' onClick={() => navigate('/dashboard/project/delete', {state: {id: projectId}})}>Yes I am sure, delete project.</Button>
          </Popover.Body>
        </Popover>
    );
    const len = processM.length-1;
    paginationItems.push(
        <Pagination.Item key={len} active={activeMetric === 0} onClick={() => setActiveMetric(0)}>
            Latest
        </Pagination.Item>
    );
    for (let i = processM.length-2; i >=0; i--) {
        paginationItems.push(
            <Pagination.Item key={i} active={activeMetric == len - i} onClick={() => setActiveMetric(len - i)}>
                {len - i}
            </Pagination.Item>
        );
    }

    return (
        <>
            <Container className='projectViewHeader'>
                <Row className='justify-content-md-between' sm='auto'>
                    <Col sm={4}>
                        <Button className='backButton' variant='secondary' onClick={() => navigate(-1)}><IoMdArrowRoundBack size={35}/></Button>
                        <Col className='sections'>
                            <span className='projectTitle'>
                                <h1>{projectName} 🚀</h1>
                                <Button className='editProj' variant='success' onClick={() => navigate('/dashboard/project/edit', 
                                                                                                        { state: { 
                                                                                                            projectId: projectId,
                                                                                                            projectName: projectName,
                                                                                                            projectDescription: projectDescription,
                                                                                                            projectMembers: members
                                                                                                        }})}>Edit Project</Button>
                                <OverlayTrigger rootClose='true' trigger="click" placement="right" overlay={deletePopover}>
                                    <Button className='editProj' variant='danger'>Delete Project</Button>
                                </OverlayTrigger>
                            </span>
                        </Col>
                    </Col>
                    
                    <Col className='sections' sm={8}>
                        <h3>Project Details 📑</h3>
                        <hr />
                        <Row>
                            <Col sm={5}>
                                <Card style={{borderColor: '#9D231B'}}>
                                    <Card.Body>
                                        <Card.Title>Description</Card.Title>
                                        <Card.Text style={{fontSize: '20px'}}>
                                            {projectDescription}
                                        </Card.Text>
                                    </Card.Body>
                                </Card>
                            </Col>
                            <Col>
                                <Card style={{borderColor: '#9D231B'}}>
                                    <Card.Body>
                                        <Card.Title>Members</Card.Title>
                                        <Row>
                                            <Col>
                                                <ListGroup style={{fontSize: '20px'}}>
                                                    {
                                                        members.map((member, index) => {
                                                            return (
                                                                <>
                                                                    { (index <= (members.length/2)) &&
                                                                    <ListGroup.Item key={index}>{member}</ListGroup.Item>
                                                                    }
                                                                </>
                                                            );
                                                        })
                                                    }
                                                </ListGroup>
                                            </Col>
                                            <Col>
                                                <ListGroup style={{fontSize: '20px'}}>
                                                    {
                                                        members.map((member, index) => {
                                                            return (
                                                                <>
                                                                    { (index > (members.length/2)) &&
                                                                    <ListGroup.Item key={index}>{member}</ListGroup.Item>
                                                                    }
                                                                </>
                                                            );
                                                        })
                                                    }
                                                </ListGroup>
                                            </Col>
                                        </Row>
                                    </Card.Body>
                                </Card>
                            </Col>
                        </Row>
                    </Col>
                </Row>
                <Row className='mt-4'>
                    <Container className='sections'>
                        <h3>Metrics 📈</h3>
                        <hr />
                        <Row>
                            <Col xs={4}>
                                <Card style={{borderColor: '#9D231B'}}>
                                    <Card.Body>
                                        <CircularProgressbar
                                            styles={buildStyles({
                                                pathColor: percentToColor(overallM),
                                                textColor: 'black'
                                            })
                                            }
                                            value={overallM} text={`${overallM}%`}
                                        />
                                    </Card.Body>
                                    <Card.Footer>
                                        <small className="text-muted">Overall Success Chance</small>
                                    </Card.Footer>
                                </Card>
                            </Col>
                            <Col style={{position: 'relative'}}>
                                <OverlayTrigger
                                    placement='top'
                                    delay={{ show: 250, hide: 400 }}
                                    overlay={renderTooltip}
                                >
                                    <div style={{position: 'absolute', top: 0, right: 0}}>
                                        <IoMdInformationCircleOutline size={32} style={{position: 'absolute', top: 0, right: 0}}/>
                                    </div>
                                </OverlayTrigger>
                                
                                <h2>Process Metrics</h2>
                                <ProgressBar className="mb-4">
                                    <ProgressBar variant="success" now={processSplit[2]} key={1} />
                                    <ProgressBar variant="warning" now={processSplit[1]} key={2} />
                                    <ProgressBar variant="danger" now={processSplit[0]} key={3} />
                                </ProgressBar>
                                <h2>Product Metrics</h2>
                                <ProgressBar className="mb-4">
                                    <ProgressBar variant="success" now={productSplit[2]} key={1} />
                                    <ProgressBar variant="warning" now={productSplit[1]} key={2} />
                                    <ProgressBar variant="danger" now={productSplit[0]} key={3} />
                                </ProgressBar>
                                <h2>Stakeholder Metrics</h2>
                                <ProgressBar className="mb-4">
                                    <ProgressBar variant="success" now={stakeHolderSplit[2]} key={1} />
                                    <ProgressBar variant="warning" now={stakeHolderSplit[1]} key={2} />
                                    <ProgressBar variant="danger" now={stakeHolderSplit[0]} key={3} />
                                </ProgressBar>
                                <Card>
                                    <Card.Body>
                                        <Card.Title>Feedback</Card.Title>
                                        <Card.Text style={{fontSize: '20px'}}>
                                            {generalFeedback}
                                        </Card.Text>
                                    </Card.Body>
                                </Card>
                            </Col>
                        </Row>
                        <Row className="mt-3">
                        <Col>
                            <h3 className='mt-3'>Metrics Breakdown 🔎</h3>
                            <hr/>
                            <Row sm='auto'>
                                <Col>
                                    <div className="d-flex justify-content-between align-items-center">
                                        <Pagination>
                                            {paginationItems}
                                        </Pagination>
                                        <OverlayTrigger
                                            placement='top'
                                            delay={{ show: 250, hide: 400 }}
                                            overlay={renderHistoryTip}
                                            >
                                            <div>
                                                <IoMdInformationCircleOutline className='align-self-center' size={32}/>
                                            </div>
                                        </OverlayTrigger>
                                    </div>
                                </Col>
                            </Row>
                            
                            <Accordion alwaysOpen flush>
                            {[
                                { metrics: processM[activeMetric], header: 'Process Metrics' },
                                { metrics: productM[activeMetric], header: 'Product Metrics' },
                                { metrics: stakeHolderM[activeMetric], header: 'Stakeholder Metrics' }
                            ].map(({ metrics, header }, index) => (
                                <Accordion.Item key={index} eventKey={index.toString()}>
                                <Accordion.Header>{header}</Accordion.Header>
                                <Accordion.Body>    
                                    <Table size='sm' className='tables' striped bordered>
                                        <thead>
                                            <tr>
                                                <th>Description</th>
                                                <th>Metric Score</th>
                                                <th>Feedback</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {metrics.map((metric, index) => (
                                            <tr key={index} style={{ backgroundColor: (metric.MetricScore!=0) && percentToColor(((metric.MetricScore-1)/4)*100)}}>
                                                <td>{metric.MetricDescription}</td>
                                                <td>{metric.MetricScore}</td>
                                                <td>{metric.Feedback}</td>
                                            </tr>
                                            ))}
                                        </tbody>
                                    </Table>
                                </Accordion.Body>
                                </Accordion.Item>
                            ))}
                            </Accordion>
                        </Col>
                    </Row>
                    </ Container>
                </Row>
            </Container>
        </>
    )
}


                                
