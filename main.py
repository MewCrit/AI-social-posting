from langchain import PromptTemplate
from langchain.llms import OpenAI
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/socials')
def lang_socials():

    data = request.json
    tone = data['tone']
    dialect = data['dialect']
    sentence = data['sentence']

    template = """
        Below is a sentence that could be bad.
        Your goal is to:
        - To make it a social media post to
        - Convert the input text to a specified tone
        - Convert the input text to a specified dialect
        Here are some Tone example
        - If aggressive the post will sound aggressive
        - If calm the post will sound calm
        - If cool the post will sound cool
        - If scary the post will sound scary    
        Dialects can be any languages such as English, Filipino etc..

        Below is the email, tone, and dialect:
        TONE: {tone}
        DIALECT: {dialect}
        EMAIL: {sentence}
        
        YOUR {dialect} RESPONSE:
    """

    prompt = PromptTemplate(
        input_variables=["tone", "dialect", "sentence"],
        template=template,
    )

    llm = load_LLM()
    send_prompt = prompt.format(tone=tone, dialect=dialect, sentence=sentence)
    results = llm(send_prompt)

    response = {
        'status_code' : 200,
        'result' : results
    }

    return jsonify(response)


def load_LLM():
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key='sk-')
    return llm


if __name__ == '__main__':
    app.run()


