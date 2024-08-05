import React from "react"
import { useDispatch, useSelector } from "react-redux"
import axios from 'axios';
import Navbar from "../components/Navbar"
import { setChosenDesc, setExtractedFaceBoxes, setSingleChosenImage, setSingleChosenImageFile } from "../redux/actions";

const Add = () => {
    const dispatch = useDispatch()
    const singleChosenImg = useSelector(state => state.singleChosenImg)
    const singleChosenImgFile = useSelector(state => state.singleChosenImgFile)
    const chosenDescription = useSelector(state => state.chosenDescription)


    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            console.log(file)
            dispatch(setSingleChosenImageFile(file));
            dispatch(setSingleChosenImage(URL.createObjectURL(file)));
        }
    }

    const handleDescriptionChange = (e) => {
        dispatch(setChosenDesc(e.target.value))
    }

    const handleImageAdd = async (e) => {
        e.preventDefault();
    
        const formData = new FormData();
        formData.append('image', singleChosenImgFile);
        formData.append('description', chosenDescription);
    
        try {
          const response = await axios.post('http://localhost:5000/upload', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          dispatch(setExtractedFaceBoxes(response.data.boxes))
        } catch (error) {
          console.error('Error uploading file:', error);
        }
    };




    return (
        <>
            <Navbar/>
            <div className="container d-flex flex-column justify-content-center">    
                <h1 className="mt-5">Add to Gallery</h1>
                <h5>Here you can upload your favorite images</h5>
                <hr/>

                {!singleChosenImgFile && <div className="row">
                    <form onSubmit={handleImageAdd}>
                        <div className="file-upload d-flex flex-column justify-content-center align-items-center  p-5">
                            <input type="file" accept="image/png, image/jpeg" class="form-control" multiple onChange={handleFileChange} />
                        </div>
                        <div class="form-group">
                            <label for="exampleTextarea">Description</label>
                            <textarea class="form-control" id="imageDescription" rows="5" onChange={handleDescriptionChange} value={chosenDescription} placeholder="Once upon a time ... "></textarea>
                        </div>
                        <button type="submit" class="btn btn-dark my-3 ">Add</button>
                    </form>
                </div>}


                {singleChosenImgFile && <img src={singleChosenImg} alt="Image Preview" style={{ width: '300px', height: 'auto' }} />}
                
            </div>
        </>
    )
}

export default Add