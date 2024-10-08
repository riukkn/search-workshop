from whoosh.fields import STORED, TEXT, ID, Schema
from whoosh.analysis import SimpleAnalyzer

analyzer = SimpleAnalyzer()

schema = Schema(
  id= ID(stored=True, unique=True),
  title= TEXT(analyzer=analyzer, stored=True),
  brand= TEXT(analyzer=analyzer, stored=True),
  price= STORED()
)
