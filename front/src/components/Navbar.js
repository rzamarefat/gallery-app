import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div className='container'>
                        <Link to="/" className='navbar-brand '>SmartGallery</Link>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                        <Link to="/add" className='nav-link'>Add to Gallery</Link>
                        </div>
                </div>
            </nav>
            
        </>
    )
}

export default Navbar