import React, { Component } from "react";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

import {Button, Grid, Typography} from "@material-ui/core";

import CustomerLogin from "./CustomerLogin";
import EmployeeLogin from "./EmployeeLogin";

export default class HomePage extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component ="h1" variant="h1">
                        Baggage Tracker
                    </Typography>
                </Grid>

                <Grid item xs={12} align="center">
                    <Typography component ="h4" variant="h4">
                        Select Login
                    </Typography>
                </Grid>

                <Grid item xs={12} align="center">
                    <Button color="primary" variant="contained">
                        Customer Login
                    </Button>
                </Grid>

                
                <Grid item xs={12} align="center">
                    <Button color="secondary" variant="contained">
                        Employee Login
                    </Button>
                </Grid>
            </Grid>
        );
    }
}