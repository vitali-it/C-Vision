import './styles.css';
import React from 'react';
import { useNavigate } from 'react-router-dom'

export const HomeContainer = () => {
    const navigate = useNavigate();
    const navigateToUpload = () => {
        navigate('/upload');
    };

    return ( 
        <div>
            <h2>Here you can classify your animal</h2>
            <div className='center'>
                <button onClick={navigateToUpload} className='btn-proceed'>Click to proceed</button>
            </div>
        </div>
    );
}
