import React, { Component } from "react";
import { TextField, Button, Grid, Typography, Alert, InputAdornment, IconButton, FormControl, OutlinedInput } from "@material-ui/core";
import { Visibility, VisibilityOff} from "@mui/icons-material"
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

export default class EmployeeLogin extends Component {
    constructor(props) {
        super(props);
        this.state = {
            UserID: "",
            Password: "",
            error: "",
            showPassword: false
        }

        this._handleIDTextFieldChange = this._handleIDTextFieldChange.bind(this);
        this._handlePassTextFieldChange = this._handlePassTextFieldChange.bind(this);
        this._enterButtonPressed = this._enterButtonPressed.bind(this);
        this._passwordShowButton = this._passwordShowButton.bind(this);
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
        console.log(this.state.showPassword);

        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
                UserID: this.state.UserID,
                Password: this.state.Password
            })
        };

        fetch('/api/')
    }

    _passwordShowButton(){
        this.setState(
            {
                showPassword: !this.state.showPassword
            }
        )
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
                        placeholder = "Enter Your User ID"
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
                        placeholder = "Enter Your Password"
                        value = {this.state.Password}
                        defaultValue = {this.state.Password}
                        type={this.state.showPassword ? 'text' : 'password'}
                        helperText = {this.state.error}
                        variant = "outlined"
                        onChange = {this._handlePassTextFieldChange}
                        InputProps = {{
                            endAdornment:
                                <InputAdornment position = "end">
                                    <IconButton edge="end" onClick={this._passwordShowButton}>
                                        {this.state.showPassword ? <VisibilityOff /> : <Visibility />}
                                    </IconButton>
                                </InputAdornment>
                        }}
                        >
                    </TextField>
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
