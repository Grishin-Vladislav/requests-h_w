import requests
from datetime import datetime
from time import sleep
import json


class StackQuestions:
    def __init__(self, tag: str, days: int, key=None):
        self.now = int(datetime.now().timestamp())
        self.past = self.now - (24 * 60 * 60 * days)
        self.url = 'https://api.stackexchange.com/2.3/questions'
        self.key = key
        self.tag = tag

    def __do_requests(self):
        page_start = 1
        params = {
            'site': 'stackoverflow',
            'fromdate': str(self.past),
            'todate': str(self.now),
            'tagged': self.tag,
            'sort': 'creation',
            'page': page_start,
            'pagesize': 100
        }
        if self.key:
            params['key'] = self.key

        has_more = True
        questions = []

        while has_more:
            response = requests.get(self.url, params=params)
            for question in response.json()['items']:
                questions.append(question['title'])
            if not response.json()['has_more']:
                has_more = False
            sleep(0.04)
            print(f'page {page_start} ready')
            page_start += 1
            params['page'] = page_start

        return questions

    @staticmethod
    def __write_json(questions):
        with open('questions.json', 'w') as f:
            data = dict(enumerate(questions, 1))
            json.dump(data, f, ensure_ascii=True, indent=4)

    def get_questions(self):
        questions = self.__do_requests()
        self.__write_json(questions)
        print('Done!')
