# Day 7: Logical Operators ( **`and`, `or`, `not`** ) : 

## `Lesson:`
### `Python`-এ একাধিক `condition` বা শর্ত একসাথে চেক করার জন্য আমরা `Logical Operators` ব্যবহার করি। `Competitive` `Programming`-এ কোনো একটি `problem solve` করতে গেলে সাধারণত একটির বেশি শর্ত পূরণ করতে হয়, আর সেখানেই এই অপারেটরগুলোর প্রয়োজন পড়ে।
* ### **`Python`-এ মূলত `৩টি` Logical Operator আছে:** 
* 1. `and (এবং)`: এর দুই পাশের দুটি শর্তই `True` হতে হবে। একটি `False` হলেই পুরো রেজাল্ট `False` হয়ে যাবে।
* 2. `or (অথবা)`: যেকোনো একটি শর্ত `True` হলেই পুরো রেজাল্ট `True` হবে।
* 3. `not (বিপরীত)`: এটি উল্টো কাজ করে। `True`-কে `False` বানায়, আর `False`-কে `True` বানায়।

## `Step 2: Tips, Tricks, Rules (Sutros), and Formulas` :
* #### `Sutro - Real Life Logic:` **Competitive programming**-এ **and** এবং **or** সবচেয়ে বেশি ব্যবহার হয় `if-else` (যা আমরা আগামী মাসে শিখব) এর ভেতরে
* #### `Trick - Use Parentheses ():` যখন একাধিক `and` ও `or` একসাথে ব্যবহার করবে, তখন ব্র্যাকেট `()` দিয়ে সেগুলোকে আলাদা করে দেবে। এতে কোড পড়তে সুবিধা হয় এবং কম্পিউটার সহজে বুঝতে পারে কোন কাজটি আগে করতে হবে। Example: <code>(score > 80) and (time < 10)</code>