yourName = prompt("What is your name: ");
loverName = prompt("What is their name: ");
var loveScore = Math.random();
loveScore = loveScore * 100;
loveScore = Math.floor(loveScore) + 1;
alert("Your love score is " + loveScore + "%");
if (loveScore > 70) {
  alert(
    "Your love score is " +
      loveScore +
      "%" +
      "You love each other like Romeo and Julet."
  );
} else {
  alert("Your love score is " + loveScore + "%");
}
