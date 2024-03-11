const color = (min,max)=> Math.floor(Math.random()*(max-min)+min)
setInterval(()=>{
    // document.querySelector(".main").style.backgroundColor=`rgb(${color(0,255)},${color(0,255)},${color(0,255)})`
},100)

console.log("Hello World")
setTimeout(()=>{
    document.querySelector(".message").textContent=""
},5000)