
document.addEventListener("DOMContentLoaded", () => {
  // Auto submit the form when you select a file
  $("#input-file").on("change", ()=>{
    document.forms.uploadfile.submit();
  });
});
