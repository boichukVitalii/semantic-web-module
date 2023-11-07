# Написати Python-скрипт, який на базі заданого графу
# повертає загальну чисельність населення кожного континенту.

from rdflib import Graph
from collections import defaultdict

countries_graph = Graph()
countries_graph.parse('countrues_info.ttl', format="ttl")

continent_population = defaultdict(int)

query = """
SELECT ?country ?population ?continent
WHERE {
  ?country :country_name ?name ;
           :population ?population ;
           :part_of_continent ?continent .
}
"""

results = countries_graph.query(query)

for row in results:
    population = int(row['population'])
    continent = row['continent']
    continent_population[continent] += population

for continent, population in continent_population.items():
    print(
        f"Континент: {continent.split('/').pop()}, Загальна чисельність населення: {population}"
    )

'''
                        ВИВІД
Континент: EU, Загальна чисельність населення: 758597538
Континент: AS, Загальна чисельність населення: 4522874728
Континент: NA, Загальна чисельність населення: 583536773
Континент: AF, Загальна чисельність населення: 1268766150
Континент: AN, Загальна чисельність населення: 170
Континент: SA, Загальна чисельність населення: 423597139
Континент: OC, Загальна чисельність населення: 43093797
'''
