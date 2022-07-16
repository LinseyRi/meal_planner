import { useState, useEffect, useReducer } from 'react'; 
import { Link } from "react-router-dom"; 
import NavBar from './NavBar'; 
import './AppHeader.css'; 

export default function AppHeader() {
    return (
        <header className='app-header'>
            <Link to="/"><h1>Meal Planner App</h1></Link>
            <NavBar />
        </header>
    )
}