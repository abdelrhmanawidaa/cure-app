function color(){
    var input = document.getElementById('total');
    input.style.backgroundColor = 'pink';
   }
   function recolor(){
    var input = document.getElementById('total');
    input.style.backgroundColor = '#357875';
   }

function calc() {
    /* Dairy Products:*/
    var milk = document.getElementById("milk").value;
    var milk50 = document.getElementById("milk50").value;
    var skimmed = document.getElementById("skimmed").value;
    var powder = document.getElementById("powder").value;
    var feta = document.getElementById("feta").value;
    var cheddar = document.getElementById("cheddar").value;
    var turkey = document.getElementById("turkey").value;
    var yogurt = document.getElementById("yogurt").value;
    var lightYogurt = document.getElementById("lightYogurt").value;
    var boiledEgg = document.getElementById("boiledEgg").value;

    var chickenBreast = document.getElementById("chickenBreast").value;
    var quarterChicken = document.getElementById("quarterChicken").value;
    var friedChicken = document.getElementById("friedChicken").value;
    var turkeySlice = document.getElementById("turkeySlice").value;
    var liver = document.getElementById("liver").value;
    var beefSteak = document.getElementById("beefSteak").value;
    var beefBurger = document.getElementById("beefBurger").value;
    var chickenBurger = document.getElementById("chickenBurger").value;
    var hotdog = document.getElementById("hotdog").value;
    var salmon = document.getElementById("salmon").value;
    var grilledShrimp = document.getElementById("grilledShrimp").value;
    var tuna = document.getElementById("tuna").value;

    var fruits1 = document.getElementById("fruits1").value;
    var fruits2 = document.getElementById("fruits2").value;
    var fruits3 = document.getElementById("fruits3").value;
    var fruits4 = document.getElementById("fruits4").value;
    var vegetables = document.getElementById("vegetables").value;
    var peas = document.getElementById("peas").value;

    var cornflakes = document.getElementById("cornflakes").value;
    var potatoes = document.getElementById("potatoes").value;
    var fries1 = document.getElementById("fries1").value;
    var ricePastaFata = document.getElementById("ricePastaFata").value;
    var bread = document.getElementById("bread").value;
    var toast = document.getElementById("toast").value;


    var pizza = document.getElementById("pizza").value;
    var shawarma = document.getElementById("shawarma").value;
    var kfcSandwich = document.getElementById("kfcSandwich").value;
    var grapeLeaves = document.getElementById("grapeLeaves").value;
    var fries = document.getElementById("fries2").value;
    var soup = document.getElementById("soup").value;


    var popcorn = document.getElementById("popcorn").value;
    var oats = document.getElementById("oats").value;
    var hummus = document.getElementById("hummus").value;
    var beans = document.getElementById("beans").value;
    var hotChocolate = document.getElementById("hotChocolate").value;
    var tea = document.getElementById("tea").value;
    var juice = document.getElementById("juice").value;
    var latteCappuccino = document.getElementById("latteCappuccino").value;
    var iceCream = document.getElementById("iceCream").value;
    var nuts = document.getElementById("nuts").value;

    var biscuit = document.getElementById("biscuit").value;

/* Points */
var points = document.getElementById("points").value
var points = parseInt(points, 10);

var total = (chickenBreast * 2) + (quarterChicken * 5) + (friedChicken * 8) + 
(turkeySlice * 2) + (liver * 3) + (beefSteak * 2.5) + (beefBurger * 5) + 
(chickenBurger * 4) + (hotdog * 5) + (salmon * 2) + (grilledShrimp * 2) +
 (tuna * 4)+(milk * 3) + (milk50 * 2) + (skimmed * 1) + (powder * 0.5) + 
 (feta * 2) + (cheddar * 3) + (turkey * 5) + (yogurt * 2) + (lightYogurt * 1.5) 
 + (boiledEgg * 2) + (fruits1 * 1) + (fruits2 * 1) + (fruits3 * 1) + (fruits4 * 0)
  + (vegetables * 0) + (peas * 2) +(cornflakes * 2) + (potatoes * 2) + (fries * 8) +
   (fries1 * 8) +(ricePastaFata * 2) + (bread * 4) + (toast * 1)+(pizza * 6) + (shawarma * 9)
    + (kfcSandwich * 9) + (grapeLeaves * 5) + (soup * 2.5)+(popcorn * 1) + (oats * 1.5) + (hummus * 2) 
    + (beans * 1) + (hotChocolate * 1.5) + (tea * 1) + (juice * 1) + (latteCappuccino * 1) + (iceCream * 2) 
    + (nuts * 4) + (biscuit * 1);


if(total > points){
    document.getElementById("total").value = "Please don't Do That !";
    color();
    }
else{
    document.getElementById("total").value = total;
    recolor();
    }
}

function age(){
    var weight = document.getElementById("weight").value ;
    var weight = parseInt(weight, 10);

    var points=0;

    if(weight <= 68 ){
        points = 20;
    }
    else if(weight <=80 && weight >=70){
        points = 22;
    }
    else if(weight <=90 && weight >=81){
        points = 24;
    }
    else if(weight <=100 && weight >=91){
        points = 26;
    }
    else if(weight <=113 && weight >=101){
        points = 28;
    }
    else if(weight <=124 && weight >=114){
        points = 30;
    }
    else if(weight <=135 && weight >=125){
        points = 31;
    }
    else if(weight <=146 && weight >=136){
        points = 32;
    }
    else if(weight <=159 && weight >=147){
        points = 33;
    }
    else if(weight >= 160){
        points = 34;
    }

    document.getElementById("points").value=points;

}


