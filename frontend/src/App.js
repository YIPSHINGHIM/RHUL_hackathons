import { Route, Routes } from "react-router-dom";

import NavBar from "./components/NavBar";
import AdPage from "./pages/AdPage";
import Dashboard from "./pages/Dashboard";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

function App() {
  return (
    <div className="main">
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/Login" element={<Login />}></Route>
        <Route path="/Dashboard" element={<Dashboard />}></Route>
        <Route path="/Ad_page" element={<AdPage />}></Route>
        <Route path="/Register" element={<Register />}></Route>
      </Routes>
    </div>
  );
}

export default App;
