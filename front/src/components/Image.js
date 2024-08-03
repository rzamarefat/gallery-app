import { useDispatch, useSelector } from "react-redux"


const Image = ({image}) => {
    const value = useSelector(state => state.initialValue)
    const dispatch = useDispatch()
    console.log(image)
    return (
        <>
            <div class="col-md-2">
                <img src={`data:image/jpeg;base64,${image.data}`} class="img-thumbnail fixed-size-img my-1"></img>
            </div>
        </>
    )
}

export default Image