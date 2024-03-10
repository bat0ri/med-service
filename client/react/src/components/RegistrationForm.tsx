import React, { FC, useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { Context } from '..';
import TopBar from './TopBar';

const RegistrationForm: FC = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');

  const { store } = useContext(Context);

  return (
    <div className='dark:bg-black h-screen'>
      <TopBar pageName='Страница регистрации' />
      <div className='max-w-md mx-auto my-10 p-6 bg-slate-500/20 rounded-md shadow-md'>
        <h2 className='text-2xl font-semibold mb-6 text-center dark:text-white'>Регистрация</h2>
        <div className='mb-4'>
          <label htmlFor='email' className='block mb-2 text-gray-800 dark:text-white'>
          Электронная почта:
          </label>
          <input
            type='text'
            id='email'
            placeholder='Электронная почта'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className='w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 dark:bg-slate-700 dark:text-white'
            autoComplete='off'
          />
        </div>
        <div className='mb-6'>
          <label htmlFor='password' className='block mb-2 text-gray-800 dark:text-white'>
            Пароль:
          </label>
          <input
            type='password'
            id='password'
            value={password}
            placeholder='Пароль'
            onChange={(e) => setPassword(e.target.value)}
            className='w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 dark:bg-slate-700 dark:text-white'
            autoComplete='off'
          />
        </div>
        <button onClick={() => store.registration(email, password)} className='w-full bg-blue-500 text-white font-semibold py-2 px-4 rounded-md focus:outline-none hover:bg-blue-600'>
          Register
        </button>
        <div className='mt-4 text-center'>
          <Link to='/login' className='text-blue-500 hover:underline'>
            У меня есть аккаунт
          </Link>
        </div>
      </div>
    </div>
  );
};

export default RegistrationForm;
