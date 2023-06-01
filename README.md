# AI-social-posting

example of langchain social media posting using AI to generate social media posts according to tones

Below is the prompt

```
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

```

To run you need
- Python 3
- Open AI key
