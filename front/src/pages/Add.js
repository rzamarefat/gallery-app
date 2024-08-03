import React, { useState } from "react"
import { useDispatch, useSelector } from "react-redux"

import Navbar from "../components/Navbar"

import {setSingleChosenImage} from "../redux/actions"

const Add = () => {
    const [file, setFile] = useState();
    const dispatch = useDispatch()
    const singleChosenImage = useSelector(state => state.singleChosenImage)

    function handleFileChange(e) {
        const file = e.target.files[0];
        if (file) {
            // dispatch(setSingleChosenImage(URL.createObjectURL(file)));
            setFile(URL.createObjectURL(e.target.files[0]));
        }
    }

    console.log(file)

    return (
        <>
            <Navbar/>
            <div className="container d-flex flex-column justify-content-center">    
                <h1 className="mt-5">Add to Gallery</h1>
                <h5>Here you can upload your favorite images</h5>
                <hr/>
                
                <div className="file-upload d-flex flex-column justify-content-center align-items-center  p-5">
                    <input type="file" accept="image/png, image/jpeg" class="form-control" multiple onChange={handleFileChange} />
                </div>

                <hr/>

                <img scr={file} className="img-thumbnail" alt="Preview"  style={{ maxWidth: '150px', maxHeight: '150px' }}></img>

                <form>
                    <div class="form-group">
                        <label for="exampleTextarea">Description</label>
                        <textarea class="form-control" id="exampleTextarea" rows="5"></textarea>
                    </div>
                </form>
                <button type="submit" class="btn btn-dark my-3">Add</button>
            </div>
        </>
    )
}

export default Add