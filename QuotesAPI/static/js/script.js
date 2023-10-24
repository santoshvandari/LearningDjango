let QuotesRead=()=>{
    let url=""
    fetch(url)
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
    })
    
}