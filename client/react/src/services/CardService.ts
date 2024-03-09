import $api from '../http'
import { AxiosResponse } from 'axios'


export default class CardService {

    static async hello(): Promise<AxiosResponse<string>> {
        return $api.get<string>('/protected')
    }
    
}

