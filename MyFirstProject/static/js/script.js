const color = (min,max)=> Math.floor(Math.random()*(max-min)+min)
GeneratedColor=`rgb(${color(0,255)},${color(0,255)},${color(0,255)})`
setInterval(()=>{
    document.querySelector(".main").style.backgroundColor=GeneratedColor
},100)