import React, { FC, useContext, useState } from 'react';
import { Context } from '..';
import { observer } from 'mobx-react-lite';
import { useNavigate, Link } from 'react-router-dom';
import TopBar from './TopBar';


const LoginForm: FC = () => {
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const navigate = useNavigate();

    const {store} = useContext(Context);

    const handleLogin = async () => {
        try {
            await store.login(email, password);
            if (store.isAuth && store.user.role && store.user.role === 'DOCTOR') {
                navigate('/profile');
            } else {
                console.log('FAIL', store.isAuth)
            }
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
            <TopBar pageName='Сервис Поликлиники, Добро пожаловать!'/>
            <div className="max-w-md mx-auto my-10 p-6 bg-slate-500/20 dark:bg-slate-900 rounded-md shadow-md">
                <h2 className="text-2xl font-semibold mb-6 text-center dark:text-white">Вход</h2>
                <div className="mb-4">
                    <label htmlFor="username" className="block mb-2 text-gray-800 dark:text-white">Электронная почта:</label>
                    <input
                        type="text"
                        id="username"
                        placeholder='Электронная почта'
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        className="w-full px-4 py-2 rounded-md focus:outline-none focus:py-4 dark:bg-slate-700 dark:text-white"
                        autoComplete="off"
                    />
                </div>
                <div className="mb-6">
                    <label htmlFor="password" className="block mb-2 text-gray-800 dark:text-white">Пароль:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        placeholder='Пароль'
                        onChange={e => setPassword(e.target.value)}
                        className="w-full px-4 py-2 rounded-md focus:outline-none focus:py-4 dark:bg-slate-700 dark:text-white"
                        autoComplete="off"
                    />
                </div>
                <button onClick={handleLogin} className="w-full bg-blue-500 text-white font-semibold py-2 px-4 rounded-md focus:outline-none hover:bg-blue-600">
                    Войти
                </button>
                <div className="mt-4 text-center">
                    <Link to="/singup" className="text-blue-500 hover:underline">Зарегистрироваться</Link>
                </div>
            </div>
        </div>
    );
};

export default observer(LoginForm);
