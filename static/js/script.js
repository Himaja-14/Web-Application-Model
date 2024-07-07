//Menu Toggle 
let menutoggle = document.querySelector('.menutoggle');
let navigation = document.querySelector('.navigation');
let section = document.querySelector('.sec')
    menutoggle.onclick = function () {
        navigation.classList.toggle('active')
        section.classList.toggle('active')
    }

let list = document.querySelectorAll('.list');
    function activelink(){
        list.forEach((item) => 
        item.classList.remove('active'));
        this.classList.add('active');
        section.classList.toggle('zind')
    }
    list.forEach((item) =>
    item.addEventListener('click', activelink));


let dropdown = document.querySelector('.dropdown');
    dropdown.onclick = function(){
        dropdown.classList.toggle('active');
    }

    function show(a){
        document.querySelector('.text02').value = a;
    } 

function profiletoggle(){
    const togglemenu = document.querySelector('.menu')
    togglemenu.classList.toggle('active')
}

