var tablinks=document.getElementsByClassName("tab-links");
var tabcontents=document.getElementsByClassName("tab-contents");

function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove("active-link")
    }
    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab")
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}



// var typed = new typed('.text', {
//     Strings:["Frontend Developer" , "Web"],
//     typeSpeed:100,
//     backSpeed:100,
//     backDelay:2000,
//     loop:true
// })


var header = document.querySelector("#header");
var cursor = document.querySelector("#cursor");
header.addEventListener("mousemove",function (dets) {
    console.log("hello")
    gsap.to(cursor,{
        x:dets.x,
        y:dets.y
    })
    
})

header.addEventListener("mouseenter",function () {
    gsap.to(cursor,{
        scale:1,
        opacity:1
    })
})
header.addEventListener("mouseleave",function () {
    gsap.to(cursor,{
        scale:0,
        opacity:0
    })
})