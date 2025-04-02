export const getUser = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

export const getRepos = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user}/repos`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}