
function register(){
    let email = document.getElementById('email').value;
    let name= document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let merchant = document.getElementById('merchantId').checked;
    
    var csrf = document.getElementById('csrf').value;

    if (email == ''){
        return alert('Email is required')
    }
    else if(password==''){
        return alert('Password is required')
    }
    var data = {
        'email' : email,
        'password':password,
        'name':name,
        'merchant':merchant
    }
    fetch('/login/register/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        if (response.status === 200){
            localStorage.clear()
            localStorage.setItem('access_token',response.access_token)
            localStorage.setItem('id',email)
            if (response.merchant==true){
                localStorage.setItem('merchant',response.merchant)
            }
            window.location.href = '/';
        }
        else{
            alert(response.msg);
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during registration. Please try again later.');
    });
}