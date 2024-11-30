import React, { Component } from "react";

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
        event.preventDefault();  // Prevent default form submission

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
                // You can use React Router for redirecting to a new page
                window.location.href = "/dashboard"; // Example redirect to dashboard
            } else {
                this.setState({ errorMessage: data.message });
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            this.setState({ errorMessage: "Something went wrong. Please try again." });
        });
    };

    render() {
        const { employeeId, password, errorMessage } = this.state;

        return (
            <div>
                <h2>Employee Login</h2>
                <form onSubmit={this.handleSubmit}>
                    <div>
                        <label>Employee ID</label>
                        <input
                            type="text"
                            name="employeeId"
                            value={employeeId}
                            onChange={this.handleInputChange}
                            required
                        />
                    </div>
                    <div>
                        <label>Password</label>
                        <input
                            type="password"
                            name="password"
                            value={password}
                            onChange={this.handleInputChange}
                            required
                        />
                    </div>
                    <button type="submit">Login</button>
                </form>
                {errorMessage && <p>{errorMessage}</p>}
            </div>
        );
    }
}
