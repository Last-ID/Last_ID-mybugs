window.onload=function () {
    var hitokoto = document.querySelector('.hitokoto');
    var from = document.querySelector('.from');
    update();
    function update() {
        gethi = new XMLHttpRequest();
        gethi.open("GET","https://international.v1.hitokoto.cn/?c=i");
        gethi.send();
        gethi.onreadystatechange = function () {
            if (gethi.readyState===4 && gethi.status===200) {
                var Hi = JSON.parse(gethi.responseText);
                hitokoto.innerHTML = "<b>" + Hi.hitokoto;
                from.innerHTML = "——<b>" + Hi.from + "_" + Hi.from_who; 
            }
        }
    }
}
