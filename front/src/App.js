import React from "react"
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import { Provider } from 'react-redux'
import Store from './redux/store'

import Gallery from "./pages/Gallery"
import Add from "./pages/Add"


const App = () => {
    return (
        <Provider store={Store}>
            <Router>
                <Routes>
                    <Route path="/" element={<Gallery />} />
                    <Route path="/add" element={<Add />} />
                </Routes>
            </Router>
        </Provider>
    )
}


export default App