import {SET_IMAGES,
        SET_SINGLE_CHOSEN_IMG,
        SET_CHOSEN_IMG_DESC,
        SET_EXTRACTED_FACE_BOXES,
        SET_SINGLE_CHOSEN_IMG_FILE
        } 
        from './actionTypes'


export const setImages = (images) => {
    return {
        type: SET_IMAGES,
        payload: images
    }
}

export const setSingleChosenImage = (img) => {
    return {
        type: SET_SINGLE_CHOSEN_IMG,
        payload: img
    }
}
export const setSingleChosenImageFile = (img) => {
    return {
        type: SET_SINGLE_CHOSEN_IMG_FILE,
        payload: img
    }
}



export const setChosenDesc = (text) => {
    return {
        type: SET_CHOSEN_IMG_DESC,
        payload: text
    }
}

export const setExtractedFaceBoxes = (faces) => {
    return {
        type: SET_EXTRACTED_FACE_BOXES,
        payload: faces
    }
}



