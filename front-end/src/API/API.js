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

export const getUserStatistics = async (user) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/github/${user.trim()}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

export const getRepoStatistics = async (user, repo) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/github/${user}/${repo}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

export const getRepoGraphCommits = async (owner, repo) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/grafico/${owner}/${repo}`)
        const blob = await data.blob()
        return URL.createObjectURL(blob)
    } catch (error) {
        console.log(error)
    }
}

export const getUserGraphCommits = async(user) =>{
    try { 
        const data = await fetch(`http://127.0.0.1:8000/grafico/${user.trim()}`)
        const blob = await data.blob()
        return URL.createObjectURL(blob)
    } catch (error) {
        console.log(error)
    }
}