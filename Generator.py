from PIL import Image
import urllib.request
import time
from io import BytesIO
import openai as ai

ai.api_key = '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'

class GPT():
    def __init__(self):
        self._name = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def GPTChatbot(self):
        completion = ai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": 'Hello, My name is %s' % self._name}])
        print(completion.choices[0].message.content)
        while True:
            conversation = input()
            completion = ai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "user", "content": conversation}],
                                                  stream = True)
            print('GPT Chatbot :', completion.choices[0].message.content)
            print('\n')
            if conversation == '': break
        return None

    def ImageGenerator(self):
        completion = ai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": 'Hello, My name is %s' % self._name}])
        print(completion.choices[0].message.content)
        paint = input('Say What you want : ')
        response = ai.Image.create(prompt=paint, model="image-alpha-001", size="1024x1024", response_format="url")
        url = response["data"][0]["url"]
        start = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req).read()
        print(time.time() - start)
        urlopen_img = Image.open(BytesIO(res))
        return urlopen_img

    def GPTBlogger(self, subject, language='eng'):
        if language == 'kor':
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": '%s에 대한 블로그 글 써 줘' % subject}],
                                                  stream = True)
        else:
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": 'Please write a blog about %s' % subject}],
                                                  stream = True)
        response = ai.Image.create(
            prompt=subject,
            model="image-alpha-001",
            size="512x512",
            response_format="url"
        )

        url = response["data"][0]["url"]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req).read()
        image = Image.open(BytesIO(res))
        print('Your assistant : ', completion.choices[0].message.content)
        return image

    def GPTpoet(self, subject, language='eng'):
        if language == 'kor':
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": '%s에 대한 시 써 줘' % subject}],
                                                  stream = True)
        else:
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": 'Please write a poem about %s' % subject}],
                                                  stream = True)
        print(completion.choices[0].message.content)
        return None

    def GPTarticle(self, subject, language='eng'):
        if language == 'kor':
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": '%s에 대한 기사 써 줘' % subject}],
                                                  stream = True)
        else:
            completion = ai.ChatCompletion.create(model="gpt-4",
                                                  messages=[{"role": "user",
                                                             "content": 'Please write an article about %s' % subject}],
                                                  stream = True)
        print(completion.choices[0].message.content)
        return None