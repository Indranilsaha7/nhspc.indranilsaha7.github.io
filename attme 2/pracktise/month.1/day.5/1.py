# input() সবসময় String দেয়
age_string = input("Enter your age: ") 

# String-কে Integer-এ রূপান্তর (Type Casting) করা হচ্ছে
age_number = int(age_string)

# এবার আমরা Math করতে পারব!
next_year_age = age_number + 1

# আউটপুট দেখানোর সময় আবার str() ব্যবহার করতে হয়, কারণ Text-এর সাথে Number সরাসরি যোগ (+) করা যায় না
print("Next year, you will be " + str(next_year_age) + " years old.")