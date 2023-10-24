document.getElementById("btn-fetch").addEventListener("click",FetchData);
// function FetchData(){
//     console.log("Fetching data");
//     const url = "api/quotes/";
//     fetch(url)
//     .then(response=>response.json())
//     .then(response=>{
//         console.log(response)
//         // document.querySelector("#fetch-result").innerHTML=JSON.stringify(response);
//         document.querySelector("#fetch-result").textContent=response[0].quotes;
//         document.querySelector("#author").textContent=" - "+response[0].author;
//     }).catch(e=>{
//         console.log(e);
//     })
// }
FetchData();

function FetchData()
let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://randomjokesapi.santosh0.com.np/JokesAPI/');
        xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let data = JSON.parse(xhr.responseText);
            console.log(data);
            }
        };
        xhr.send();