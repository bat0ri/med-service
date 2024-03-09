import $api from '../http'
import { AxiosResponse } from 'axios'
import { AuthResponce, RegistrationResponce } from '../models/response/AuthResponce'
import { User } from '../models/User'


export default class AuthService {
    
    static async login(email: string, password: string): Promise<AxiosResponse<AuthResponce>> {
        return $api.post<AuthResponce>('/auth/login', {email, password},)
    }

    static async registration(email: string, password: string): Promise<AxiosResponse<User>> {
        const role = 'PACIENR'
        return $api.post<User>('/auth/registration', {email, password, role});
      }
      

    static async logout(): Promise<void> {
        return $api.post('/auth/logout')
    }
}

