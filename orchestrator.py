import fileparser as F
import pinecone_manager as P
import openAI_manager as O

def createVectors():
    data = F.parseFile()
    #print ('res size', data )
    #data = ['Standards of Care for Children, Adolescents, and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature','Standards of Care for Children, Adolescents, and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature','Standards of Care for Children, Adolescents, and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature','Standards of Care for Children, Adolescents, and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature','Standards of Care for Children, Adolescents, and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature']

    index = P.initIndex()
    print (index.describe_index_stats())

    chunk_size = 4
    for i in range(0, len(data), chunk_size):
        chunks = data[i:i+chunk_size]
        #print('chunks -' , chunks)
        res = O.generateEmbeddings(chunks)
        #print ('res ', res)
        embeds = [record['embedding'] for record in res['data']]    
        meta = [{'text': chunk} for chunk in chunks]
        ids = [str(n) for n in range(i, i+chunk_size)]
        to_upsert = zip(ids, embeds, meta)
        #upsert to Pinecone
        index.upsert(vectors=list(to_upsert))


createVectors()