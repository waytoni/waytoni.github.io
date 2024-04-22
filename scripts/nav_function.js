function navFunction() {
    var x = document.getElementById("Topnavbar");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }