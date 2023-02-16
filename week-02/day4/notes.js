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

class Cat {
  constructor(name) {
    this.name = name;
  }

  eat(food) {
    console.log(`"${this.name} eats a ${food}.`);
  }

  meow() {
    console.log("meow meow!");
  }
}

const garfield = new Cat("Garfield");
console.log(garfield.name);
garfield.eat("lasagna");
garfield.meow();