exampleList = [1,5,6,6,2,1,5,2,1,4]

for x in exampleList:
    print(x)

print('\n')

for x in range(1,11):
    print(x)

print('\n')

edibles = ["ham", "spam", "eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue
    print("Great, delicious " + food)
    # here can be the code for enjoying our food :-)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")