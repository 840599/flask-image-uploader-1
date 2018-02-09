
setInterval(()=>{
  $.getJSON($SCRIPT_ROOT + '/uploads/get/random', {}, function(data) {
        $("#image-frame img").attr("src", data);
      });
}, 7000);
