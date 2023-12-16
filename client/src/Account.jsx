import React from 'react';
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';

import Loading from './Loading';
import './App.css';

const Account = () => {

    const [userData, setUserData] = useState(null);
    const [loading, setLoading] = useState(true);
    const { username } = useParams();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch(`getUserData`);
                const user_data = await res.json();
                setUserData(user_data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching player data:', error);
            }
        };

        fetchData();
    }, [username]);

    async function deleteAccount() {
        const res = await fetch("registration/delete_account/");

        window.location = "registration/sign_in/";
    }

    return (
        <div>
            {loading ? <Loading /> : ( userData.user === 'None' ? <div className='container'><div className="player-card">Account no Found. Please make sure you are logged in.</div></div> :
                <div className='container'>
                    <div className="player-card">
                        <div className="username">Your Account</div>
                        <div className="details">Name: {userData.first_name} {userData.last_name}</div>
                        <div className="details">Email: {userData.email}</div>
                        <div className="details">Linked Halo Username: {userData.haloUsername}</div>
                        <button onClick={deleteAccount}>Delete Account</button>
                    </div>
                </div>
                )
            }
            <button onClick={deleteAccount}>Delete Account</button>
        </div>
    )
};

export default Account;