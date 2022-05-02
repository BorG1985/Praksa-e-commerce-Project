function Myfunction1(btnId) {
var targetDiv1 = document.getElementById("parent1");
var targetDiv2 = document.getElementById("parent2");
var targetDiv3 = document.getElementById("parent3");

    if (btnId == "btn1") {
        targetDiv1.style.display = "block";
        targetDiv2.style.display = "none";
        targetDiv3.style.display = "none";
        document.getElementById("parent1").scrollIntoView();
    }
    else if (btnId == "btn2"){
        targetDiv1.style.display = "none";
        targetDiv2.style.display = "block";
        targetDiv3.style.display = "none";
        document.getElementById("parent2").scrollIntoView();
    }
    else if (btnId == "btn3") {
        targetDiv1.style.display = "none";
        targetDiv2.style.display = "none";
        targetDiv3.style.display = "block";
        document.getElementById("parent3").scrollIntoView();
    }
}

  

