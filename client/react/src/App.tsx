import React, { useContext, useEffect, useState } from 'react';
import './tailwindcss.css'
import LoginForm from './components/LoginForm';
import RegistrationForm from './components/RegistrationForm';
import { Context } from '.';
import { observer } from 'mobx-react-lite';

import { User } from './models/User';

import { Routes, Route } from 'react-router-dom';
import DoctorHome from './components/DoctorHome';




function App() {
    
    const {store} = useContext(Context);
    const [users, setUsers] = useState<User[]>([]);

    //useEffect(() => {
    //    if (localStorage.getItem('access')) {
    //        store.checkAuth()
    //    }
    //}, [])

    if(store.isLoading) {
        return(
        <div>Загрузка</div>
        )
    }



    if(!store.isAuth) {
        return (
            <div>
                <Routes>
                    <Route path='/login' element={<LoginForm/>}></Route>
                    <Route path='/singup' element={<RegistrationForm/>}></Route>
                </Routes>
            </div>
        )
    }
    
  return (
    <div className="App">
        <Routes>
            <Route path='/home' element={<>Home</>}/>
            <Route path="/profile" element={<DoctorHome/>}/>
        </Routes>
    </div>
  );
}

export default observer(App);
