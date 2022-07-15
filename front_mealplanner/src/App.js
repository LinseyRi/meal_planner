import { useState, useEffect, useReducer } from 'react'; 
import AppBody from './AppBodyContent/AppBody';
import AppHeader from './AppHeaderContent/AppHeader';

export default function App() {
    return (
        <div>
            <AppHeader /> 
            <AppBody />
        </div>
    )
}