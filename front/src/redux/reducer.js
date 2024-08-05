import initialState from "./initiaState"
import { SET_CHOSEN_IMG_DESC, SET_EXTRACTED_FACE_BOXES, SET_IMAGES,
        SET_SINGLE_CHOSEN_IMG,
        SET_SINGLE_CHOSEN_IMG_FILE,
        SWITCH_LOADER,
        SET_PREPROCESSING_STATUS
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
                ...state, singleChosenImg: action.payload
            }
        case SET_SINGLE_CHOSEN_IMG_FILE:
            return {
                ...state, singleChosenImgFile: action.payload
            }
        
        case SET_CHOSEN_IMG_DESC:
            return {
                ...state, chosenDescription: action.payload
            }
        case SET_EXTRACTED_FACE_BOXES:
            return {
                ...state, extractedFaceBoxes: action.payload
            }
        case SWITCH_LOADER:
            return {
                ...state, loaderStatus: action.payload
            }
        case SET_PREPROCESSING_STATUS:
            return {
                ...state, isPreprocessingDone: action.payload
            }


            

        default:
            return state;
    }

}


export default reducer