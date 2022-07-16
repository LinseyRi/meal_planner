import { useState, useEffect, useReducer } from 'react'; 
import DummyData from './dummydata.json'; 
import './RecipeList.css'; 

export default function RecipeList() {
    return (
        <div>
            <div className='subheader'>
                <h2>Recipes</h2>
            </div>
            
            <ul className='recipe-list'>
                {
                    DummyData.map( p => {
                        return <li key={p.name}><i class="fa-solid fa-utensils"></i> {p.name}</li>
                    })
                }
            </ul>
        </div>
    )
}