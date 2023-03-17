console.log("I'm connected!")

const createAStudent = (event) => {
    event.preventDefault();

    let studentName = document.getElementById("name").value
    let studentEmail = document.getElementById("email").value
    console.log(studentName, studentEmail)
   
    axios.post("student/", {
        name : studentName,
        email : studentEmail
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        if(response.data.success){
            // window.location.reload()
            let holder = document.getElementById("studentHolder")
            let li = document.createElement("li")
            li.innerHTML = `${studentName} - ${studentEmail}`
            li.classList.add("newItem")
            holder.appendChild(li)
        }
        else{
            alert("incorrect input")
        }
    })
}