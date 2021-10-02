from googlesearch import search

# simple google python script using (googlesearch-python package)
inputSearch = input("Enter query: ")
queryLength = int(input('Enter query length: '))
getSearch = search(inputSearch, lang="en", num_results=queryLength)
print(len(getSearch))
for queryResults in getSearch:
  print(queryResults)
