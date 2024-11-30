import React, { Component } from "react";
import { TextField, Button, Grid, Typography, Paper, Alert } from "@mui/material";

export default class EmployeeLogin extends Component {
    constructor(props) {
        super(props);
        this.state = {
            employeeId: "",
            password: "",
            errorMessage: "",
        };
    }

    // Handle input changes
    handleInputChange = (event) => {
        const { name, value } = event.target;
        this.setState({ [name]: value });
    };

    // Handle form submission
    handleSubmit = (event) => {
        event.preventDefault(); // Prevent default form submission

        const { employeeId, password } = this.state;

        // Send the credentials to the backend for verification
        fetch("http://localhost:8000/api/employee/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ employeeId, password }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.message === "Login successful") {
                    // Redirect the user after successful login
                    window.location.href = "/dashboard"; // Example redirect to dashboard
                } else {
                    this.setState({ errorMessage: data.message });
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                this.setState({
                    errorMessage: "Something went wrong. Please try again.",
                });
            });
    };

    render() {
        const { employeeId, password, errorMessage } = this.state;

        return (
            <Grid
                container
                spacing={0}
                alignItems="center"
                justifyContent="center"
                style={{ minHeight: "100vh" }}
            >
                <Grid item xs={11} sm={6} md={4}>
                    <Paper elevation={3} style={{ padding: "2rem" }}>
                        <Typography
                            component="h1"
                            variant="h5"
                            align="center"
                            gutterBottom
                        >
                            Employee Login
                        </Typography>

                        <form onSubmit={this.handleSubmit}>
                            <Grid container spacing={2}>
                                {/* Employee ID Field */}
                                <Grid item xs={12}>
                                    <TextField
                                        fullWidth
                                        label="Employee ID"
                                        name="employeeId"
                                        variant="outlined"
                                        value={employeeId}
                                        onChange={this.handleInputChange}
                                        required
                                    />
                                </Grid>

                                {/* Password Field */}
                                <Grid item xs={12}>
                                    <TextField
                                        fullWidth
                                        label="Password"
                                        type="password"
                                        name="password"
                                        variant="outlined"
                                        value={password}
                                        onChange={this.handleInputChange}
                                        required
                                    />
                                </Grid>

                                {/* Error Message */}
                                {errorMessage && (
                                    <Grid item xs={12}>
                                        <Alert severity="error">{errorMessage}</Alert>
                                    </Grid>
                                )}

                                {/* Submit Button */}
                                <Grid item xs={12} align="center">
                                    <Button
                                        type="submit"
                                        variant="contained"
                                        color="primary"
                                        fullWidth
                                        style={{ padding: "0.8rem" }}
                                    >
                                        Login
                                    </Button>
                                </Grid>
                            </Grid>
                        </form>
                    </Paper>
                </Grid>
            </Grid>
        );
    }
}
