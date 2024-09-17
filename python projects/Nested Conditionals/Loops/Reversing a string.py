#Input a word or sentence
string = input("Please enter your own String : ")

string2 = ('')
#lpp for pritng in revenrse
for i in string:
    string2 = i + string2

print("\n The original String =", string)
print("\n The Reversed String =", string2)
