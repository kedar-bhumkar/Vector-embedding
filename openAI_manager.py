import openai
import constants as Q
from string import Template

import logging


# get API key from top-right dropdown on OpenAI website
openai.api_key = Q.OPENAI_KEY
embed_model = Q.EMBEDDING_MODEL
messages = [
    Q.CHATGPT_SYSTEM_SETTINGS[Q.CHATGPT_PERSONALITY_MODE]
]
temperature = 0.1 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Low' else 0.5 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Medium' else 1.0


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

def getAIresponse(prompt={}, theContext = {}):  
    t = Template("Could you answer the following  query based on the provided context? Query: $note.\n Context: $ctx")

    print ('Passed prompt - ', prompt, '\ntheContext - ', theContext)
    message = t.substitute(note =prompt, ctx= theContext)
    print ('Templated  text ', message)
    if message !='':
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature = temperature, messages=messages)
    reply = chat.choices[0].message.content
    print("ChatGPT:", reply)
    messages.append({"role": "assistant", "content": reply})
    return {"reply":reply}
          
#getAIresponse("\'Physcian Note : no weakness, unexpected weight changes,No assessment recorded. fever, chills, sweats, not weak, went to church, and walk well.HEENT: denies of abnormal headache, visual or hearing changes, rhinorrhea, difficult or pain to swallow.\'")

