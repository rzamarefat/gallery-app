import initialState from "./initiaState"
import { SET_CHOSEN_IMG_DESC, SET_IMAGES,
        SET_SINGLE_CHOSEN_IMG
         } 
         from "./actionTypes";


const reducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_IMAGES:
            return {
                ...state, images: action.payload
            }

        case SET_SINGLE_CHOSEN_IMG:
            return {
                ...state, singleChosenImage: action.payload
            }
        
        case SET_CHOSEN_IMG_DESC:
            return {
                ...state, chosenDescription: action.payload
            }

        default:
            return state;
    }

}


export default reducer