import { useState, useEffect, useReducer } from 'react'; 
import './NavBar.css';

export default function NavBar() {
    return (
        <nav className='nav-bar'>
            <div className='dropdown'>
                <button className='drop-btn'>
                    <i class="fa-solid fa-bars"></i>
                </button>
                <div className='dropdown-content'>
                    <div className='nav-link'><a href="">Home</a></div>
                    <div className='nav-link'><a href="">Recipes</a></div>
                    <div className='nav-link'><a href="">Ingredients</a></div>
                </div>
            </div>
        </nav>
    )
}