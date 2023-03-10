// component to create a new project for the user
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Row, Col, ListGroup } from 'react-bootstrap';
import { CSFs } from './CSFs.js';
import { JSONCSFs } from './JSONCSFs.js';
import NameAndDetails from './NameAndDetails';
import ScoreCSFs from './ScoreCSFs';
import Review from './Review';


//import axios to use backend data
import axiosInstance from '../axiosApi';


import '../style/CreateProj.css'
import 'bootstrap/dist/css/bootstrap.min.css';
// create project component
export default function CreateProj(props) {
  // state variables
  const [currentPage, setCurrentPage] = useState(0);
  const [data, setData] = useState({name: '', description: '', CSFs: CSFs, JSONCSFs: JSONCSFs, members: []});
  const [review, setReview] = useState(false);

  const pageTitles = ["Name and Description", "CSFs", "Review"];

  // nav hook
  const navigate = useNavigate();

  // handler to check if user is already logged in
  useEffect(() => {
    if (props.isLoggedIn == false) {
        navigate('/login');
    }
  }, []);

  
  //Create new project and post to backend (projects/create) then navigate to dashboard
	const createProject = (e) => {
		e.preventDefault();


		axiosInstance
			.post(`projects/create/`, {
				name: data.name,
				description: data.description,
				CSFs: data.JSONCSFs,
				members: {"members":data.members},
			})
			.then((res) => {
				navigate('/dashboard');
			});
	};

  //}
  // page to welcome the user and ask them to create a project

  const handleNext = (newData) => {
    if(currentPage==1) setReview(true);
    if(!review) setCurrentPage((prevPage) => prevPage + 1);
    else setCurrentPage(2);
    setData((prevData) => ({...prevData, ...newData}));
  }

  const setPage = (page) => {
    setCurrentPage(page);
  }

  let page;
  switch(currentPage) {
    case 0:
      page = <NameAndDetails handleNext={handleNext} data={data} review={review}/>;
      break;
    case 1:
      page = <ScoreCSFs handleNext={handleNext} data={data}/>;
      break;
    case 2:
      page = <Review handleSubmit={createProject} data={data} setPage={setPage}/>;
      break;
    default:
      break;
  }
  return(
    <>
      <Container className='formContainer'>
        <h1 className='createTitle'>Project Creation ✍</h1>
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
                        
    
    
    
    
    
