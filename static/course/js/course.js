var qq = document.getElementById("qq");
console.log(qq);
var li = document.querySelector("#my-ul").querySelectorAll("li");

function dy(m) {
    li[m].onclick = function() {
        qq.innerText = li[m].querySelector("a").innerText;
    }
}
for (i = 0; i < li.length; i++) {
    dy(i);
}