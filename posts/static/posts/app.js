/* selectors */
const nav_links = document.querySelector(".nav-links");
const burger = document.querySelector(".burger");
const lineOne = document.querySelector(".line1");
const lineTwo = document.querySelector(".line2");
const lineThree = document.querySelector(".line3");

/* listeners */

burger.addEventListener("click", showNavLinks);

/* functions */
function showNavLinks() {
  nav_links.classList.toggle("show-nav-links");
  lineTwo.classList.toggle("display-none");
  lineOne.classList.toggle("rotateLineOne");
  lineThree.classList.toggle("rotateLineThree");
}
