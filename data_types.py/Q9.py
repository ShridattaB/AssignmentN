# Question9: Count the number of vowels in a given string.

# Sample Input: String = "Hello, World!"
# Expected Output: Number of vowels: 3

String = "Hello, World!"
vowels=0
for i in String:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
     vowels=vowels+1
print(vowels)
