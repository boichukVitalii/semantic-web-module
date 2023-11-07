# Використовуючи бібліотеки RdfLib, SPARQLWrapper та відкритий endpoint написати Python-скрипт,
# який буде повертати країни, в яких розмовляють англійською.
# Країни необхідно впорядкувати за площею.

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "https://query.wikidata.org/bigdata/namespace/wdq/sparql")
sparql.setQuery("""
SELECT ?countryLabel ?area
WHERE {
  ?country wdt:P31 wd:Q3624078 ;
           wdt:P37 wd:Q1860 .
  ?country wdt:P1082 ?area .
  ?country rdfs:label ?countryLabel .
  FILTER (lang(?countryLabel) = "en")
}
ORDER BY DESC(?area)
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    country_label = result["countryLabel"]["value"]
    area = float(result["area"]["value"])
    print(f"Країна: {country_label}")
    print(f"Площа: {area} кв.км \n")
