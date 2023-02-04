import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Style from "./Home.module.scss";

function Home() {
  return (
    <div className="Home">
      <h1>This is Home page </h1>

      <Container fluid>
        <Row>
          <Col className={Style.hero}>
            <h2>Landing Page for our Idea</h2>
            <h4>
              We want to connect the social media user and the company who want
              to sell ad
            </h4>
          </Col>
        </Row>
      </Container>

      <div className="hero">
        {/* insert some images in here  */}
        <h1>insert some images in here </h1>
      </div>

      <div className="testimonials">
        <Container>
          <Row>
            <Col>sdfsdfasdfasd</Col>
            <Col>sdfdfgsdf</Col>
            <Col>dgdfg</Col>
          </Row>
        </Container>
      </div>
    </div>
  );
}

export default Home;
