// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return response.json();
  }


sendButton.addEventListener("click", async ()=>{
    questionInput=document.getElementById("questionInput").value;
    document.getElementById("questionInput").value="";
    document.querySelector(".right_q").style.display="block"
    document.querySelector(".right").style.display="none";
    question1.innerHTML=questionInput;
    question2.innerHTML=questionInput;

    let res=await postData("/api",{"question":questionInput});
    solution.innerHTML=res.result;

})