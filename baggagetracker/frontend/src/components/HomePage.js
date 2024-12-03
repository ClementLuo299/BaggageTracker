import React, { Component } from "react";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

import {Button, Grid, Typography} from "@material-ui/core";

import CustomerLogin from "./CustomerLogin";
import EmployeeLogin from "./EmployeeLogin";
import EmployeeDashboard from "./EmployeeDashboard";
import EmployeeCheckIn from "./EmployeeCheckIn";

export default class HomePage extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path="/" element ={
                        <Grid container spacing={1} align="center">
                            <Grid item xs={12}>
                                <Typography component ="h1" variant="h1">
                                    Baggage Tracker
                                </Typography>
                            </Grid>
        
                            <Grid item xs={12}>
                                <Typography component ="h4" variant="h4">
                                    Select Login
                                </Typography>
                            </Grid>
        
                            <Grid item xs={12}>
                                <Button color="primary" variant="contained" href="/login">
                                    Customer Login
                                </Button>
                            </Grid>
        
                            
                            <Grid item xs={12}>
                                <Button color="secondary" variant="contained" href ="/emplogin">
                                    Employee Login
                                </Button>
                            </Grid>
                        </Grid>
                    }/>
                    <Route path="/login" element={<CustomerLogin/>}/>
                    <Route path="/emplogin" element={<EmployeeLogin/>}/>
                    <Route path="/employees/:userID" element = {<EmployeeDashboard/>}/>
                    <Route path="/empcheckin" element = {<EmployeeCheckIn/>}/>
                </Routes>
            </Router>
        );
    }
}