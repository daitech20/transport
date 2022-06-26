const dimensions = document.querySelector('.dimensions__inner')
const show_dimensions = document.querySelector('#uk-with_dimensions')
const hide_dimensions = document.querySelector('#uk-no_dimensions')

const price_table = document.querySelector('.get-quote__prices')
const btn_show_oneship = document.querySelector('.btn__oneshipment')
const btn_show_manyship = document.querySelector('.btn__manyship')

function showSpaceMobile() {
var margin__100__mobile = document.querySelector(".btn__oneshipment");
margin__100__mobile.classList.add("space-100-mobile")
margin__100__mobile.classList.remove("space-0-mobile")

}

function hideSpaceMobile() {
var margin__0__mobile = document.querySelector(".btn__oneshipment");
margin__0__mobile.classList.add("space-0-mobile")
margin__0__mobile.classList.remove("space-100-mobile")
// location.reload()
}

show_dimensions.addEventListener('click', () => {
dimensions.style.display ='flex'
price_table.style.paddingTop = '60px'

})

hide_dimensions.addEventListener('click', () => {
dimensions.style.display ='none'
price_table.style.paddingTop = '0px'

})

const one_shipment = document.querySelector('.one__shipment')
const many_shipment = document.querySelector('.many__shipment')

const tab_one = document.querySelector('.uk-quote')
const tab_many = document.querySelector('.international-quote')

tab_many.addEventListener('click', () => {
many_shipment.style.display ='block'
one_shipment.style.display = 'none'
price_table.style.display = 'none'
price_table.style.paddingTop = '0px'
tab_many.style.backgroundColor  = '#00bd64'
tab_one.style.backgroundColor  = '#2c1f47'
})

tab_one.addEventListener('click', () => {
// location.reload()
many_shipment.style.display ='none'
one_shipment.style.display = 'block'
tab_many.style.backgroundColor  = '#2c1f47'
tab_one.style.backgroundColor  = '#00bd64'
price_table.style.display = 'none'
// dimensions.style.display = 'none'
})


btn_show_oneship.addEventListener('click', () => {
price_table.style.display = 'block'
})

btn_show_manyship.addEventListener('click', () => {
price_table.style.display = 'block'
})

const btn_menu_show = document.querySelector('.header__menu-open')
const btn_menu_hide = document.querySelector('.header__menu-close')
const menu_mobile = document.querySelector('.header__nav')

btn_menu_show.addEventListener('click', () => {
menu_mobile.style.display = 'block'
btn_menu_show.style.display = 'none'
btn_menu_hide.style.display = 'block'
})

btn_menu_hide.addEventListener('click', () => {
menu_mobile.style.display = 'none'
btn_menu_show.style.display = 'block'
btn_menu_hide.style.display = 'none'
})