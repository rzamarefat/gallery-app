import React, {useEffect} from "react"
import Image from '../components/Image'
import Navbar from "../components/Navbar"
import { useDispatch, useSelector } from "react-redux"
import {setImages} from "../redux/actions"
import FilterInput from "../components/FilterInput"

const Gallery = () => {
    const dispatch = useDispatch()
    const images = useSelector(state => state.images)
    
    async function fetchImages() {
        try {
            const response = await fetch('http://127.0.0.1:5000/images');
            const images = await response.json();
            
            dispatch(setImages(images))
            
        } catch (error) {
            console.error('Error fetching images:', error);
        }
    }

    useEffect(() => {
        fetchImages()
    }, [])

    return (
        <>
            <Navbar/>
            <div className="container d-flex flex-column justify-content-center">    
                <h1 className="mt-5">Gallery</h1>
                <h5>Here your collection of images are shown</h5>
                
                <div id="imageContainer"></div>
                <hr/>

                <div class="row my-4 d-flex justify-content-center">
                    <FilterInput/>
                </div>

                <hr/>

                <div class="row mt-4">
                    {images.map(img => (
                        <Image image={img}/>
                    ))}
                </div>

            </div>
            
        </>
    )
}

export default Gallery