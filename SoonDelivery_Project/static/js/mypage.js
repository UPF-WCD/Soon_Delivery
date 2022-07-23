function setThubnail(event){
  let reader = new FileReader();

  reader.onload = function(event){
    let img = document.getElementById('profile-img');
    img.setAttribute("src", event.target.result);
  };

  reader.readAsDataURL(event.target.files[0]);
}