word = "lumos"
input_string = input("Enter a string: ").lower()

collected_string = ""

for step, ch in enumerate(input_string, start=1):
    collected_string += ch

    if all(c in collected_string for c in word):    
        print(f"Found '{word}' at step {step}")
        break

else:
    print(-1)