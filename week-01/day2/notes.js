// "use strict"

// cmd/shift/p--> quokka start on current file

// const firstName = 'marcus';
// const properName = firstName[0].toUpperCase() + firstName.slice(1);
// console.log(`my name is ${properName}`)


// console.log(typeof(5))
// console.log(typeof(1.25e4))

// const nums = [44, 4, -72, 100]
// let currLargest = -Infinity;
// for (let num of nums){
// currLargest = num;
// }

// currLargest;



// console.log(typeof(NaN))


// function areTheyCool(name) {
//   name = name || "Jason";
//   console.log(`${name} is cool!`);
// }

// areTheyCool(); // Jason is cool!
// areTheyCool(""); // Jason is cool!
// areTheyCool("Sarah"); // Sarah is cool!


// let isStillLoading = true
// return isStillLoading && <myComponent></myComponent>

// const daysOfTheWeek = ["mon", "tues", "wed"];
// daysOfTheWeek[0] = "sun";
// console.log(daysOfTheWeek); // ["sun", "tues", "wed"]

// const daysOfTheWeek = ["mon", "tues", "wed"];
// daysOfTheWeek.push("thurs");
// console.log(daysOfTheWeek); // ["mon", "tues", "wed", "thurs"];


// objects can be nested
// const database = {
//   457: {
//     name: "Tom",
//     age: 34,
//   },
//   57782: {
//     name: "Sally",
//     age: 42,
//   },
// };

// // an objects value can be referenced by key using [] syntax
// const tomEntry = database[457];

// // if the key is a string, you can also use . syntax
// console.log(tomEntry.name); // "Tom"

// // You can re-assign a key's value (mutable)
// tomEntry.age = tomEntry.age + 1;

// // this update changes the value at any reference (mutable)
// console.log(database); // { ... 457: { ..., age: 35 } }






// // primitive
// let myNumber = 42;

// // 'num' is 'copy by value', changes to it won't effect what was passed in
// function incrementNumber(num) {
//   num = num + 1;
// }

// incrementNumber(myNumber);

// console.log(myNumber); // 42


// let myNumber = 42;

// function incrementNumber(num) {
//   return num + 1;
// }

// myNumber = incrementNumber(myNumber);

// console.log(myNumber); // 43





// // complex
// let myObject = { name: "Tom", age: 34 };

// // obj is 'copy by reference', changes to it will effect what was passed in
// function incrementObjectAge(obj) {
//   obj.age = obj.age + 1;
// }

// incrementObjectAge(myObject);

// console.log(myObject); // { name: "Tom", age: 35 };




// let myObject = { name: "Tom", age: 34 };

// function incrementObjectAgeImmutable(obj) {
//   const objCopy = Object.assign({}, obj); // helper function to create a new object, copy everything over
//   objCopy.age = objCopy.age + 1;
//   return objCopy;
// }

// const newObject = incrementObjectAgeImmutable(myObject);

// // updated object
// console.log(newObject); // { name: "Tom", age: 35 };

// // preserved original
// console.log(myObject); // { name: "Tom", age: 34 };

//----------------------------------------------------------------

//SETS: WILL NOT STORE A VALUE MORE THAN ONCE.

// const mySet = new Set();
// mySet.add(1)
// mySet.add(2)
// mySet.add(3)
// mySet.add(2)
// console.log(mySet.has(4))
// console.log(mySet)

//------------------------------------------------------------------

// // const can not be reassigned
// const num = 1;
// num = 42; // Uncaught TypeError: Assignment to constant variable

// // Note that complex types don't honor this 'constant' guarantee, only the variable itself
// const obj = { num: 1 };
// obj.num = 42; // kosher
// obj = 42; // Uncaught TypeError: Assignment to constant variable


// // let can be reassigned
// let num = 1;
// num = 42; // kosher


// function sumWithVar(n) {
//   var sum = 0;

//   for (var i = 0; i < n; i++) {
//     sum += i;
//   }

//   console.log(
//     `Hey can I still access ${i}? Yup it exists for the entire life of the function!`
//   );

//   return sum;
// }

// function sumWithLet(n) {
//   let sum = 0;

//   for (let i = 0; i < n; i++) {
//     sum += i;
//   }

//   console.log(
//     `Hey can I still access ${i}? No of course not, why would that be useful behavior?`
//   );

//   return sum;
// }

// sumWithVar(5); // 15
// sumWithLet(5); // ReferenceError: i is not defined


// makeFullName("Benjamin", "Cohen"); // "Benjamin Cohen"

// function makeFullName(firstName, lastName) {
//   return `${firstName} ${lastName}`;
// }

// const makeFullName = (firstName, lastName) => `${firstName} ${lastName}`;

// makeFullName("Benjamin", "Cohen"); // "Benjamin Cohen"


// const nums = [1, 2, 3];

// const doubles = nums.map((x) => x * 2);

// console.log(doubles); // [2, 4, 6]

// const nums = [1, 2, 3];

// const doubles = nums.map((x) => x * 2).filter((x) => x < 6);

// console.log(doubles); // [2, 4]


// const nums = [1, 2, 3];

// const doubles = nums.map(doubler);

// console.log(doubles); // [2, 4, 6]

// function doubler(x) {
//   return x * 2;
// }

//_______________________________________
// const age = 24;
// let canDrink;

// if (age < 21) {
//   canDrink = "nope!";
// } else {
//   canDrink = "yup!";
// }


// const age = 24;
// const canDrink = age < 21 ? "nope!" ;
                    // age < 28 ? 'hello' : 'yup!'


//___________________________________



// let myNumbers = [1, 44, 72];
// for (let i = 0; i < myNumbers.length; i++) {
//   console.log(myNumbers[i]);
// }

// let myNumbers = [1, 44, 72];
// for (let num of myNumbers.length) {
//   console.log(num);
// }


// const database = {
//   457: {
//     name: "Tom",
//     age: 34,
//   },
//   57782: {
//     name: "Sally",
//     age: 42,
//   },
// };

// // for (let entry of Object.entries(database)) {
// //   console.log(entry); // [ '457', { name: 'Tom', age: 34 } ]
// // }

// for (let [key, value] of Object.entries(database)){
//   console.log(key)
//   console.log(value)
// }

//________________________________________



// const myArray = ["x", "y", "z"];
// const x = myArray[0];
// const y = myArray[1];
// const z = myArray[2];

// const myObject = { a: 45, b: "hello", c: true };
// const a = myObject.a;
// const b = myObject.b;
// const c = myObject.c;


// const [x, y, z] = ["x", "y", "z"];

// const { a, b, c } = { a: 45, b: "hello", c: true };

// console.log(a)

//____________________________________________________________

// const arr = [1, 2, 3];
// const obj = { x: 1, y: 2, z: 3 };

// const arrCopy = [...arr];
// const objCopy = { ...obj };

// arrCopy[0] = 42;
// objCopy.x = 42;

// console.log(arr);
// console.log(arrCopy);
// console.log(obj);
// console.log(objCopy);

// const obj = { x: 1, y: 2, z: 3 };

// const objCopy = { ...obj, x: 42 };

// console.log(obj);
// console.log(objCopy);


// const arr = [1,2,3,4]
// const [x,y,z] = arr
// const[a,...b]= arr
// x
// y
// z
// a
// b
