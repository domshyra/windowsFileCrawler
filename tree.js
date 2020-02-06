var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
    var img = this.getElementsByClassName('far')[0];
    if (img.classList[1] === "fa-folder"){
      img.classList.remove("fa-folder");
      img.classList.add("fa-folder-open");
    }
    else {
      img.classList.remove("fa-folder-open");
      img.classList.add("fa-folder");
    }
  });
}