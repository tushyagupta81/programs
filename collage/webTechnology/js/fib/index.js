const n = parseInt(prompt("Enter number of elements: "));
let a = 0;
let b = 1;
let temp = 0;
console.log(a);
let c = 0;
while (c + 2 <= n) {
  console.log(b);
  temp = b;
  b = a + b;
  a = temp;
  c++;
}
