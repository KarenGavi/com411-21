# Display message
print("program stated!")

print("Please enter an ASCII code:")

code = int(input())

if code >= 32 and code <= 126:
    print(f"the character represented by the ASCII value {code} is:{chr(code)}")
else:
    print("the character cannot be displayed.")

print("program ended")
