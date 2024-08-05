import React, {useEffect} from "react"
import Image from "./Image"
import { useDispatch, useSelector } from "react-redux"


const Verification = () => {
    const dispatch = useDispatch()
    const extractedFaceBoxes = useSelector(state => state.extractedFaceBoxes)
    const images = useSelector(state => state.images)

    return (
        <>
            <div className="container d-flex flex-column justify-content-center">    
                <h1 className="mt-5">Verification</h1>
                <h5>Here you can verify who we have recognized in the uploaded images</h5>
                <hr/>

                <div className="d-flex ">
                        {extractedFaceBoxes.map(face => {

                        return (
                            <div className="d-flex flex-column justify-content-center align-items-center m-4">
                                <img src={`data:image/jpeg;base64,${face.data}`} className="img-thumbnail fixed-size-img"></img>
                                <p>Not known yet</p>
                                
                            </div>
                        )
                        })}
                </div>
                
                
            </div>
            
        </>
    )
}

export default Verification