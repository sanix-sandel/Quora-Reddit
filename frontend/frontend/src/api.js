const url='http://127.0.0.1:8000/api/questions-list/'

const fetchquestions=async()=>{
    return fetch(url, {})
    .then(res=>res.json())
    .then(data=>{
        console.log(data);
        return data
        
    });
}
export default fetchquestions;
