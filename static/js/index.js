
function addshop(){
    var merchant = localStorage.getItem('merchant');
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                if (merchant === 'True' || merchant==='true'){
                    let shop_name = document.getElementById('shopname').value;
                    let shop_email = document.getElementById('shopemail').value;
                    let address = document.getElementById('address').value;
                    let city = document.getElementById('city').value;
                    let state = document.getElementById('state').value;
                    let pincode = document.getElementById('pincode').value;
                    let country = document.getElementById('country').value;
                    let number = document.getElementById('number').value;
                    let file= document.getElementById('image');
                    let image = file.files[0];
                    let token = localStorage.getItem('access_token');
                    let csrf = document.getElementById('csrf').value;
                    if (shop_name==='' || shop_email ==='' || address==='' || city ==='' || state ==='' || pincode==='' || image===''){
                        return alert('Please Enter all values');
                    }else{
                        const formdata = new FormData();
                        formdata.append('image',image);
                        formdata.append('shop_name',shop_name);
                        formdata.append('shop_email',shop_email);
                        formdata.append('address',address);
                        formdata.append('city',city);
                        formdata.append('state',state);
                        formdata.append('pincode',pincode);
                        formdata.append('country',country);
                        formdata.append('number',number);
                        formdata.append('lat',lat);
                        formdata.append('lng',lng);
                        formdata.append('useremail',localStorage.getItem('id'))
                        fetch('/postshop/',{
                            method : 'POST',
                            headers:{
                                'Authorization':`Bearer ${token}`,
                                'X-CSRFToken':csrf,
                            },
                            body:formdata
                        }).then(result => result.json())
                        .then(response => { 
                            console.log('response:', response);
                            if (response.status===200){
                                console.log(response.msg);
                                window.location.href = '/';
                            }
                            else{
                                alert(response.msg);
                            }
                        })
                        .catch(error => {
                            console.error(error);
                            alert('An error occurred during login. Please try again later.');
                        });
                    }
                }else{
                    return alert('Shop can only be added by merchants');
                }
            },
            error => {
                console.error(error);
                alert('Could not get location. Please enable geolocation and try again.');
            }
        );
    } else {
        console.log('Geolocation is not supported by this browser.');
    }
}

function fetchtoken(){
    let email = localStorage.getItem('id');
    let token = localStorage.getItem('access_token');
    let csrf = document.getElementById('csrf').value;
    let data = {'email':email}
    if (email){
        // alert('5 min done')
        fetch('/login/usertoken/',{
            method : 'POST',
            headers:{
                'Content-Type':'application/json',
                'Authorization':`Bearer ${token}`,
                'X-CSRFToken':csrf,
            },
            body:JSON.stringify(data)
        }).then(result => result.json())
        .then(response => { 
            console.log(response)
            if (response.status === 200){
                localStorage.setItem('access_token',response.access_token);
                localStorage.setItem('id',response.user);
                localStorage.setItem('merchant',response.merchant);
            }else{
                console.log(response.msg)
            }
        })
        .catch(error => {
            console.error(error);
        console.log('An error occurred during login. Please try again later.');
        });
    }
}

setInterval(fetchtoken,240000); 

// function search(){
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(
//             position => {
//                 const lat = position.coords.latitude;
//                 const lng = position.coords.longitude;
//                 let csrf = document.getElementById('csrf').value;
//                 let token = localStorage.getItem('access_token')
//                 let word = document.getElementById('Form_Search').value;
//                 let data = {'word':word,'lat':lat,'lng':lng}
//                 alert(csrf)
//                 fetch('/search/',{
//                     method:'POST',
//                     headers:{
//                         'Content-Type':'application/json',
//                         'Authorization':`Bearer ${token}`,
//                         'X-CSRFToken':csrf,
//                     },
//                     body : JSON.stringify(data)
//                 }).then(result=>result.json())
//                 .then(response => {
//                     alert('dome')
//                     if(response.status===200){
//                         console.log('done')
//                     }
//                 })
//             }
//         )}else{
//             alert('Please allow the location permission')
//         }
// }