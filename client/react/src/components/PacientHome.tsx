import React, { FC, useContext, useState } from 'react';
import { Context } from '..';
import { observer } from 'mobx-react-lite';
import { useNavigate, Link } from 'react-router-dom';
import TopBar from './TopBar';


const PacientHome: FC = () => {



    const {store} = useContext(Context);


    return (
        <div>

        </div>
    );
};

export default observer(PacientHome);
