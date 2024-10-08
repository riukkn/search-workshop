import json
from pathlib import Path
from whoosh.fields import STORED, TEXT, ID, Schema
from whoosh.analysis import SimpleAnalyzer
from whoosh.filedb.filestore import FileStorage

# Path to indexes folder
current_path = Path('./')
indexes = current_path / 'indexes'

# Create directory
indexes.mkdir(parents=True, exist_ok=True)

# Createc Indexes Schema
analyzer = SimpleAnalyzer()

schema = Schema(
  id= ID(stored=True, unique=True),
  title= TEXT(analyzer=analyzer, stored=True),
  brand= TEXT(analyzer=analyzer, stored=True),
  price= STORED(),
)

# Create index with its Schema
storage = FileStorage(indexes)
ind = storage.create_index(schema)
writer = ind.writer()

# Read JSON
with open('products.json') as f:
  products = json.load(f)
# print(products)

for product in products: 
  writer.add_document(
    id=  product['id'],
    title= product['title'],
    brand= product['brand'],
    price= product['price'],
  )

writer.commit(optimize=True)
with ind.searcher() as searcher:
  doc_count = searcher.doc_count()

print('total indexes:', doc_count)
