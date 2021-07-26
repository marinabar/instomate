from search import searchimg
from addphotos import upload

query = str(input("What is your query ?  "))
N = int(input("How many images ?  "))
mainword = str(input("What word in the description ?  "))


#searchimg(query, N)
upload(mainword, N)