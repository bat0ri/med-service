import { User } from "../User"

export interface AuthResponce {
    token: string
    user: User
}

export interface RegistrationResponce {
    user: User
}