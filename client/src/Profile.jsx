import React from 'react';
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';
import Loading from './Loading';
import './App.css';

const Profile = () => {
    const [playerData, setPlayerData] = useState(null);
    const [loading, setLoading] = useState(true);
    const { username } = useParams();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch(`getUserData`);
                const user_data = await res.json();
                const res2 = await fetch(`userData/${user_data.haloUsername}`);
                const data = await res2.json();
                console.log(data);
                setPlayerData(data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching player data:', error);
            }
        };

        fetchData();
    }, [username]);

    return (
        <div>
            {loading ? <Loading /> : ( playerData.notFound ? <div className='container'><div className="player-card">Player not found</div></div> :
                <div className='container'>
                    <div className="player-card">
                        <span>Your Linked Account</span>
                        <div className="username">{playerData.gamertag}</div>
                        <div className="details">Accuracy: {playerData.accuracy}%</div>
                        <div className="details">Kills: {playerData.kills.toLocaleString('en-US')}</div>
                        <div className="details">Assists: {playerData.assists.toLocaleString('en-US')}</div>
                        <div className="details">Deaths: {playerData.deaths.toLocaleString('en-US')}</div>
                        <div className="details">K/D Ratio: {playerData.kd_ratio}</div>
                        <div className="details">Damage Dealt: {playerData.damage_dealt.toLocaleString('en-US')}</div>
                        <div className="details">Damage Taken: {playerData.damage_taken.toLocaleString('en-US')}</div>
                        <div className="details">Headshots: {playerData.headshots.toLocaleString('en-US')}</div>
                    </div>
                </div>
                )
            }
        </div>
    )
};

export default Profile;