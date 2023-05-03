import openAI_manager as O
import pinecone_manager as P

def runQuery(data):
    xq = O.generateEmbeddings(data)
    res = P.initIndex().query([xq['data'][0]['embedding']], top_k=1, include_metadata=True)
    for match in res['matches']:
        print(f"{match['score']:.2f}: {match['metadata']['text']}")

runQuery("What is Psychiatric Consultation")