import React, { Component } from "react";
import { useParams } from "react-router-dom";

const EmployeeDashboard = () => {
    const {userID} = useParams();
    return <p>Dashboard page for: {userID}</p>
}

export default EmployeeDashboard;