import { createContext, useContext, useState } from "react";

const UserContext = createContext(undefined)

export const UserProvider = ({children}) => {
    const [userData, setUserData] = useState(null)
    const [userRepos, setUserRepos] = useState(null)

    return(
        <UserContext.Provider value={{userData, setUserData, userRepos, setUserRepos}}>
            {children}
        </UserContext.Provider>
    )
}

export const useUser = () => {
    const context = useContext(UserContext)
    return context
}