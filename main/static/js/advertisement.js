const favorite = document.querySelector(".cart_list")
const cart_list = document.querySelector('.cart_list')
const cart_list_id = document.querySelector('#cart_list_id')
const cart = document.querySelector('#cart_id')
const cart_img = document.querySelector('#cart_img_id')
const cart_info = document.querySelector('#cart_info_id')
const cart_link = document.querySelector('#cart_link_id')
const cart_info_price = document.querySelector('#cart_info_price_id')
const cart_info_bearer = document.querySelector('#cart_info_bearer_id')
const sorted_1 = document.querySelector('#type_sorted_1')
const sorted_2 = document.querySelector('#type_sorted_2')

const array_cart = document.querySelectorAll('.cart')
console.log(array_cart)

favorite.onclick = function(event){
    let target = event.target;
    if (target.className === "favorite_img"){
        if (target.getAttribute("src") === "/static/img/favorite.png"){
            target.src = "/static/img/favorite_yes.png";
        }
        else {
            target.src = "/static/img/favorite.png";
        }
    }

}
for (i of array_cart) {
    console.log(i)

}
// sorted_1.addEventListener("click", () => {
//     console.log('johan')
//     cart_list_id.classList.remove(("cart_list"))
//     cart.classList.remove(("cart"))
//     cart_img.classList.remove(("cart_img"))
//     cart_info.classList.remove(("cart_info"))
//     cart_link.classList.remove(("cart_link"))
//     cart_info_price.classList.remove(("cart_info_price"))
//     cart_info_bearer.classList.remove(("cart_info_bearer"))
//     cart_list_id.classList.add(("cart_list_2"))
//     cart.classList.add(("cart_2"))
//     cart_img.classList.add(("cart_img_2"))
//     cart_info.classList.add(("cart_info_2"))
//     cart_link.classList.add(("cart_link_2"))
//     cart_info_price.classList.add(("cart_info_price_2"))
//     cart_info_bearer.classList.add(("cart_info_bearer_2"))
// });



