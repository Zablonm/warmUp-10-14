//Arrays
let fruits = ["Apple", "Banana", "Cherry"];


console.log(fruits[0]); // Output: "Apple"


fruits.push("Mango");  
console.log(fruits);   

fruits.pop();         
console.log(fruits);  

fruits.unshift("Grape");
console.log(fruits);     

fruits.shift();          
console.log(fruits);     

//Objects
let car = { make: "Toyota", model: "Camry" };
console.log(car.make); // Output: "Toyota"

// Object with a method
let person = {
  name: "Alice",
  age: 25,
  greet: function() {
    return "Hello, " + this.name;
  }
};
console.log(person.greet()); // Output: "Hello, Alice"

//Events
document.getElementById("btn").addEventListener("click", function() {
  alert("Button clicked!");
});

let elements = document.getElementsByClassName("text");
for (let i = 0; i < elements.length; i++) {
  elements[i].style.color = "blue"; // Changes text color to blue
}
