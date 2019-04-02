import wolframalpha
import wikipedia
import wikipediaapi

# entrada = input("Question: ")
app_id = "3KPAG5-7Q3X82XH89"
client = wolframalpha.Client(app_id)

# res = client.query(entrada)
# answer = next(res.results).text

wiki_wiki = wikipediaapi.Wikipedia('es')

page_py = wiki_wiki.page('Cristóbal Colón')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary)
# Page - Summary: Python is a widely used high-level programming language for

