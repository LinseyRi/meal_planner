import { useState, useEffect, useReducer } from 'react'; 
import './HomePageLinks.css'; 

export default function HomePageLink({ linkTitle, linkURL, iconClass }) {

    // <i class="fa-solid fa-book"></i> => recipe book 
    // <i class="fa-solid fa-carrot"></i> => carrot icon

    return (
        <div className='home-page-links'>
            <i className={ iconClass }></i><a href={ linkURL }>{ linkTitle }</a>
        </div>
    )
}