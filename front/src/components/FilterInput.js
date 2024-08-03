import { useDispatch, useSelector } from "react-redux"


const FilterInput = ({image}) => {
    const value = useSelector(state => state.initialValue)
    const dispatch = useDispatch()
    console.log(image)
    return (
        <>
            <div class="col-md-4">
            <form>
                <div class="form-group">
                    <input type="text" className="form-control" id="description" placeholder="For example: Brad Pit is smiling"/>
                </div>
                <select className="form-control my-1">
                    <option>No selection</option>
                    <option>Brad Pit</option>
                </select>
                <button type="submit" class="btn btn-dark my-3">Submit</button>
            </form>
            </div>
        </>
    )
}

export default FilterInput



