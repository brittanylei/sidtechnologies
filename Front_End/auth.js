var Firebase = require('firebase');

module.exports = {
  auth: null,
  init: function (callback) {
    var config = {
      apiKey: "AIzaSyDX8In6v77C3gMQB6L99mF2PQyLBtul28g",
      authDomain: "silver-surfer-services.firebaseapp.com",
      databaseURL: "https://silver-surfer-services.firebaseio.com",
      projectId: "silver-surfer-services",
      storageBucket: "silver-surfer-services.appspot.com",
      messagingSenderId: "272241968147"
    };
    Firebase.initializeApp(config);
    var dbRef = Firebase.database();
    var usersRef = dbRef.ref('users')
    
    this.auth = Firebase.auth();
    this.auth
      .onAuthStateChanged(function(user) {
        if(callback){
          callback();
        }
      })

    return this;
  },

  checkLoggedInUser: function(){
    return this.auth.currentUser
  },
  



  logout: function () {
    this.auth
      .signOut()
      .then(function () {
        return true;
      })
      .catch(function (e) {
        return false;
      })
  },
  login: function (type, data) {
    var auth = Firebase.auth();
    var request = null;
    //in case want to add different login schema such as twitter, google, or fb
    switch(type){
      case 'email': {
        request = auth.signInWithEmailAndPassword(data.email, data.password)
        break;
      }
    }
    if( request !== null ){
      return request
        .then(this.resultHandler)
        .catch(this.errorHandler);
    } else {
      console.log('No Method Found');
      return null;
    }
  },

  resultHandler: function (user) {
    console.log(user)
    return user;
  },

  errorHandler: function (err) {
    console.error(err);
    return false;
  }
}