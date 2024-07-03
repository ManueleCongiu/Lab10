from database.DAO import DAO

countries = DAO.get_all_country(2006)

idMap = {}
for c in countries:
    idMap[c.CCode] = c


borders = DAO.get_all_archi(2006, idMap)

print(len(countries))
print(len(borders))
