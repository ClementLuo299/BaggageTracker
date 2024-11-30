import React, { Component } from "react";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

import CustomerLogin from "./CustomerLogin";
import EmployeeLogin from "./EmployeeLogin";

export default class HomePage extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path='/' element={<p>This is the home page</p>}></Route>
                    <Route path='/login' element={<CustomerLogin/>}></Route>
                    <Route path='/emplogin' element={<EmployeeLogin/>}></Route>
                </Routes>
            </Router>
        );
    }
}