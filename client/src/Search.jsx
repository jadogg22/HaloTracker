import React from 'react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Search.css';

const Search = () => {
    const [stringValue, setStringValue] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        navigate(`/player/${stringValue}`);
    }

    return (
        <div className="search-container">
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Enter Xbox Live Username" className="search-bar" value={stringValue} onChange={(e) => setStringValue(e.target.value)}/>
                <button type="submit" className="search-button">Search</button>
            </form>
        </div>
    );
}

export default Search;