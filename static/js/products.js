// PRODUCT_INFO da olan TAP_IMG
function myFunction(imgs) {
  // Get the expanded image
  var expandImg = document.getElementById("expandedImg");
  // Use the same src in the expanded image as the image being clicked on from the grid
    expandImg.src = imgs.src;
  // Show the container element (hidden with CSS)
}

// PRODUCT BASKET

var check = false;

function changeVal(el) {
  var qt = parseFloat(el.parent().children(".qt").html());
  var price = parseFloat(el.parent().children(".price").html());
  var eq = Math.round(price * qt * 100) / 100;
  
  el.parent().children(".full-price").html( eq + "€" );
  
  changeTotal();      
}

function changeTotal() {
  
  var price = 0;
  
  $(".full-price").each(function(index){
    price += parseFloat($(".full-price").eq(index).html());
  });
  
  price = Math.round(price * 100) / 100;
  var tax = Math.round(price * 0.05 * 100) / 100
  var shipping = parseFloat($(".shipping span").html());
  var fullPrice = Math.round((price + tax + shipping) *100) / 100;
  
  if(price == 0) {
    fullPrice = 0;
  }
  
  $(".subtotal span").html(price);
  $(".tax span").html(tax);
  $(".total span").html(fullPrice);
}

$(document).ready(function(){
  
  $(".remove").click(function(){
    var el = $(this);
    el.parent().parent().addClass("removed");
    window.setTimeout(
      function(){
        el.parent().parent().slideUp('fast', function() { 
          el.parent().parent().remove(); 
          if($(".product").length == 0) {
            if(check) {
              $("#cart").html("<h1>The shop does not function, yet!</h1><p>If you liked my shopping cart, please take a second and heart this Pen on <a href='https://codepen.io/ziga-miklic/pen/xhpob'>CodePen</a>. Thank you!</p>");
            } else {
              $("#cart").html("<h1>No products!</h1>");
            }
          }
          changeTotal(); 
        });
      }, 200);
  });
  
  $(".qt-plus").click(function(){
    $(this).parent().children(".qt").html(parseInt($(this).parent().children(".qt").html()) + 1);
    
    $(this).parent().children(".full-price").addClass("added");
    
    var el = $(this);
    window.setTimeout(function(){el.parent().children(".full-price").removeClass("added"); changeVal(el);}, 150);
  });
  
  $(".qt-minus").click(function(){
    
    child = $(this).parent().children(".qt");
    
    if(parseInt(child.html()) > 1) {
      child.html(parseInt(child.html()) - 1);
    }
    
    $(this).parent().children(".full-price").addClass("minused");
    
    var el = $(this);
    window.setTimeout(function(){el.parent().children(".full-price").removeClass("minused"); changeVal(el);}, 150);
  });
  
  window.setTimeout(function(){$(".is-open").removeClass("is-open")}, 1200);
  
  $(".btn").click(function(){
    check = true;
    $(".remove").click();
  });

  $(".sss").slick({
    lazyLoad: 'ondemand',
    slidesToShow: 4,
    slidesToScroll: 4,
    dots: true,

    responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });

});

diss = document.getElementById('disa').style.display;

function disa() {
  if(diss==''){
    document.getElementById('disa').style.display = 'block';
    document.getElementById('disarasi').style.color = '#17B3C6';
  }else{
    document.getElementById('disa').style.display = '';
  }
}

f = document.getElementById('fircalar').style.display;

function fircaa() {
  if(f==''){
    document.getElementById('fircalar').style.display = 'block';
    document.getElementById('fircaa').style.color = '#17B3C6';
  }else{
    document.getElementById('fircalar').style.display = '';
  }
}

// Product info page dec inc

function setdown() {
  let i = document.getElementById('inn').value;
  if(i==1){
    document.getElementById('inn').value=1;
  }else {
    i--;
    document.getElementById('inn').value=i;
  }
}
function setup() {
  let i = document.getElementById('inn').value;
  i++;
  document.getElementById('inn').value=i;
}

