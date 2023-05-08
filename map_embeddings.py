from nomic import atlas
import pinecone_manager as P
import numpy as np

num_embeddings = 173
vectors = P.getIndex().fetch(ids=[str(i) for i in range(num_embeddings)])

dict = {}
embeddings = []
for id, vector in vectors['vectors'].items():
    dict[id]=vector['metadata']['text']    
    embeddings.append(vector['values'])


embeddings = np.array(embeddings)

atlas.map_embeddings(embeddings=embeddings, data=[{'id':k, 'text': v} for k,v in dict.items()], id_field='id')