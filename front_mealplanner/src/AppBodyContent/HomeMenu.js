import { useState, useEffect, useReducer } from 'react'; 
import HomePageLink from './HomePageLink'; 

export default function HomeMenu() {

    return (
        <div className='home-menu'>
            <HomePageLink linkTitle="Recipes" linkURL="/recipes/" iconClass="fa-solid fa-book" />
            <HomePageLink linkTitle="Ingredients" linkURL="/ingredient_list/" iconClass="fa-solid fa-carrot" />
        </div>
    )
}