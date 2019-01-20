var contentIndex = 0;
showContents(contentIndex)
function showContents(n) {
  var i;
  var content = document.getElementsByClassName("content"); 
  var sidebar = document.getElementsByClassName("sidebar-about-thumbnail");
  for (i = 0; i < content.length; i++) {
      content[i].style.display = "none";  
  }
  for (i = 0; i < sidebar.length; i++){
  	sidebar[i].className = sidebar[i].className.replace(" active", "");
  }
  content[n].style.display = "block"; 
  sidebar[n].className += " active";
  contentIndex = n; 
}