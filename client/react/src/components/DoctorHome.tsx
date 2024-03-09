import React, { FC, useContext, useState } from 'react';
import { Context } from '..';
import { observer } from 'mobx-react-lite';
import { useNavigate, Link } from 'react-router-dom';
import TopBar from './TopBar';
import CardService from '../services/CardService';


const DoctorHome: FC = () => {



    const {store} = useContext(Context);

    const handleProtected = async () => {
        try {
            const response = CardService.hello();
            console.log(response);
        } catch (e: any) {
            if ('response' in e && e.response?.data?.message) {
                console.log(e.response.data.message);
            } else {
                console.log('An error occurred:', e);
            }
        }
    };

    return (
        <div className='dark:bg-black h-screen'>
            <TopBar pageName='Сервис Медкарт'/>
            <button onClick={handleProtected} className="w-full bg-blue-500 text-white font-semibold py-2 px-4 rounded-md focus:outline-none hover:bg-blue-600">
                   Hello
            </button>
        </div>
    );
};

export default observer(DoctorHome);
