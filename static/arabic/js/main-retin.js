const upp =document.querySelector(".upp");
const fileName =document.querySelector(".file-name");
const cancelBtn =document.querySelector(".cancel-btn");
const defaultBtn =document.querySelector(".default-btn"); 
const custBtn =document.querySelector(".custom-btn");
const img =document.querySelector(".img2");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
function defaultBtnActive(){
defaultBtn.click();
}
defaultBtn.addEventListener("change",function(){
    const file = this.files[0];
    
if(file){
    const reader = new FileReader();
    reader.onload=function(){
        const result = reader.result;
        img.src= result;
        upp.classList.add("active");
    }
    cancelBtn.addEventListener("click",function(){
        img.src =" ";
        upp.classList.remove("active");
    });
    reader.readAsDataURL(file);
}
if(this.value){
    let valueStore = this.value.match(regExp);
    fileName.textContent = valueStore;
}
});