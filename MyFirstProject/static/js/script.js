const color = (min,max)=> Math.floor(Math.random()*(max-min)+min)
setInterval(()=>{
    // document.querySelector(".main").style.backgroundColor=`rgb(${color(0,255)},${color(0,255)},${color(0,255)})`
},100)

document.querySelector(".message")
console.log("connected.")