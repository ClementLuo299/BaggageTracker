import React, { Component } from "react";
import { useParams } from "react-router-dom";

import AppBar from "@material-ui/core/AppBar";
import ToolBar from "@material-ui/core/Toolbar";
import ToolbarGroup from "@material-ui/core/Toolbar";
import{Button, Grid, Box, IconButton} from "@material-ui/core";
import {Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";
import { AccountCircle } from "@mui/icons-material";

const pages = ["Dashboard","Check In","Incidents"]

function createData(test,test2){
    return {test,test2};
}

const rows = [
    createData(1,1),
    createData(2,1),
    createData(1,2)
]

const EmployeeDashboard = () => {
    const {userID} = useParams();

    const [anchorElNav, setAnchorElNav] = React.useState(null);

    const columns = [
        {field:"test", headerName:"Column 1", width: 100},
        {field:"test2", headerName:"Column 2", width: 100}
    ];

    const rows = [
        {test1:1,test2:1},
        {test1:2,test2:2}
    ];

    const handleOpenNavMenu = (event) =>{
        setAnchorElNav(event.currentTarget);
    }

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    }

    return (
        <div>
            <div>
                <AppBar>
                    <ToolBar>
                        <ToolbarGroup firstChild={true} float = "left" display="flex" sx={{ml:"auto"}}>
                            <IconButton>
                                <AccountCircle style={{color:'white'}}/>
                            </IconButton>

                            <Button variant="text" color="inherit">
                                Dashboard
                            </Button>

                            <Button variant="text" color="inherit" style={{whiteSpace:"nowrap"}}>
                                Check In
                            </Button>

                            <Button variant="text" color="inherit">
                                Incidents
                            </Button>
                        </ToolbarGroup>
                    </ToolBar>
                </AppBar>
            </div>

            <div>
                <TableContainer>
                    <Table sx={{minWidth:650}}>
                        <TableHead>
                            <TableRow>
                                <TableCell>Column 1</TableCell>
                                <TableCell>Column 2</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row) => (
                                <TableRow key={row.test1}>
                                    <TableCell>{row.test1}</TableCell>
                                    <TableCell>{row.test2}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </div>
    );
}

export default EmployeeDashboard;