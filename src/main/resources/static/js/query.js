$( document ).ready(function() {
    $('#begin').fadeIn(1500);
    var flag=document.getElementById("result").innerHTML;
    console.log(flag);
    if (flag){
        if (flag=='true'){
            showResults('Attention Attention!!<br><br><br>You are in grave danger. Here is the best Doctor in Universe. You should visit him.');
            document.getElementById('infected').style.display='block';
        }
        else{
            showResults('Everything is allright. You have nothing to fear!');
            document.getElementById('disinfected').style.display='block';
        }
        showResults("<br><br><br>Thank you for using our services.");
    }
});

function showResults(message){
    document.getElementById('resultBlock').style.display='flex';
    var msg=document.getElementById('message');
    msg.innerHTML+=message;
    msg.style.lineHeight
};

function validateForm() {
    var alertmsg1 = "You must fill the following required fields";
    var alertmsg2 = "";
    var d = document.getElementById('age').value;
    if (d === "" || /^[0-9||]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour Age";
    }
    d = document.getElementById('sex').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Sex";
    }
    d = document.getElementById('cp').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Chest Pain";
    }
    d = document.getElementById('bp').value;
    if (d === "" || /^[0-9||]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour Blood Pressure";
    }
    d = document.getElementById('chol').value;
    if (d === "" || /^[0-9||]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour Cholesterol";
    }
    d = document.getElementById('fbs').value;
    if (d === "" || /^[0-9||]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour Blood Sugar";
    }
    d = document.getElementById('restecg').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Electrocardiographic results";
    }
    d = document.getElementById('thalach').value;
    if (d === "" || /^[0-9||]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour Maximum Heart Rate";
    }
    d = document.getElementById('exang').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Exercised induced angina";
    }
    d = document.getElementById('oldPeak').value;
    if (d === "" || /^[0-9||.]+$/.test(d) === false) {
        alertmsg2 = alertmsg2 + "\nYour ST depression";
    }
    d = document.getElementById('slope').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Slope of ST segment";
    }
    d = document.getElementById('ca').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Number of major vessels";
    }
    d = document.getElementById('thal').value;
    if (d === "0" ) {
        alertmsg2 = alertmsg2 + "\nYour Thal";
    }

    if (alertmsg2 != "") {
        alert(alertmsg1 + alertmsg2);
        return false;
    }
    else{
        // epeidh einai boolean sth java petaei error. Ara to ftiaxnw apo edw an ola einai swsta
        document.getElementById('fbs').value=d>120?1:0;
        return true;
    }

}
