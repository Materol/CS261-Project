// component to view details of individual project
import "bootstrap/dist/css/bootstrap.min.css";
import { useEffect, useState } from "react";
import {
  Accordion,
  Button,
  Card,
  Col,
  Container,
  ListGroup,
  OverlayTrigger,
  Pagination,
  Popover,
  ProgressBar,
  Row,
  Table,
  Tooltip
} from "react-bootstrap";
import { buildStyles, CircularProgressbar } from "react-circular-progressbar";
import {
  IoMdArrowRoundBack,
  IoMdInformationCircleOutline
} from "react-icons/io";
import { useLocation, useNavigate } from "react-router-dom";
import axiosInstance from "./axiosApi";
import { MetricDescriptions } from "./MetricDescriptions";
import "./style/ProjectView.css";
import { getSuccessSplit, percentToColor } from "./Utils";

// component to view details of individual project
export default function ProjectView(props) {
  const navigate = useNavigate();
  const location = useLocation();
  const { projectId, projectName, projectDescription } = location.state;
  const [members, setMembers] = useState(["John", "Jane", "Joe"]);
  const [activeMetric, setActiveMetric] = useState(0);
  const [processM, setProcessM] = useState([[]]);
  const [productM, setProductM] = useState([[]]);
  const [stakeHolderM, setStakeHolderM] = useState([[]]);
  const [overallM, setOverallM] = useState(0);
  const [overallHistory, setOverallHistory] = useState([]);
  const [processSplit, setProcessSplit] = useState([]);
  const [productSplit, setProductSplit] = useState([]);
  const [stakeHolderSplit, setStakeHolderSplit] = useState([]);
  const [generalFeedback, setGeneralFeedback] = useState("Placeholder");
  const [generalFeedbackHistory, setGeneralFeedbackHistory] = useState([]);
  const paginationItems = [];

  useEffect(() => {
    if (props.isLoggedIn === false) {
      navigate("/login");
    }

    // insert axios call to get project details using 'id'
    // store in following format into projects via 'setProject':
    // {name: (string),
    // description: (string),
    // generalFeedback: (string),
    // metricHistory: [[{MetricDescription: (string),
    //                  MetricScore: (float),
    //                  Feedback: (string)}]],
    // members: [MemberName (string)]}

    // (see below for how there's 2 lists of metrics for each. It should be in
    // ascending order of age) e.g. [0] is oldest, [-1] is newest. Means you can
    // just .push updates to the 'history' list. then they can be split up,
    // first 4 are process, next 10 are product and last 3 are stakeholder.

    //Get project details from backend
    axiosInstance.get("projects/detail/" + projectId).then((res) => {
      // Sort the metric history by unix timestamp newest to oldest.
      // res.data.metricHistory is a dictionary of unix timestamps to metric objects.
      var sorted_metric_history = [];
      for (var timestamp in res.data.metricHistory) {
        sorted_metric_history.push([
          timestamp,
          res.data.metricHistory[timestamp],
        ]);
      }
      sorted_metric_history.sort(function (a, b) {
        return a[0] - b[0];
      });
      // Unpack the sorted metric history.
      sorted_metric_history = sorted_metric_history.map(function (a) {
        return a[1];
      });

      // Sort the feedback history by unix timestamp newest to oldest.
      // res.data.feedbackHistory is a dictionary of unix timestamps to feedback
      // objects.
      var sorted_feedback_history = [];
      for (timestamp in res.data.feedbackHistory) {
        sorted_feedback_history.push([
          timestamp,
          res.data.feedbackHistory[timestamp],
        ]);
      }
      sorted_feedback_history.sort(function (a, b) {
        return a[0] - b[0];
      });
      // Unpack the sorted feedback history.
      sorted_feedback_history = sorted_feedback_history.map(function (a) {
        return a[1];
      });

      // Iterate through the sorted metric history and calculate the overall
      // success for each.
      setOverallHistory([]);
      for (let i = 0; i < sorted_metric_history.length; i++) {
        setOverallHistory((prev) => [
          ...prev,
          (
            (sorted_metric_history[i].overall_success / 5) *
            100
          ).toFixed(1),
        ]);
      }

      // Iterate through the sorted general feedback history for use when
      // showing the general feedback history.
      setGeneralFeedbackHistory([]);
      for (let i = 0; i < sorted_feedback_history.length; i++) {
        setGeneralFeedbackHistory((prev) => [
          ...prev,
          sorted_feedback_history[i].overall_success,
        ]);
      }

      // Update the members.
      setMembers(res.data.members.members);

      // Console log the sorted metric history.
      console.log("sorted_metric_history");
      console.log(sorted_metric_history);

      setProcessM([]);
      setProductM([]);
      setStakeHolderM([]);
      for (let i = 0; i < sorted_metric_history.length; i++) {
        setProcessM((prev) => [
          ...prev,
          [
            {
              value: sorted_metric_history[i].budget,
              feedback: sorted_feedback_history[i].budget,
              description: MetricDescriptions.budget,
            },
            {
              value: sorted_metric_history[i].schedule,
              feedback: sorted_feedback_history[i].schedule,
              description: MetricDescriptions.schedule,
            },
            {
              value: sorted_metric_history[i].scope,
              feedback: sorted_feedback_history[i].scope,
              description: MetricDescriptions.scope,
            },
            {
              value: sorted_metric_history[i].team_building_and_dynamics,
              feedback: sorted_feedback_history[i].team_building_and_dynamics,
              description: MetricDescriptions.team_building_and_dynamics,
            },
          ],
        ]);
        setProductM((prev) => [
          ...prev,
          [
            {
              value: sorted_metric_history[i].overall_quality,
              feedback: sorted_feedback_history[i].overall_quality,
              description: MetricDescriptions.overall_quality,
            },
            {
              value: sorted_metric_history[i].business_and_revenue_generated,
              feedback:
                sorted_feedback_history[i].business_and_revenue_generated,
              description: MetricDescriptions.business_and_revenue_generated,
            },
            {
              value: sorted_metric_history[i].functional_suitability,
              feedback: sorted_feedback_history[i].functional_suitability,
              description: MetricDescriptions.functional_suitability,
            },
            {
              value: sorted_metric_history[i].reliability,
              feedback: sorted_feedback_history[i].reliability,
              description: MetricDescriptions.reliability,
            },
            {
              value: sorted_metric_history[i].performance_efficiency,
              feedback: sorted_feedback_history[i].performance_efficiency,
              description: MetricDescriptions.performance_efficiency,
            },
            {
              value: sorted_metric_history[i].operability,
              feedback: sorted_feedback_history[i].operability,
              description: MetricDescriptions.operability,
            },
            {
              value: sorted_metric_history[i].security,
              feedback: sorted_feedback_history[i].security,
              description: MetricDescriptions.security,
            },
            {
              value: sorted_metric_history[i].compatibility,
              feedback: sorted_feedback_history[i].compatibility,
              description: MetricDescriptions.compatibility,
            },
            {
              value: sorted_metric_history[i].maintainability,
              feedback: sorted_feedback_history[i].maintainability,
              description: MetricDescriptions.maintainability,
            },
            {
              value: sorted_metric_history[i].transferability,
              feedback: sorted_feedback_history[i].transferability,
              description: MetricDescriptions.transferability,
            },
          ],
        ]);
        setStakeHolderM((prev) => [
          ...prev,
          [
            {
              value: sorted_metric_history[i].user_satisfaction,
              feedback: sorted_feedback_history[i].user_satisfaction,
              description: MetricDescriptions.user_satisfaction,
            },
            {
              value: sorted_metric_history[i].team_satisfaction,
              feedback: sorted_feedback_history[i].team_satisfaction,
              description: MetricDescriptions.team_satisfaction,
            },
            {
              value: sorted_metric_history[i].top_management_satisfaction,
              feedback: sorted_feedback_history[i].top_management_satisfaction,
              description: MetricDescriptions.top_management_satisfaction,
            },
          ],
        ]);
      }
    });
  }, [navigate, overallHistory, projectId, props.isLoggedIn]);

  // Update the overallM using the overallHistory.
  useEffect(() => {
    setOverallM(overallHistory[overallHistory.length - 1 - activeMetric]);
  }, [activeMetric, overallHistory]);

  // Update the generalFeedbackM using the generalFeedbackHistory.
  useEffect(() => {
    setGeneralFeedback(
      generalFeedbackHistory[generalFeedbackHistory.length - 1 - activeMetric]
    );
  }, [activeMetric, generalFeedbackHistory]);

  useEffect(() => {
    setProcessSplit(
      getSuccessSplit(processM[processM.length - 1 - activeMetric])
    );
  }, [activeMetric, processM]);

  useEffect(() => {
    setProductSplit(
      getSuccessSplit(productM[productM.length - 1 - activeMetric])
    );
  }, [activeMetric, productM]);

  useEffect(() => {
    setStakeHolderSplit(
      getSuccessSplit(stakeHolderM[stakeHolderM.length - 1 - activeMetric])
    );
  }, [activeMetric, stakeHolderM]);

  const renderTooltip = (props) => {
    return (
      <Tooltip id="button-tooltip" {...props}>
        Green represent a high (3.5-5) score, yellow represents a medium
        (2.5-3.5) score, and red represents a low (1-2.5) score.
      </Tooltip>
    );
  };

  const renderHistoryTip = (props) => {
    return (
      <Tooltip id="button-tooltip" {...props}>
        Browse through the metric history to see the progress of the project.
        The higher the number, the older the metrics.
      </Tooltip>
    );
  };

  const deletePopover = (
    <Popover id="popover-delete">
      <Popover.Header as="h3">Are you sure?</Popover.Header>
      <Popover.Body>
        Once you delete the project, it's <strong>gone forever!</strong>.
        <Button
          className="editProj"
          variant="danger"
          onClick={() =>
            navigate("/dashboard/project/delete", { state: { id: projectId } })
          }
        >
          Yes I am sure, delete project.
        </Button>
      </Popover.Body>
    </Popover>
  );
  const len = processM.length - 1;
  paginationItems.push(
    <Pagination.Item
      key={len}
      active={activeMetric === 0}
      onClick={() => setActiveMetric(0)}
    >
      Latest
    </Pagination.Item>
  );
  for (let i = processM.length - 2; i >= 0; i--) {
    paginationItems.push(
      <Pagination.Item
        key={i}
        active={activeMetric === len - i}
        onClick={() => setActiveMetric(len - i)}
      >
        {len - i}
      </Pagination.Item>
    );
  }

  return (
    <>
      <Container className="projectViewHeader">
        <Row className="justify-content-md-between" sm="auto">
          <Col sm={4}>
            <Button
              className="backButton"
              variant="secondary"
              onClick={() => navigate(-1)}
            >
              <IoMdArrowRoundBack size={35} />
            </Button>
            <Col className="sections">
              <span className="projectTitle">
                <h1>{projectName} 🚀</h1>
                <Button
                  className="editProj"
                  variant="success"
                  onClick={() =>
                    navigate("/dashboard/project/edit", {
                      state: {
                        projectID: projectId,
                        projectName: projectName,
                        projectDescription: projectDescription,
                        projectMembers: members,
                      },
                    })
                  }
                >
                  Edit Project
                </Button>
                <OverlayTrigger
                  rootClose="true"
                  trigger="click"
                  placement="right"
                  overlay={deletePopover}
                >
                  <Button className="editProj" variant="danger">
                    Delete Project
                  </Button>
                </OverlayTrigger>
              </span>
            </Col>
          </Col>

          <Col className="sections" sm={8}>
            <h3>Project Details 📑</h3>
            <hr />
            <Row>
              <Col sm={5}>
                <Card style={{ borderColor: "#9D231B" }}>
                  <Card.Body>
                    <Card.Title>Description</Card.Title>
                    <Card.Text style={{ fontSize: "20px" }}>
                      {projectDescription}
                    </Card.Text>
                  </Card.Body>
                </Card>
              </Col>
              <Col>
                <Card style={{ borderColor: "#9D231B" }}>
                  <Card.Body>
                    <Card.Title>Members</Card.Title>
                    <Row>
                      <Col>
                        <ListGroup style={{ fontSize: "20px" }}>
                          {members.map((member, index) => {
                            return (
                              <>
                                {index <= members.length / 2 && (
                                  <ListGroup.Item key={index}>
                                    {member}
                                  </ListGroup.Item>
                                )}
                              </>
                            );
                          })}
                        </ListGroup>
                      </Col>
                      <Col>
                        <ListGroup style={{ fontSize: "20px" }}>
                          {members.map((member, index) => {
                            return (
                              <>
                                {index > members.length / 2 && (
                                  <ListGroup.Item key={index}>
                                    {member}
                                  </ListGroup.Item>
                                )}
                              </>
                            );
                          })}
                        </ListGroup>
                      </Col>
                    </Row>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Col>
        </Row>
        <Row className="mt-4">
          <Container className="sections">
            <h3>Metrics 📈</h3>
            <hr />
            <Row>
              <Col xs={4}>
                <Card style={{ borderColor: "#9D231B" }}>
                  <Card.Body>
                    <CircularProgressbar
                      styles={buildStyles({
                        pathColor: percentToColor(overallM),
                        textColor: "black",
                      })}
                      value={overallM}
                      text={`${overallM}%`}
                    />
                  </Card.Body>
                  <Card.Footer>
                    <small className="text-muted">Overall Success Chance</small>
                  </Card.Footer>
                </Card>
              </Col>
              <Col style={{ position: "relative" }}>
                <OverlayTrigger
                  placement="top"
                  delay={{ show: 250, hide: 400 }}
                  overlay={renderTooltip}
                >
                  <div style={{ position: "absolute", top: 0, right: 0 }}>
                    <IoMdInformationCircleOutline
                      size={32}
                      style={{ position: "absolute", top: 0, right: 0 }}
                    />
                  </div>
                </OverlayTrigger>

                <h2>Process Metrics</h2>
                <ProgressBar className="mb-4">
                  <ProgressBar
                    variant="success"
                    now={processSplit[2]}
                    key={1}
                  />
                  <ProgressBar
                    variant="warning"
                    now={processSplit[1]}
                    key={2}
                  />
                  <ProgressBar variant="danger" now={processSplit[0]} key={3} />
                </ProgressBar>
                <h2>Product Metrics</h2>
                <ProgressBar className="mb-4">
                  <ProgressBar
                    variant="success"
                    now={productSplit[2]}
                    key={1}
                  />
                  <ProgressBar
                    variant="warning"
                    now={productSplit[1]}
                    key={2}
                  />
                  <ProgressBar variant="danger" now={productSplit[0]} key={3} />
                </ProgressBar>
                <h2>Stakeholder Metrics</h2>
                <ProgressBar className="mb-4">
                  <ProgressBar
                    variant="success"
                    now={stakeHolderSplit[2]}
                    key={1}
                  />
                  <ProgressBar
                    variant="warning"
                    now={stakeHolderSplit[1]}
                    key={2}
                  />
                  <ProgressBar
                    variant="danger"
                    now={stakeHolderSplit[0]}
                    key={3}
                  />
                </ProgressBar>
                <Card>
                  <Card.Body>
                    <Card.Title>Feedback</Card.Title>
                    <Card.Text style={{ fontSize: "20px" }}>
                      {generalFeedback}
                    </Card.Text>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
            <Row className="mt-3">
              <Col>
                <h3 className="mt-3">Metrics Breakdown 🔎</h3>
                <hr />
                <Row sm="auto">
                  <Col>
                    <div className="d-flex justify-content-between align-items-center">
                      <Pagination>{paginationItems}</Pagination>
                      <OverlayTrigger
                        placement="top"
                        delay={{ show: 250, hide: 400 }}
                        overlay={renderHistoryTip}
                      >
                        <div>
                          <IoMdInformationCircleOutline
                            className="align-self-center"
                            size={32}
                          />
                        </div>
                      </OverlayTrigger>
                    </div>
                  </Col>
                </Row>

                <Accordion alwaysOpen flush>
                  {[
                    {
                      metrics: processM[processM.length - 1 - activeMetric],
                      header: "Process Metrics",
                    },
                    {
                      metrics: productM[productM.length - 1 - activeMetric],
                      header: "Product Metrics",
                    },
                    {
                      metrics:
                        stakeHolderM[stakeHolderM.length - 1 - activeMetric],
                      header: "Stakeholder Metrics",
                    },
                  ].map(({ metrics, header }, index) => (
                    <Accordion.Item key={index} eventKey={index.toString()}>
                      <Accordion.Header>{header}</Accordion.Header>
                      <Accordion.Body>
                        <Table size="sm" className="tables" striped bordered>
                          <thead>
                            <tr>
                              <th>Description</th>
                              <th>Metric Score</th>
                              <th>Feedback</th>
                            </tr>
                          </thead>
                          <tbody>
                            {metrics.map((metric, index) => (
                              <tr
                                key={index}
                                style={{
                                  backgroundColor:
                                    metric.value !== 0 &&
                                    percentToColor(
                                      ((metric.value - 1) / 4) * 100
                                    ),
                                }}
                              >
                                <td>{metric.description}</td>
                                <td>{metric.value}</td>
                                <td>{metric.feedback}</td>
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
          </Container>
        </Row>
      </Container>
    </>
  );
}
