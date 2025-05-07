let uploadForm=document.getElementById("uploadForm");
uploadForm.addEventListener("submit",async (event)=>{
    event.preventDefault();
    const formData = new FormData(uploadForm);
    const response=await fetch("/api/bulletin",{
        method: "POST",
        body:formData,
      }) 
    const result = await response.json();
    insertElement(result);
    let uploadMessage = document.getElementById("uploadMessage");
    if (uploadMessage) {
      uploadMessage.value = "";
    }
    let fileInput = document.getElementById("uploadFormFile");
    if (fileInput) {
      fileInput.value = null;
    }
})

async function init(){
  const response=await fetch("/api/bulletin",{
    method: "GET",
  }) 
  const result = await response.json();
  createElement(result);
}
init();

function createElement(result){
  if(result["status"]=="success"){
    let root=document.getElementById("messageRoot")
    let res=result["message_data"]
    for(let i=0;i<res.length;i++){
      let div1=document.createElement("div")
      let h3=document.createElement("h3")
      h3.textContent=res[i][0];
      let img=document.createElement("img")
      img.src=res[i][1];
      img.style.width="300px";
      let hr=document.createElement("hr")
      div1.appendChild(h3);
      div1.appendChild(img);
      div1.appendChild(hr);
      root.appendChild(div1);
    }
  }
}

function insertElement(result){
  if(result["status"]=="success"){
    let root=document.getElementById("messageRoot")
    let firstChild = root.firstChild;
    let res=result["message_data"]
    let div1=document.createElement("div")
    if(res[0][0]){
      let h3=document.createElement("h3")
      h3.textContent=res[0][0];
      div1.appendChild(h3);
    }
    if(res[0][1]){
      let img=document.createElement("img")
      img.src=res[0][1];
      img.style.width="300px";
      div1.appendChild(img);
    }
    let hr=document.createElement("hr")
    div1.appendChild(hr);
    root.insertBefore(div1,firstChild);
  }
}