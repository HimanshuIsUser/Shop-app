

// function addBlogButton(){
//     var csrf = document.getElementById('csrf').value;
//     var token = localStorage.getItem('access_token')
//     if (token){
//         fetch('/add_blog/', {
//             method: 'GET',
//             headers: {
//             'Authorization' : `Bearer ${token}`,
//             'Content-Type': 'application/json'
//             }
//         })
//     }
//     else{
//         alert('Login Requied')
//     }
// }
function login(){
    var username = document.getElementById('loginusername').value;
    var password = document.getElementById('loginpassword').value;
    var csrf = document.getElementById('csrf').value;
    if (username=='' && password==''){
        return alert('Please enter email and password !');
    }else if(username == ''){
        return alert('please Enter the Email ');
    }else if(password == ''){
        return alert('Please Enter your password')
    }

    var data = {
        'email':username,
        'password':password
    }

    fetch('/login/login/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        console.log('response:', response);
        if (response.status === 200){
            localStorage.clear()
            localStorage.setItem('access_token',response.access_token)
            localStorage.setItem('id',response.user)
            localStorage.setItem('merchant',response.merchant)
            window.location.href = '/';
        }
        else{
            console.log('No user Found');
            alert('No User Found');
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during login. Please try again later.');
    });

}

const accessToken = localStorage.getItem('access_token');
const loginButton = document.getElementById('login-button');
const logoutButton = document.getElementById('logout-button');
const addblogcontainer = document.getElementById('addblogContainer')

  if (accessToken) {
    // console.log(accessToken)
    // If an access token is present, show the logout button and hide the login button
    logoutButton.style.display = 'inline-block';
    loginButton.style.display = 'none';
    addblogcontainer.style.display = 'inline-block';

  } else {
    // If no access token is present, show the login button and hide the logout button
    loginButton.style.display = 'inline-block';
    logoutButton.style.display = 'none';
    addblogcontainer.style.display = 'none';
  }

function logout() {
    // Remove the access token from localStorage and hide the logout button
    localStorage.removeItem('access_token');
    localStorage.removeItem('id');
    localStorage.removeItem('merchant');
    logoutButton.style.display = 'none';
    loginButton.style.display = 'inline-block';
    addblogcontainer.style.display = 'none';

}


