
console.log("loaded");
const uploadBox =  document.querySelector(".upload-box");
const fileName = document.querySelector(".file-name");
const fileInput = document.querySelector("#file")


// check for file submission and output the file name
fileInput.addEventListener("change", function(){
    console.log("change event happened");
    if (fileInput.files.length > 0) {
        console.log("there is file");

        const file = fileInput.files[0];
        fileName.textContent = file.name;
    }
});

uploadBox.addEventListener("dragover", function(event){
    console.log("DRAGOVER FIRED");
    event.preventDefault();
    uploadBox.classList.add("drag-active");   
});

uploadBox.addEventListener("dragleave", function(event){
    event.preventDefault();
    uploadBox.classList.remove("drag-active");   
});

uploadBox.addEventListener("drop", function(event){
    event.preventDefault();
    uploadBox.classList.remove("drag-active");

    const file = event.dataTransfer.files[0];
    if (!file) {
    return; 
    }

    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;
    fileName.textContent = file.name;

});
