function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      } 
    }
  }

$('#show').on('click', function () {
  $('.center').show();
  // $(this).hide();
})

$('#close').on('click', function () {
  $('.center').hide();
  $('#show').show();
})

$(function () {
  $("form").each(function () {
    $(this)
      .find("input")
      .keypress(function (e) {
        if (e.which == 10 || e.which == 13) {
          this.form.submit();
        }
      });
    $(this).find("input[type=submit]").hide();
  });
});

$('#noSpacesField').keyup(function() {
  $(this).val($(this).val().replace(/ +?/g, ''));
});

$(document).ready(function() {
  $(".container").click(function() {
    $(".stick").toggleClass(function () {
      return $(this).is('.open, .close') ? 'open close' : 'open';
    });
  });
});

