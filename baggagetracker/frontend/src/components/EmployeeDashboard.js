import React, { Component } from "react";
import { useParams } from "react-router-dom";

import AppBar from "@material-ui/core/AppBar";
import ToolBar from "@material-ui/core/Toolbar";
import ToolbarGroup from "@material-ui/core/Toolbar";
import{Button, Grid, Box, IconButton} from "@material-ui/core";
import { AccountCircle } from "@mui/icons-material"

const pages = ["Dashboard","Check In","Incidents"]

const EmployeeDashboard = () => {
    const {userID} = useParams();

    const [anchorElNav, setAnchorElNav] = React.useState(null);

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
                <Button variant="contained" color="inherit">
                    Content Here
                </Button>
            </div>
        </div>
    );
}

export default EmployeeDashboard;