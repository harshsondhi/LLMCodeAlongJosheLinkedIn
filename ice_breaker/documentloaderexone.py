from langchain.document_loaders import CSVLoader
from langchain.document_loaders import BSHTMLLoader
from langchain.document_loaders import PyPDFLoader


# loader = CSVLoader('some_data/penguins.csv')
# data = loader.load()
# print(data[10].metadata)

# loader = BSHTMLLoader('some_data/some_website.html')
# data = loader.load()
# print(data[0].page_content)

loader = PyPDFLoader("some_data/SomeReport.pdf")
pages = loader.load_and_split()
print(type(pages))
print(pages[0])
print(pages[0].page_content.replace("\n", " "))
