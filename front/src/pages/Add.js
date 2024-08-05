import React from "react"
import { useDispatch, useSelector } from "react-redux"
import { Link } from 'react-router-dom';
import axios from 'axios';
import Navbar from "../components/Navbar"
import Loader from "../components/Loader";
import { setChosenDesc, 
        setExtractedFaceBoxes, 
        setSingleChosenImage, 
        setSingleChosenImageFile,
        switchLoader,
        setPreprocessingStatus
      } from "../redux/actions";
import Verification from "../components/Verification"


const Add = () => {
    const dispatch = useDispatch()
    const singleChosenImg = useSelector(state => state.singleChosenImg)
    const singleChosenImgFile = useSelector(state => state.singleChosenImgFile)
    const chosenDescription = useSelector(state => state.chosenDescription)
    const loaderStatus = useSelector(state => state.loaderStatus)
    const isPreprocessingDone = useSelector(state => state.isPreprocessingDone)


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
        dispatch(switchLoader(true))
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
          
        console.log(response)

          dispatch(setExtractedFaceBoxes(response.data))
          dispatch(switchLoader(false))
          dispatch(setPreprocessingStatus(true))
        } catch (error) {
          console.error('Error uploading file:', error);
          dispatch(switchLoader(false))
          dispatch(setPreprocessingStatus(false))
        }
    };




    return (
        <>
            <Navbar/>
            <div className="container">   
                {!isPreprocessingDone && <div className="row">
                    <h1 className="mt-5">Add to Gallery</h1>
                    <h5>Here you can upload your favorite images</h5>
                    <hr/>

                    {!loaderStatus && <div className="row">
                        <div className="col-sm-6"> 
                        <h4>Upload</h4>
                            <form onSubmit={handleImageAdd}>
                                    <div className="file-upload d-flex flex-column justify-content-center align-items-center  p-5">
                                        <input type="file" accept="image/png, image/jpeg" className="form-control" multiple onChange={handleFileChange} />
                                    </div>
                                    <div className="form-group">
                                        <label for="exampleTextarea">Description</label>
                                        <textarea className="form-control " id="imageDescription" rows="3"  onChange={handleDescriptionChange} value={chosenDescription} placeholder="Once upon a time ... "></textarea>
                                    </div>
                                    <button type="submit" className="btn btn-dark my-3 ">Add</button>
                                </form>
                        </div>
                        <div className="col-sm-6 ">
                            <h4>Preview</h4>
                            <div className="d-flex flex-column justify-content-center align-items-center">
                                {!singleChosenImgFile && <p className="mx-5">No image is selected!</p>}
                                {singleChosenImgFile && <img src={singleChosenImg} alt="Image Preview" style={{ width: '300px', height: 'auto' }} />}
                            </div>
                        </div>
                    </div>}
                </div>} 


                {loaderStatus && !isPreprocessingDone && 
                                <div className="d-flex justify-content-center p-5">
                                <Loader/>   
                                </div>
                        }

                {isPreprocessingDone && <div className="row">
                    <Verification/>
                </div>}
                    
            </div> 
        </>
    )
}

export default Add