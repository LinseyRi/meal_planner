import { useState, useEffect, useReducer } from 'react'; 
import { Link } from "react-router-dom"; 
import './NavBar.css';

export default function NavBar() {
    return (
        <nav className='nav-bar'>
            <div className='dropdown'>
                <button className='drop-btn'>
                    <i className="fa-solid fa-bars"></i>
                </button>
                <div className='dropdown-content'>
                    <Link className="nav-link" to="/">Home</Link>
                    <Link className='nav-link' to="/recipes">Recipes</Link>
                    <a className='nav-link' href="">Ingredients</a>
                </div>
            </div>
        </nav>
    )
}