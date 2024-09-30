let n = prompt("Enter the number: ");
const l = n.length;
n = parseInt(n);
const dis = n;
let s = 0;
let d;
for (let i = 0; i < l; i++) {
  d = n % 10;
  n = Math.floor(n / 10);
  s += Math.pow(d, l);
}
if (s === dis) {
  alert(`${dis} is a armstrong number`);
} else {
  alert(`${dis} is not a armstrong number`);
}
