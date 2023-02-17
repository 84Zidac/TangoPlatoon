//--------------------------------------------------------------------------------------------------------------------
// Comparision with Python
// class Cat:
//     def __init__(self, name):
//         self.name = name

//     def eat(self, food):
//         print(f"{self.name} eats a {food}.")

//     def meow(self):
//         print("meow meow!")


// garfield = Cat("Garfield")

// print(garfield.name)
// garfield.meow()
// garfield.eat("lasagna")

// class Cat {
//   constructor(name) {
//     this.name = name;
//   }

//   eat(food) {
//     console.log(`"${this.name} eats a ${food}.`);
//   }

//   meow() {
//     console.log("meow meow!");
//   }
// }

// const garfield = new Cat("Garfield");
// console.log(garfield.name);
// garfield.eat("lasagna");
// garfield.meow();

//--------------------------------------------------------------------------------------------------------------------
// Python vs JS: Inheritance

// class Animal:
//     def __init__(self, name):
//         self.name = name

//     def eat(self, food):
//         print(f"{self.name} eats a {food}.")

//     def speak(self):
//         print("I'm an animal!")

// class Dog(Animal):
//     def __init__(self, name, is_service_animal):
//       super().__init__(name)
//       self.is_service_animal = is_service_animal

//     def bark(self):
//         print("bark bark!")

//     def speak(self):
//         self.bark()


// fido = Dog('Fido', True)
// fido.eat('chicken nugget')
// fido.bark()
// fido.speak()


// class Animal {
// genus = 'animal'
//   constructor(name) {
//     this.name = name;
//   }

//   eat(food) {
//     console.log(`${this.name} eats a ${food}.`);
//   }

//   speak() {
//     console.log("I'm an animal!");
//   }
// }

// class Dog extends Animal {
//   constructor(name, is_service_animal) {
//     super(name);
//     this.is_service_animal = is_service_animal;
//   }

//   bark() {
//     console.log(`${this.name} bark bark!`);
//   }

//   speak() {
//     super.speak()
//     this.bark();
//   }
// }

// const fido = new Dog('Fido', true)
// fido.eat('chicken nugget')
// fido.bark()
// fido.speak()

//--------------------------------------------------------------------------------------------------------------------
// The this keyword

// // `this` is not attached to any object, so it refers to 'global' in node (an empty object).
// // either way this is rarely something you want
// console.log(this);

// // `this` appears in the function `sayHello`
// const alice = {
//   name: "alice",
//   // sayHello is a regular 'function' function, so it has it's own scope, and the inner 'this'
//   // will refer to it's calling context
//   sayHello: function () {
//     console.log(`Hello, my name is ${this.name}`);
//   },
// };

// // because of how we are calling this, the 'alice' variable is the 'context' in which sayHello is run
// // so when sayHello hits it's 'this' keyword, it refers to the variable 'alice'
// alice.sayHello();

// // arrow functions do not rebind `this`
// const bob = {
//   name: "bob",
//   // sayHello is an arrow function, so it doesn't create it's own scope
//   sayHello: () => {
//     console.log(`My name is ${this.name}`);
//   },
// };

// // that means when we call this, 'bob' is not it's context, but bob's context is sayHello's context, which is the 'global' object, or {}
// // we warned you this is confusing and ugly!
// bob.sayHello();

// // the value of `this` depends on how the function is CALLED, not how it is DEFINED
// const sayHello = function () {
//   console.log(this.name);
// };

// // this.name is undefined or empty string, depending on the environment
// sayHello();

// const eve = {
//   name: "eve",
//   sayHello: sayHello,
// };

// // in this case, `this` refers to the eve object, so `this.name` is 'eve',
// eve.sayHello();

// def sayHello(name):
//   print(f"My name is {name}")


// bob = {
//     'name':'bob'
//     'sayHello': lambda name: print(f"My name is {name}")

//     bob['sayhello'](bob['name'])
// }
//--------------------------------------------------------------------------------------------------------------------
// The new keyword


// // we're pretending this is a class, so we named it with a capital letter
// const Person = function (name) {
//   // const this = {} (implicit, because of 'new')
//   this.name = name;
//   // return this (implicit, because of 'new')
// };

// const alice = new Person("Alice");

//--------------------------------------------------------------------------------------------------------------------
// Prototype

// const Person = function (name) {
//   this.name = name;
// };

// Person.prototype.sayHello = function () {
//   console.log(`Hello, my name is ${this.name}.`);
// };

// const alice = new Person("Alice");

// // alice has no method sayHello, but alice is a Person and a Person's prototype does have it
// alice.sayHello();

//--------------------------------------------------------------------------------------------------------------------
// Encapsulation

// class Animal{
//   #genus = 'animal';  //-----------------------> makes private
//   constructor(name){
//     this.name = name;
//     this.$genus = genus
//   }
//   description(){
//     console.log(`My name is ${this.name} and i am an ${this.#genus}`)
//   }
// }
// const pikachu = new Animal('Pikachu')

// pikachu.description()
// console.log(pikachu.name)
// pikachu.#genus=43





