// função para extrair info básicas do usuário
export const getUser = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user.trim()}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

// função para extrair info básicas dos repositórios do usuário
export const getRepos = async (user) => {
    try { 
        const data = await fetch(`https://api.github.com/users/${user.trim()}/repos`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

// função para extrair estatísticas básicas do usuário
export const getUserStatistics = async (user) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/github/${user.trim()}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

// função para extrair estatísticas básicas de um repositório específico do usuário
export const getRepoStatistics = async (user, repo) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/github/${user}/${repo}`)
        return data.json()
    } catch (error) {
        console.log(error)
    }
}

// função para extrair gráfico de commits de um repositório específico do usuário
export const getRepoGraphCommits = async (owner, repo) => {
    try { 
        const data = await fetch(`http://127.0.0.1:8000/grafico/${owner}/${repo}`)
        const blob = await data.blob()
        return URL.createObjectURL(blob)
    } catch (error) {
        console.log(error)
    }
}

// função para extrair gráfico de commits do usuário
export const getUserGraphCommits = async(user) =>{
    try { 
        const data = await fetch(`http://127.0.0.1:8000/grafico/${user.trim()}`)
        const blob = await data.blob()
        return URL.createObjectURL(blob)
    } catch (error) {
        console.log(error)
    }
}

// função para gerar relatório em pdf do usuário
export const getUserPdf = async(user) =>{
    try { 
        const data = await fetch(`http://127.0.0.1:8000/relatorio/${user.trim()}`)
        const blob = await data.blob()
        const url = window.URL.createObjectURL(blob)
        const link = document.createElement("a")
        link.href=url
        link.download="Relatorio Usuário.pdf"
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        window.URL.revokeObjectURL(url)
    } catch (error) {
        console.log(error)
    }
}

// função para gerar relatório em pdf de um repositório específico do usuário
export const getReposPdf = async(user, repo) =>{
    try { 
        const data = await fetch(`http://127.0.0.1:8000/relatorio/${user.trim()}/${repo}`)
        const blob = await data.blob()
        const url = window.URL.createObjectURL(blob)
        const link = document.createElement("a")
        link.href=url
        link.download=`Relatorio ${repo}.pdf`
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        window.URL.revokeObjectURL(url)
    } catch (error) {
        console.log(error)
    }
}