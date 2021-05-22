const games = document.getElementById('games')
var frag = document.createDocumentFragment();
$.ajax({
type: 'GET',
url: '/games-json',
success: function(response){
    for (const item of response){
        var option = document.createElement("OPTION");
        option.textContent = item;
        option.value = item;
        frag.appendChild(option);
    }
    games.appendChild(frag)
},
error: function(response){
    console.log(response)
  }
})

function openTab(index) {
    var i, x;
    x = document.getElementsByClassName("details");
    for (i = 0; i < x.length; i++) {
      x[i].classList.add("not-visible");
    }
    $("#dets"+index).removeClass("not-visible")
    $('html,body').animate({
        scrollTop: $("#dets"+index).offset().top},
        100);
}