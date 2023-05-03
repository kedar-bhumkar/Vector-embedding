import openai

# get API key from top-right dropdown on OpenAI website
openai.api_key = "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"
embed_model = "text-embedding-ada-002"

def generateEmbeddings(data):
    res = openai.Embedding.create(
        input=
            data
        , engine=embed_model
    )
    

    #print (res.keys())
    #print (len(res['data'][0]['embedding']), len(res['data'][1]['embedding']))

    return res


#generateEmbeddings(['Standards of Care for Children  Adolescents  and their Families', 'The cat is a cute animal', 'The dog is an adorable animal','The squirrel is a lovely creature']
