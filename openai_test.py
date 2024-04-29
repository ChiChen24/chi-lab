import json

my_assigned_team = 'team_22'
keys = json.load(open('C:/shared/content/config/api-keys/hackathon_openai_keys.json'))
my_key = keys[my_assigned_team]

from openai import OpenAI
client = OpenAI(api_key=my_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What are 10 synonyms for person in the context of finance?  Please return a single line comma-separated list."}
  ]
)

synonyms = completion.choices[0].message.content.split(',')
print(synonyms)

model = "text-embedding-3-small"
synonyms = ["Individual","Investor","Stakeholder","Client","Customer","Participant","Trader","Player","Shareholder","Debtor"]

embeddings = {}
for word in synonyms:
    embedding = client.embeddings.create(input = [word], model=model).data[0].embedding
    embeddings[word] = embedding
    print(f"Embedding for {word} is {embedding}")

    