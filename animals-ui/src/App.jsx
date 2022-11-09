import './App.css';
import React from 'react';
import { Route,Routes,BrowserRouter } from 'react-router-dom';
import { UploadContainer } from './containers/UploadContainer';
import { HomeContainer } from './containers/HomeContainer';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<HomeContainer/>}/>
                <Route exact path='/upload' element={<UploadContainer/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
