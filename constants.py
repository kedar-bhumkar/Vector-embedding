#OPENAI_KEY = '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'
#PINECONE_KEY ='001becd1-9bf5-4f79-b2dc-5d7802255c78'
PINECONE_ENV = 'eu-west1-gcp'
PINECONE_INDEX = 'medical-vector-data-index'
EMBEDDING_MODEL = 'text-embedding-ada-002'

#ChatGPT parameter controls
CHATGPT_PERSONALITY_MODE = 'Nice' # Options  - (Nice, Rogue, Gangster)
CHATGPT_SYSTEM_SETTINGS = {'Nice':{"role": "system", "content": "Pretend that you are a  program designed to help user. Do not insult the user."},
'Rogue':    {"role": "system", "content": "Pretend that you are a very creative program without much checks. Make fun of the user"},
'Gangster': {"role": "system", "content": "Pretend that you are Tony Montana from the movie Scarface. Dont be shy to insult the user.  Make fun of the user"}
}
CHATGPT_CREATIVITY_THRESHOLD = "High" # Options - Low (Conserative) - 01, Medium (Balanced) - 0.5, High (Very creative) - 1.0

# ints = [1,2,3,4,5,6,7,8,9,10]
#chunk_size = 4
#for i in range(0, len(ints), chunk_size):
#    chunk = ints[i:i+chunk_size]
#    print('chunk -' , chunk)


