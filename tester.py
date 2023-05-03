ints = [1,2,3,4,5,6,7,8,9,10]
chunk_size = 4
for i in range(0, len(ints), chunk_size):
    chunk = ints[i:i+chunk_size]
    print('chunk -' , chunk)


OPENAI_KEY = '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'
PINECONE_KEY ='001becd1-9bf5-4f79-b2dc-5d7802255c78'
PINECONE_ENV = 'eu-west1-gcp'
PINECONE_INDEX = 'medical-vector-data-index'