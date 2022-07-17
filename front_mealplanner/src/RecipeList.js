import { useState, useEffect, useReducer } from 'react'; 
import axios from 'axios'; 
import DummyData from './dummydata.json'; 
import './RecipeList.css'; 

export default function RecipeList() {

    const [ recipeList, setRecipeList ] = useState(null); 

    // pull data from the API 
    const getAllRecipes = () => {

    }

    useEffect( () => {
        axios.get("http://127.0.0.1:8000/")
        .then((response) => {
            console.log("Trying:")
            console.log(response.data)
            setRecipeList(response.data)
        })
        .catch(function (error) {
            console.log(error)
        })
    }, [])

    const checkRecipes = () => {
        console.log("Hello")
        console.log(recipeList)
    }

    return (
        <div>
            <div className='subheader'>
                <h2>Recipes</h2>
            </div>
            
            <ul className='recipe-list'>
                {   recipeList &&
                    recipeList.map( p => {
                        return <li key={p.name}><i className="fa-solid fa-utensils"></i> {p.name}</li>
                    })
                }
            </ul>
        </div>
    )
}