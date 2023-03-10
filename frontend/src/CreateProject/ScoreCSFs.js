import React, { useState } from "react";
import { Form, Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";


export default function ScoreCSFs({handleNext, data}) {
    const [CSFs, setCSFs] = useState(data.CSFs);
    const [JSONCSFs, setJSONCSFs] = useState(data.JSONCSFs);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [show, setShow] = useState(true);
    // mapping score to human answers
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
    // called when a radio check is clicked
    const handleScoreSelect = (event) => {
        const { value } = event.target;
        console.log(value);
        // update the CSF and JSONCSFs results after every answer.

        //temp variables
        const tempCSFs = CSFs;
        const tempname = CSFs[currentIndex].name;
        const tempscore = CSFs[currentIndex].score;
        console.log("Current CSF Name " + tempname);
        console.log("Current CSF Score " + tempscore);
        const tempJSONCSFs = JSONCSFs;
        console.log("Current JSONCSF Score " + tempJSONCSFs[tempname]);

        //set CSF to score inputted in temp JSONCSF and CSF
        tempJSONCSFs[tempname] = parseInt(value);
        console.log("Updated JSONCSF score " + JSONCSFs[tempname]);
        tempCSFs[currentIndex].score = value;
        console.log("Updated CSF Score " + value);

        //Update original values
        setCSFs(tempCSFs);
        setJSONCSFs(tempJSONCSFs);

        // toggle fade to show next question
        setShow(false);
        event.target.checked = false;
    };

    const handleFade = () => {
        // after fade is complete, go to next question
        if(!show) {
            setCurrentIndex((prev) => prev + 1); 
            if(currentIndex === CSFs.length - 1) {
                handleNext(CSFs);
            }
        }
        // fade next one back in
        setShow(true);
    };

    const renderScoreForm = () => {
        // get current question and description
        const question = CSFs[currentIndex].question;
        const description = CSFs[currentIndex].description;
        return (
        <Form >
            {/* make radio buttons form  */}
            <Form.Group 
                controlId="formBasicRadio"
                className={`fade ${show ? "show" : ""}`}
                onTransitionEnd={handleFade}
            >
                {/* do some design cssery */}
            <Row sm='auto' className="justify-content-md-center">
                <Col sm={12}>
                    <h2 className="text-center">{description}</h2>
                    <hr/>
                    <h3 className="text-center">{question}</h3>
                    <Container>
                        {/* make each of the radio button by mapping 1-4 */}
                        <Row className="radios">
                            {[1, 2, 3, 4].map((score) => (
                                <Col 
                                    sm={3} // colour based on label
                                    style={{padding: '0.5%',backgroundColor: colourMap[score]}}
                                    onClick={() => { // allows the background to be clicked instead of just the radio button
                                        const radioBtn = document.getElementById(`score-${score}`);
                                        radioBtn.click();
                                    }}
                                >   
                                    <Form.Check inline 
                                        type="radio"
                                        label={scoreLabels[score]}
                                        name={question}
                                        value={score}
                                        onChange={handleScoreSelect} // when clicked, update the score
                                        id={`score-${score}`}
                                        key={score}
                                    />
                                </Col>
                            ))}
                        </Row>
                    </Container>
                </Col>
            </Row>
            </Form.Group>
        </Form>
        );
    };
    
    return (
        <Container className="my-5">
            <Row>
                <Col>
                {/* render selected question and when it updates will re render */}
                    {renderScoreForm()} 
                </Col>
            </Row>
            
        </Container>
    );
}
