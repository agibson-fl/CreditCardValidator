import sys
from CreditCardValidator import CreditCardValidator

#this is goofy, but satisfies the requirement to take credit card numbers through stdin

validator = CreditCardValidator()

try:
    count = int(sys.stdin.readline().strip())
except: 
    print("Invalid input format")
    sys.exit(1)
    
results = []
for x in range(count):
    ccnum = sys.stdin.readline().strip()
    if validator.execute(ccnum):
        results.append("Valid")
    else:
        results.append("Invalid")

print()
print("Results:")
for result in results:
    print(result)    