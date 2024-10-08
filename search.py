from pathlib import Path
from whoosh.filedb.filestore import FileStorage
from whoosh.qparser import QueryParser

# Path to indexes folder
current_path = Path('./')
indexes = current_path / 'indexes'

storage = FileStorage(indexes)
ind = storage.open_index()



def do_search(field, query, limit):
  with ind.searcher() as searcher:
    parser = QueryParser(field,ind.schema)
    query = parser.parse(f"*{query}*")
    results = searcher.search(query, terms=True, limit=limit)
    results_list = []
    for hit in results:
      results_list.append(dict(hit))
    return results_list


# field = 'title'
# query = 'laptop'
# limit = 10

if __name__ == "__main__":
  results = do_search('title', 'laptop', 10) 
  for hit in results:
    print(f"""ID: {hit['id']} Title: {hit['title']}""")


