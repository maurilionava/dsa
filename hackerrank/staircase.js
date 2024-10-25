function staircase(n) {
    let string = ''

    for(let i=1; i<=n; i++){
        string = `${' '.repeat(n-i)}${'#'.repeat(i)}`
        console.log(string)
    }
}

staircase(6)