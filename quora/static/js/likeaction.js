function handleLike(answer, id){
    console.log(answer, id);
    action="like";
    const url="upvote/"+id+"/"+action+"/";
    const method="POST"
    const data=JSON.stringify({
        id:id
    })
    console.log(data);
    console.log(url);
/*
    const xhr=new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
   // xhr.setRequestHeader("X-CSRFToken", csrftoken)
    
    xhr.onload=function(){
        const result=xhr.response;
        result=result.response;
        console.log("click");
    }*/
   // xhr.send(data)
    console.log("clicked")
}