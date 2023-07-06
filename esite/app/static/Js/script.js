var modal = document.getElementById("my_modal");
var flex_modal = document.getElementById("loginFlex")
var login = document.getElementById("loginButton");

var span = document.getElementsByClassName("close")[0];

login.onclick = function () {

    modal.style.display = "block";

}
span.onclick = function () {

    modal.style.display = "none";


}
