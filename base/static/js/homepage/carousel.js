 function nextSlide() {
    $("#pinautos").carousel("next");
  }

function prevSlide() {
    $("#pinautos").carousel("prev");
  }

   
  $(document).ready(function () {
    $("#pinautos").carousel();
    setInterval(nextSlide, 3000);  
  });
 