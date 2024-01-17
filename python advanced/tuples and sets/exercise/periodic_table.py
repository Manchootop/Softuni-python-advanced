n = int(input())
unique_chemical_compounds = set()
for i in range(n):
    unique_chemical_compounds.add(tuple(input().split(' ')))

[print(element) for compound in unique_chemical_compounds for element in compound]