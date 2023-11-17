setInterval(() => {
    fetch("/data/update")
    .then(response => response.json())
    .then(data => {
        const press = data["Pressure"];
        console.log(press)
        const max_press = 1200;
        const deg = press - 960;
        document.querySelector(".gauge .pointer .hand").style.transform = `rotate(${deg}deg)`;
    })
    
}, 200);