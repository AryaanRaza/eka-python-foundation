knowledge = [
    "Python" ,
    "Machine learning",
    "Retrieval Augmented Generation",
    "Databases"
]

choice = int(input("Enter the number of the knowledge to view: "))

for index , item in enumerate(knowledge ):
    if choice -1 != index :
        print(index + 1 , item)

