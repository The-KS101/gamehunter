
  const spinnerBox =document.getElementById('spinner-box')
  const dataBox = document.getElementById('data-box')
  const games = document.getElementById('games')
  const img = document.getElementById('hold_images')
  const buttonRight = document.getElementById('slideRight');
  const buttonLeft = document.getElementById('slideLeft');
  var frag = document.createDocumentFragment();
  const gameName= "{{gameShowing}}".replace("#", "");
  let width = screen.width -75;

  $(document).on("click", '.right',function(){
    $('#hold_images').animate({scrollLeft: '+='+width}, 300);
  });
  $(document).on("click", '.left', function(){
    $('#hold_images').animate({scrollLeft: '-='+width}, 300);
  });

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
      dataBox.innerHTML = '<p>Failed to get Similar Games, please try again later.</p>'
    }

  })
        

      //Sorting functions
      function dsc_sort_rating(a, b){ return ($(b).data("rating")) > ($(a).data("rating")) ? 1 : -1; }
      function asc_sort_name(a, b){ return ($(b).data("name")) < ($(a).data("name")) ? 1 : -1; }
      function dsc_sort_date(a, b){ return ($(b).data("release")) > ($(a).data("release")) ? 1 : -1; }
      function dsc_sort_sim(a, b){ return ($(b).data("similarity")) < ($(a).data("similarity")) ? 1 : -1; }
      
      
      
      // Sort by Rating
      
      jQuery.fn.sortDivsDscR = function sortDivsDscR() {
          $(".games_div", this[0]).sort(dsc_sort_rating).appendTo(this[0]);
      }
      $('#Rating').on('click', function(){
          $("#hold_images").sortDivsDscR();
          $('#Rating').addClass("sort-select");
          $('#Name').removeClass("sort-select");
          $('#Release').removeClass("sort-select");
          $('#Similarity').removeClass("sort-select");
      });

      // sort by name
      
      jQuery.fn.sortDivsAscN = function sortDivsAscN() {
          $(".games_div", this[0]).sort(asc_sort_name).appendTo(this[0]);
      }
      $('#Name').on('click', function(){
          $("#hold_images").sortDivsAscN();
          $('#Name').addClass("sort-select");
          $('#Rating').removeClass("sort-select");
          $('#Release').removeClass("sort-select");
          $('#Similarity').removeClass("sort-select");
      });

      // sort by date

      jQuery.fn.sortDivsDscD = function sortDivsDscD() {
          $(".games_div", this[0]).sort(dsc_sort_date).appendTo(this[0]);
      }
      $('#Release').on('click', function(){
          $("#hold_images").sortDivsDscD();
          $('#Release').addClass("sort-select");
          $('#Rating').removeClass("sort-select");
          $('#Name').removeClass("sort-select");
          $('#Similarity').removeClass("sort-select");
      });

      // sort by similarity
      
      jQuery.fn.sortDivsDscS = function sortDivsDscS() {
          $(".games_div", this[0]).sort(dsc_sort_sim).appendTo(this[0]);
      }
      $('#Similarity').on('click', function(){
          $("#hold_images").sortDivsDscS();
          $('#Similarity').addClass("sort-select");
          $('#Rating').removeClass("sort-select");
          $('#Name').removeClass("sort-select");
          $('#Release').removeClass("sort-select");
      });
      
      },
    error: function(response){
      spinnerBox.classList.add('not-visible')
      dataBox.innerHTML = '<p>Failed to get Similar Games, please try again later.</p>'
    }

  });