export const getUser = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user.trim()}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

export const getRepos = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user.trim()}/repos`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}