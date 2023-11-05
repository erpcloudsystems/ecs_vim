// congratz
document.getElementById("nav_link").addEventListener("click", function(e){
    hashMap = {
        "1": ".one",
        "2": ".two",
        "3": ".three",
        "4": ".four",
    }
    if (e.target.matches("li")){
        let currentLi = document.getElementById(e.target.id)
        currentLi.classList.toggle("underline")
        let rowGallery = document.querySelector(hashMap[e.target.id])
        rowGallery.classList.toggle("show")
        let curLis = document.getElementById("nav_link").children
        for (let element of curLis) {
            if (!(element.id == e.target.id)) {
                let cur_li = document.getElementById(element.id)
                cur_li.classList.remove("underline")
            }
        }
        let curdivs = document.querySelectorAll(".gallery")
        for (let i = 0; i < curdivs.length; i++) {
            if (!(e.target.id == i +1)) {

                curdivs.item(i).classList.remove("show")
            }
          }
        

    }
})