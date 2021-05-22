
  const spinnerBox =document.getElementById('spinner-box')
  const dataBox = document.getElementById('data-box')
  const games = document.getElementById('games')
  const img = document.getElementById('hold_images')
  const buttonRight = document.getElementById('slideRight');
  const buttonLeft = document.getElementById('slideLeft');
  var frag = document.createDocumentFragment();
  const gameName= "{{gameShowing}}".replace("#", "");
  let width = screen.width -75;
  console.log(gameName)

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

  $.ajax({
    type: 'GET',
    url: `/similar-games-json/${gameName}/filter%3F{{console}}`,
    success: function(response){
      spinnerBox.classList.add('not-visible')
      response['gameDets'].forEach((element, index) => {
        img.innerHTML += `
            <div class='games_div' data-similarity="${index}" data-name="${element.name}" data-rating="${element.meta_score}" data-release="${element.release_date}">
              <div onclick="openTab(${index})" class="imgDiv">\
                <img class="my_img" width=230px height=300px src='{% static '' %}games/${response['imgNames'][index]}' alt='${element.name}'>\
              </div>
              
            </div>
            `
        dataBox.innerHTML += `
          <div id='dets${index}' class='details not-visible' style='color: white;'>\
            <span onclick="this.parentElement.style.display='none'" class="closebtn">x</span>
                      <div style='display: block; margin: auto; '>\
                        <h3 style='margin:10px;'> ${element.name}</h3>\
                        <h6 style='margin:10px;'> Platform:  ${response['platforms'][index]}</h6>\
                        <h6 style='margin:10px;'> Release: ${element.release_date}</h6>\
                        <h5 style='margin:10px;'> Rating: ${element.meta_score}</h5>\
                        <h6 style='margin:10px;'> ${element.gameDesc}</h6>\
                        <div class="dets-small" style="margin-left: 5px;">
                          <h6 style='margin: 0 5px; padding:0px;'> User Score: ${element.user_score} | </h6>\
                          <h6 style='margin: 0 5px; padding:0px;'> Age: ${element.age_rating} | </h6>\
                          <h6 style='margin: 0 5px; padding:0px;'> Developers: ${element.Devs} | </h6>\
                        </div>
                        
                        <h6 style='margin:10px;'> Genres: ${element.Genres}</h6>\
                    </div>\
              </div>
        `
      });
        

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