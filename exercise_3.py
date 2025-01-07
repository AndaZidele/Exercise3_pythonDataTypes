# List
# List contains employee positions
typesOfEmployeePositions = ["sales manager", "administrator", "accountant", "cook", "waiter"]
typesOfEmployeePositions.append("product supplier")
print(typesOfEmployeePositions)

# Tuple
# Tuple also contains employee positions
typesOfEmployeePositionsTuple = ("sales manager", "administrator", "accountant", "chef", "cook")
l = list(typesOfEmployeePositionsTuple)
l.append("hotel manager")
tup = tuple(l)
print(tup)

# Set
# Set also contains employee positions
typesOfEmployeePositionsSet = {"sales manager", "administrator", "accountant"}
typesOfEmployeePositionsSet.add("waiter")
print(typesOfEmployeePositionsSet)
# Var apskatīties kuru amatu tipi ir visās klasēs
print(typesOfEmployeePositionsSet & set(typesOfEmployeePositionsTuple) & set(typesOfEmployeePositions))

# Dictionary
# Dictionary contains employee positions, names and age
employeeDictionary = {
    "date": "10.12.2024.",
    "employees": [
        {
            "position": "sales manager",
            "name": "Igors",
            "age": 36
        },
        {
            "position": "hotel manager",
            "name": "Dace",
            "age": 38
        }
    ]
}

for item in employeeDictionary["employees"]:
    print(item.get("name"), "is a", item.get("position")+".")