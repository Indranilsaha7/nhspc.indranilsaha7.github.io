# Day 5: Type Casting & Conversion
## The lesson

`Type Casting` মানে হলো একটি `Data Type`-কে জোর করে অন্য একটি `Data Type`-এ রূপান্তর করা (যেমন `String`-কে `Integer` বানানো)।

`Python`-এ এই কাজটি করার জন্য আমাদের কাছে ৩টি প্রধান ফাংশন আছে:

`int()`: যেকোনো কিছুকে Integer বা পূর্ণ সংখ্যায় রূপান্তর করে।

`float()`: যেকোনো কিছুকে Float বা দশমিক সংখ্যায় রূপান্তর করে।

`str()`: যেকোনো কিছুকে String বা Text-এ রূপান্তর করে।

## Tips, Tricks, Rules (Sutros), and Formula
* `Rule 1` - The Concatenation Error: print("Age: " + 14) লিখলে `Error` আসবে। `String-এর সাথে String জোড়া লাগানো যায়`, কিন্তু `String-এর সাথে Integer জোড়া লাগানো যায় না`। তাই `print("Age: " + str(14))` লিখতে হবে।

* `Trick 1` - The Ninja Input (Shorthand): `Competitive programming`-এ আমরা লাইন কমানোর জন্য ইনপুট নেওয়ার সময়ই সাথে সাথে তাকে Integer-এ রূপান্তর করে ফেলি।
Example: `age = int(input("Enter age: "))`
এই এক লাইনেই ইনপুট নেওয়া এবং `Type Casting`—দুটি কাজই হয়ে যায়!