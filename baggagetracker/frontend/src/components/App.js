import React, { Component } from "react";
import { render } from "react-dom";

import HomePage from "./HomePage";
import CustomerLogin from "./CustomerLogin";
import EmployeeLogin from "./EmployeeLogin";

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div>
                <HomePage />
                <CustomerLogin />
                <EmployeeLogin />
            </div>);
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);