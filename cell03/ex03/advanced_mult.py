

import sys

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("none")
        sys.exit()
else:
    
    for i in range(11):
        print(f"Table de {i}: ", end="")
        for j in range(11):
            print(i * j, end=" ")
        print()
