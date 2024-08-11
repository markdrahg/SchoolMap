document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('alert_body').style.display='none';  
    document.getElementById('login_display').style.display='none';
});


// The SignUp Alert display 

document.getElementById('load-books-button').addEventListener('click', function() {
    document.getElementById('alert_body').style.display='block';
});

document.getElementById('closeButton').addEventListener('click', function() {
    document.getElementById('alert_body').style.display='none';
});

document.getElementById('okButton').addEventListener('click', function() {
    // document.getElementById('alertPopup').classList.add('hidden');
    document.getElementById('alert_body').style.display='none';

});


//  The Login Form Display Handler

document.getElementById('login_btn').addEventListener('click', function() {
    document.getElementById('login_display').style.display='block';
});

document.getElementById('login_btn2').addEventListener('click', function() {
    document.getElementById('login_display').style.display='block';
});

document.getElementById('close_login').addEventListener('click', function() {
    document.getElementById('login_display').style.display='none';
});


//  The SignUp Form Display Handler

document.getElementById('signUp_link').addEventListener('click', function() {
    document.getElementById('signUp_display').style.display='block';
});

document.getElementById('close_signUp').addEventListener('click', function() {
    document.getElementById('signUp_display').style.display='none';
});


//  nav_signUp onclick function

document.getElementById('nav_signUp').addEventListener('click', function() {
    document.getElementById('login_display').style.display='none';
    document.getElementById('signUp_display').style.display='block';
});


//  nav_logIn onclick function

document.getElementById('nav_logIn').addEventListener('click', function() {
    document.getElementById('signUp_display').style.display='none';
    document.getElementById('login_display').style.display='block';
});