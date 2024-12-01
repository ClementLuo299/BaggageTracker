import React, { Component } from "react";
import { TextField, Button, Grid, Typography, Alert, InputAdornment, IconButton } from "@material-ui/core";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

export default class EmployeeLogin extends Component {
    constructor(props) {
        super(props);
        this.state = {
            UserID: "",
            Password: "",
            error: "",
        }

        this._handleIDTextFieldChange = this._handleIDTextFieldChange.bind(this);
        this._handlePassTextFieldChange = this._handlePassTextFieldChange.bind(this);
        this._enterButtonPressed = this._enterButtonPressed.bind(this)
    }

    _handleIDTextFieldChange(e){
        this.setState(
            {
                UserID: e.target.value
            }
        );
    }

    _handlePassTextFieldChange(e){
        this.setState(
            {
                Password: e.target.value
            }
        );
    }

    _enterButtonPressed(){
        console.log(this.state.UserID);
        console.log(this.state.Password);
    }

    _passwordShowButton(){
        setShowPassword(!showPassword);
    }

    render() {
        return (
            <Grid container spacing={1} align="center">
                <Grid item xs={12}>
                    <Typography component ="h2" variant="h2">
                        Enter Login Info
                    </Typography>
                </Grid>

                <Grid item xs={12}>
                    <TextField
                        error = {this.state.error}
                        label = "User ID"
                        placeholder = "Enter Your User ID Here"
                        value = {this.state.UserID}
                        defaultValue = {this.state.UserID}
                        helperText = {this.state.error}
                        variant = "outlined"
                        onChange = {this._handleIDTextFieldChange}
                    />
                </Grid>

                <Grid item xs={12}>
                    <TextField
                        error = {this.state.error}
                        label = "Password"
                        placeholder = "Enter Your Password Here"
                        value = {this.state.Password}
                        defaultValue = {this.state.Password}
                        helperText = {this.state.error}
                        variant = "outlined"
                        onChange = {this._handlePassTextFieldChange}
                    />
                </Grid>

                <Grid item xs={12}>
                    <Button color="primary" variant="contained" onClick= {this._enterButtonPressed}>
                        Enter
                    </Button>
                </Grid>

                <Grid item xs={12}>
                    <Button color="secondary" variant="contained" to="/" component={ Link }>
                        Back
                    </Button>
                </Grid>
            </Grid>
        );
    }
}
