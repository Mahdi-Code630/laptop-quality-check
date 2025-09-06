try:
    n = int(input("what's your number of laptops?").strip())
except ValueError:
    print("Error input! please enter a number of laptops.")
laptops = []
c = 0
while c < n:
    
    price, quality = map(int, input("what's your price and quality?").split())
    laptops.append((price, quality))
    c+=1
laptops.sort()

print("Happy irsa!" if laptops[0][0] < laptops[1][0] and laptops[0][1] > laptops[1][1] else "Poor irsa!")
