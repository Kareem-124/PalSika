//----------------------- Login Modal Section---------------------//

// Select the Modal That we want to Display/Hide
var modal = document.getElementById("my_modal");
// Select The login Button 
var login = document.getElementById("loginButton"); 
// Select the close button 'X'
var span = document.getElementsByClassName("close")[0]; 

// Display The Modal When Click on loginButton
login.onclick = function () {
    modal.style.display = "block";
}
// Close the Modal When Click on 'X' Button
span.onclick = function () {
    modal.style.display = "none";
}
