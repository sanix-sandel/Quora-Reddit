function getCookie(name) {//Pour le CSRF
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function letcheck(){
    console.log("Let's check")
}
letcheck();
function handleLike(id, action){
    console.log(id)
    console.log('wher is the answer ?')
    const url="api/answer/like/";
    const method="POST"
    
    const data=JSON.stringify({
        id:id,
        action:action
    })
    console.log(data);
    console.log(url);

    const xhr=new XMLHttpRequest()
    const csrftoken=getCookie('csrftoken');
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    
    xhr.onload=function(){
       
        console.log("Liked");
    }
    xhr.send(data)
    return 
}