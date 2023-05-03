import pinecone
import constants as Q
index_name = Q.PINECONE_INDEX


def initIndex():
    # initialize connection to pinecone (get API key at app.pinecone.io)
    pinecone.init(
        api_key=Q.PINECONE_KEY,
        environment=Q.PINECONE_ENV
    )

    # check if index already exists (it shouldn't if this is first time)
    if index_name not in pinecone.list_indexes():
        # if does not exist, create index
        pinecone.create_index(
            index_name,
            dimension=1536,
            metric='cosine',
            metadata_config={'indexed': ['channel_id', 'published']}
        )
    # connect to index
    index = pinecone.Index(index_name)
    # view index stats
   

    return index

def getIndex():
    return initIndex()

def deleteIndex():
    pinecone.init(
        api_key=Q.PINECONE_KEY,
        environment=Q.PINECONE_ENV
    )
    if index_name in pinecone.list_indexes():
        pinecone.delete_index(index_name)

