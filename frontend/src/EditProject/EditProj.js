// component to create a new project for the user
import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Container, Row, Col, ListGroup } from 'react-bootstrap';
import { CSFs } from '../CreateProject/CSFs.js';
import ScoreCSFs from '../CreateProject/ScoreCSFs';
import Details from './Details';
import EditPage from './EditPage';

import '../style/CreateProj.css'
import 'bootstrap/dist/css/bootstrap.min.css';
// create project component
export default function CreateProj(props) {

    // nav hook
  const location = useLocation();
  const navigate = useNavigate();
  const CSF = CSFs
  // state variables
  const [currentPage, setCurrentPage] = useState(0);
  console.log("MEMBERS: " + location.projectMembers)
  const {projectName, projectDescription, projectMembers} = location.state;
  const [data, setData] = useState({name: projectName, description: projectDescription, CSFs: CSF, members: projectMembers});
  const pageTitles = ["Edit", "CSFs", "Name and Description"];

  // handler to check if user is already logged in
  useEffect(() => {
    if (props.isLoggedIn == false) {
        navigate('/login');
    }
  }, []);

  // handler to create project
  const updateProject = () => {
    // insert axios call to create project in django backend
    // navigate to dashboard
    navigate(-1);
  }
  // page to welcome the user and ask them to create a project

  const goBack = (newData) => {
    setCurrentPage(0);
    console.log(newData.members)
    setData((prevData) => ({...prevData, ...newData}));
    }

  const setPage = (page) => {
    setCurrentPage(page);
  }

  let page;
  switch(currentPage) {
    case 0:
      page = <EditPage handleSubmit={updateProject} setPage={setPage} data={data}/>;
      break;
    case 1:
      page = <ScoreCSFs handleNext={goBack} data={data}/>;
      break;
    case 2:
      page = <Details handleNext={goBack} data={data}/>;
      break;
    default:
      break;
  }
  return(
    <>
      <Container className='formContainer'>
        <h1 className='createTitle'>Editing Project 🎬</h1>
        <h2 className='createSubTitle'>{pageTitles[currentPage]}</h2>
        <Row className="innerContainer">
          <Col sm={12}>
            {page}
          </Col>
        </Row>
      </Container>
    </>
  )
}
                        
    
    
    
    
    
