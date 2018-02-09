document.addEventListener("DOMContentLoaded", () => {
  if ( CURRENT_PAGE_ID.length ) {
      $("#"+CURRENT_PAGE_ID).addClass("active");
      $("#"+CURRENT_PAGE_ID).attr("href", "#");
  }
});
