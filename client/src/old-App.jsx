import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

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
    const res = await fetch("/registration/logout/", {
      credentials: "same-origin", // include cookies!
    });

    if (res.ok) {
      // navigate away from the single page app!
      window.location = "/registration/sign_in/";
    } else {
      // handle logout failed!
    }
  }


  return (
    <>
      <div> 
        Hello World {user ? user.first_name : "Anonymous"} 
      </div>
      <a href="/registration/logout">Sign In</a>
    </>
  )
}

export default App;
