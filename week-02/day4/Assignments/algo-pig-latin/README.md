# Pig Latin

You're going to implement a pig latin word and phrase converter program. Your code should accept a string as a parameter and return the string 'pig latin-ified'

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below) but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

## Rules

For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added, as in the following examples:

- "pig" = "igpay"
- "latin" = "atinlay"
- "banana" = "ananabay"

When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing. Examples:

- "friends" = "iendsfray"
- "smile" = "ilesmay"
- "string" = "ingstray"

For words that begin with vowel sounds, one just adds "ay" to the end of the word. Examples: 

- "eat" = "eatway" or "eatay"
- "omelet" = "omeletway" or "omeletay"
- "are" = "areway" or "areay"

**Be sure to also look at the examples in the test files.**

You can also see https://en.wikipedia.org/wiki/Pig_Latin#Rules for more examples.

Below is what it should look like on the command line when you run your program. `# =>` is shorthand indicating what running the command should print to your terminal. 

```python
translate("apple") # => appleay

translate("university") # => universityay

translate("apple university") # => appleay universityay

translate("School") # => Oolschay

translate("I go to apple university") # => Iay ogay otay appleay universityay.

translate("Hi, I'm Zach") # => Ihay, I'may Achzay

translate("Hi, I'm Zach.\nHow are you?")
# => Ihay, I'may Achzay.
# => Owhay areay ouyay?
```
