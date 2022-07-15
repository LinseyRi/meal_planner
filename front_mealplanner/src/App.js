import { useState, useEffect, useReducer } from 'react'; 
import { Route, Routes } from "react-router-dom"; 
import AppBody from './AppBodyContent/AppBody'; // Use as page 1
import RecipeList from './RecipeList';  // Use as page 2
import AppHeader from './AppHeaderContent/AppHeader';

export default function App() {
    return (
        <div>
            <AppHeader /> 
            <Routes>
                <Route path="/" element={<AppBody />} />
                <Route path="/recipes" element={<RecipeList />} />
            </Routes>
        </div>
    )
}