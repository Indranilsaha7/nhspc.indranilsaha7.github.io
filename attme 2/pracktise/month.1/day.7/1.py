age = 14
is_student = True

# and: দুটি শর্তই সত্য হতে হবে
print(age < 18 and is_student)  # Output: True (কারণ দুটিই True)

# or: যেকোনো একটি সত্য হতে হবে
print(age == 20 or is_student)  # Output: True (বয়স ২০ নয়, কিন্তু is_student True)

# not: সত্যকে মিথ্যা, মিথ্যাকে সত্য বানায়
print(not is_student)           # Output: False (কারণ is_student True ছিল)