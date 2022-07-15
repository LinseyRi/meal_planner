import { useState, useEffect, useReducer } from 'react'; 
import NavBar from './NavBar'; 
import './AppHeader.css'; 

export default function AppHeader() {
    return (
        <header className='app-header'>
            <h1>Meal Planner App</h1>
            <NavBar />
        </header>
    )
}