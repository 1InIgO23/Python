import string
#Used for a conditional

print("Select story: ")
print("A: a kid in the garden. B: the bussisnesman life.")
value = input("Enter A or B: ")
#Selection between 2 story

def first_story():
    print("Hello, my name is [name]")
    print("I [verb] with my dog in my garden")
    print("I love [adjective] gardens")
    name = input("[Name]: ")
    verb = input("[Verb]: ")
    adjective = input("[Adjective]: " )
    if name in  string.digits or verb in string.digits or adjective in string.digits:
        print("Invalid input, cannot be numbers.")
    else:
        print("Hello my name is " + name)
        print("I " + verb + " with my dog in my garden")
        print("I love " + adjective  + " gardens")

def second_story():
    print("Hello my name is [name]")
    print("I invest my money in [plural noun]")
    print("My goal is to [verb]")
    name = input("[Name]: ")
    plural_noun = input("[Plural noun]: ")
    verb = input("[Verb]: " )
    if name in  string.digits or plural_noun in string.digits or verb in string.digits:
        print("Invalid input, cannot be numbers.")
    else:
        print("Hello my name is " + name)
        print("I invest my money in " + plural_noun)
        print("My goal is to " + verb)

if value == "A":
    first_story()
elif value == "B":
    second_story()
else:
    print("Invalid input.")