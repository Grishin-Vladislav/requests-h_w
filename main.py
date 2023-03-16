import os
from dotenv import load_dotenv, find_dotenv
from superheroes import HeroesChecker
from yandex import YaUploader
from stackoverflow import StackQuestions


load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
TOKEN1 = os.getenv('TOKEN1')


if __name__ == '__main__':

    hero = HeroesChecker(('Hulk', 'Captain America', 'Thanos'))
    hero.print_best()

    stack = StackQuestions(key=TOKEN1, tag='python', days=2)
    stack.get_questions()

    ya = YaUploader(TOKEN)
    ya.upload_file_to_root('questions.json')
