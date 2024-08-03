import {SET_IMAGES,
        SET_SINGLE_CHOSEN_IMG
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
