import operationsMongo

numberString = (operationsMongo.Database("SP").searchForItem("P", "SP", "TYP_FS"))
# print(numberString)/
# for x in numberString:/
print(numberString[-1]["NUMER"])