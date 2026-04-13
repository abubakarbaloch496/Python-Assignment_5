# Performs even/odd check, prints numbers, countdown, and greeting
name = input("Enter your name: ") 
num = int(input("Enter a number: ")) 
# 2. Even or Odd Check 
if num % 2 == 0:    
     print(num,"is Even") 
else:     
    print(num,"is Odd") 
# 3. For Loop (1 to Number) 
print("Numbers from 1 to", num, ":")
for i in range(1, num + 1):    
     print(i) 
# 4. While Loop (Countdown)
print("countdown from", num, "to 1:")
i = num 
while i >= 1:
    print(i) 
    i = i - 1 
# 5. Final Message 
print("Thank you", name) 