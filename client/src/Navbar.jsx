import React from 'react';
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';
import './App.css';

const Navbar = () => {

  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch('/getUserData')
      .then(res => res.json())
      .then(data => {
        setUser(data);  
      });
      console.log(user);
  }, []);

  async function logout() {
    const res = await fetch("registration/logout/", {
      credentials: "same-origin", // include cookies!
    });

    if (res.ok) {
      window.location = "/registration/sign_in/";
    } else {
      window.location = "/registration/sign_in/";
    }
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <Link className="navbar-brand" to="/">Halo Player Tracker</Link>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse navbar-nav ml-auto" id="navbarNav">
          <li className="nav-item">
            <Link className="nav-link" to="/">Home</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/account">Account Settings</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/profile">Profile</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" onClick={logout}>Logout</Link>
          </li>
      </div>
    </nav>
  );
}

export default Navbar;