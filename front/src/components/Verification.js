import React, {useEffect} from "react"
import Navbar from "../components/Navbar"
import { useDispatch, useSelector } from "react-redux"

const Verification = () => {
    const dispatch = useDispatch()
    const images = useSelector(state => state.images)

    return (
        <>
            <div className="container d-flex flex-column justify-content-center">    
                <h1 className="mt-5">Verification</h1>
                <h5>Here your collection of images are shown</h5>
            </div>
            
        </>
    )
}

export default Verification