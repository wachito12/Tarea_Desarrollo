import openai
from pydantic import BaseModel

openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
openai.api_key = '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'


class Document(BaseModel):
    item: str = ''


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programacion universitario, tu sabes cualquier legunaje
        E.G
        Lenguajes:
        java
        python
        visual studio
        visual studio code
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
