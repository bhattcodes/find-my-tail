
document.querySelectorAll(".where").forEach((element) => {



    element.addEventListener("click", () => {
        
        document.querySelectorAll(".where").forEach((e) => {
            e.classList.remove("active");
        })
        element.classList.add("active");
    })
});

document.querySelectorAll(".season").forEach((element) => {



    element.addEventListener("click", () => {
        
        document.querySelectorAll(".season").forEach((e) => {
            e.classList.remove("active");
        })
        element.classList.add("active");
    })
});


document.querySelectorAll(".occasion").forEach((element) => {



    element.addEventListener("click", () => {
        
        document.querySelectorAll(".occasion").forEach((e) => {
            e.classList.remove("active");
        })
        element.classList.add("active");
    })
});


document.querySelector(".submit").addEventListener("click",()=>{

    var a=[];
    document.querySelectorAll(".active").forEach((e)=>{a.push(e.innerHTML)})

    var my_json = {
        "sad_happy": document.getElementById("sad_happy").value,
        "stressed_relaxed": document.getElementById("stressed_relaxed").value,
        "lonely_romantic": document.getElementById("lonely_romantic").value,
        "couchpotato_party": document.getElementById("couchpotato_party").value,
    
        "where": a[0],
        "season": a[1],
        "occasions": a[2]
    
    };

    console.log(my_json);




})