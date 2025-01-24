//Asynchronous Programming
setTimeout(function() {
  console.log("Hello after 2 seconds");
}, 2000); // Logs "Hello after 2 seconds" after a delay
let promise = new Promise((resolve, reject) => {
  let success = true;
  success ? resolve("Success!") : reject("Failure!");
});
promise.then(console.log).catch(console.error); // Logs "Success!"
let x = 5;
console.log("Value of x: ", x); // Logs the value of x
