$(document).ready(function () {
  //Initialize the Firebase App
  Auth.init(authStateRouter);

var config = {
      apiKey: "AIzaSyDX8In6v77C3gMQB6L99mF2PQyLBtul28g",
      authDomain: "silver-surfer-services.firebaseapp.com",
      databaseURL: "https://silver-surfer-services.firebaseio.com",
      projectId: "silver-surfer-services",
      storageBucket: "silver-surfer-services.appspot.com",
      messagingSenderId: "272241968147"
  };
  firebase.initializeApp(config);

  //create firebase references
  var Auth = firebase.auth();
  var dbRef = firebase.database();
  var usersRef = dbRef.ref('users')
  var auth = null;

var $ = require('jquery');
var Auth = require('./auth')

//Error box indexes
var errorIndex = 0;

//Login Wrapper
var login = function(type, data){
  return Auth.login(type, data);
};

//Redirect to some Page or URL
var redirect = function(to) {
  window.location = to;
}

//Redirect to Home
var redirectToHome = function(user) {
  if(user){
    redirect('index1.html');
  }
}

//Redirect to Main
var redirectToLogin = function(user) {
  if(!user){
    redirect('index.html');
  }
}

//Error show and hide controller, will be using the ErrorIndex
var showError = function(errorObject){

}

//Gets the currently open page, can evolve to a router
var currentPage = function(){
  var page = window.location.pathname.split('/')
  page = page[page.length - 1].replace('\.html', '');
  console.log(page)
  return page == '' ? 'index' : page;
}

//Function to ensure the redirects on user auth state
var authStateRouter = function(){
  console.log('Auth Router')
  //Check and Set the user status
  var user = Auth.checkLoggedInUser();

  if( user === null ){ //User is not logged in
    if( currentPage() !== 'login' ){//IF user is not on login page
      //Open the login page
      redirectToLogin(user)
    }
  } else { //User is logged in
    //Check if page is login page
    if( currentPage() === 'login' ){//User is on login page
      //Redirect to the Home page
      redirectToHome(user);
    } else { //User is not on login page
      //Show and Hide the appropriate button in the Header
      $('.logout-link').show();
      $('.login-link').hide();
    }
  }
}

$('#register').on('click', function(e){
  e.preventDefault();
  var data = {
  	email: $('#regEmail').val(),
  	firstName: $('#regFirstName').val(),
  	lastName: $('#regLastName').val(),
  	}
  console.log(data);
  $('#regEmail, #regPassword').val('')
  Auth.register(data).then(redirectToHome)
})
  
/*
  var passwords = {
  	password : $('#regPassword').val(),
  	cPassword : $('#regCPassword').val(),
  	}
  	if((data.email != '' )&&(passwords.password != '' )&&( passwords.cPassword != '')){
  		if( passwords.password == passwords.cPassword ){
 		 	firebase.auth().createUserWithEmailAndPassword(data.email, passwords.password).then(function(user){
 		  //now user is needed to be logged in to save data
            console.log("Authenticated successfully with payload:", user);
            auth = user;
            //now saving the profile data
            usersRef
              .child(user.user_id)
              .set(data)
              .then(function(){
                console.log("User Information Saved:", user.user_id);
              })
	     },
	 */

  //Logout Button
  $('.logout-link').on('click', function (e) {
    if( Auth.logout() ){
      redirectToLogin();
    }
  }),

  //Email Auth Scheme Login
  $('#login').on('click', function(e) {
    e.preventDefault();
    var data = {email: $('#email').val(), password: $('#password').val()}
    console.log(data);
    $('#email, #password').val('')
    login('email', data).then(redirectToHome)
  })
})
