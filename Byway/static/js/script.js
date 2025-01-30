let Cards = document.querySelectorAll('.Item-Card')

Cards.forEach(Card=>{

    Card.addEventListener('click', function(){
        window.location.href = 'home'
    })
    
})

let Categories =  document.querySelectorAll('.Category-card')

Categories.forEach(Category => {
    Category.addEventListener('click',function(){
        window.location.href = 'courses'
        
    })
})

document.addEventListener("DOMContentLoaded", function () {
    let priceDiv = document.querySelector(".Price");

    // Get values as strings and convert them to floating-point numbers
    let ogPrice = parseFloat(priceDiv.getAttribute("data-ogprice"));
    let offPrice = parseFloat(priceDiv.getAttribute("data-offprice"));

    // Check if values are valid numbers before calculation
    if (!isNaN(ogPrice) && !isNaN(offPrice)) {
        let finalPrice = ogPrice - (ogPrice * offPrice / 100);
        document.getElementById("finalPrice").innerText = `$${finalPrice.toFixed(2)}`;
    } else {
        console.error("Invalid price values:", ogPrice, offPrice);
    }
});
