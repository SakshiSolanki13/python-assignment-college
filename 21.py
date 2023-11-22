numbers = [14,28,7,11,8,2,10]
f = 0 
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print(" Search unsuccessful")