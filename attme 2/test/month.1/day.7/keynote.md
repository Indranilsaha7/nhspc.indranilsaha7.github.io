# Day 6: Comparison Operators:
## Python-এর প্রধান ৬টি Comparison Operator হলো:

1. > `==` (Equal to / সমান)
2. >`!=` (Not equal to / অসমান)
3. > `>` (Greater than / বড়)
4. > `<` (Less than / ছোট)
5. >`>`= (Greater than or equal to / বড় অথবা সমান)
6. >`<=` (Less than or equal to / ছোট অথবা সমান)
# Rule:
### 1 - The Ultimate Trap (= vs ==): 
* নতুন প্রোগ্রামাররা সবচেয়ে বেশি এই ভুলটি করে। শুধুমাত্র একটি সমান চিহ্ন **(=)** মানে হলো কোনো variable-এ value রাখা **(Assignment)**। আর দুটি সমান চিহ্ন **(==)** মানে হলো দুটি value একই কি না তা তুলনা করা `(Comparison)`।

### Sutro:
* `Comparison Operator`-এর আউটপুট সবসময় **bool** data type হবে। **Competitive Programming*-এ `(If-Else)` লজিক লেখার সময় এই **True**/ **False** কনসেপ্টটি তোমার সবচেয়ে বড় হাতিয়ার হবে।

### Trick 1 - 
* String Comparison: তুমি চাইলে শুধু `Number` নয়, `String`-ও তুলনা করতে পারো। যেমন: `"Indranil" == "Indranil"` এর আউটপুট হবে `True`।