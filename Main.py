from typing import List
#adding the amount of oxygen molecules to the rbc
rbc: list[str] = []

amount = int (input("How many oxygen molecules?"))


if amount < 4:
    print("Error, the Red Blood Cell needs 4 oxygen molecules")
elif amount > 4:
    print("Error, the Red Blood Cell needs 4 oxygen molecules")
else:
    print("Moving oxygen molecules")

    for i in range(0, amount):
        rbc.append("oxygen")
    print("The red blood cell is full")

    print(rbc)


left_leg = []
right_leg = []
left_arm = []
right_arm = []
def move_oxygen(organ) -> []:
    for x in range(0, len(rbc)):
        organ.append("oxygen")
    for i in range(0, amount):
        rbc.pop()
    print(organ)
    print(rbc)

move_oxygen(right_arm)
