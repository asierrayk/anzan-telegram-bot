#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from gtts import gTTS
import os
from pydub import AudioSegment


def generate_audio(file_name=None, times=3, numbers=10, digits=1, substraction=False, substraction_probability=0.2, slow=False, include_answer=True, delay_answer=3000):
    pause_1s = AudioSegment.silent(duration=1000)
    pause = AudioSegment.silent(duration=delay_answer)
    final = AudioSegment.empty()
    for t in range(times):
        resultado = 0
        intro_text = ''
        problem_text = ''
        solution_text = ''
        intro_text += 'Ejercicio {}'.format(t+1)
        for i in range(numbers):
            n = randint(1, pow(10, digits)-1)

            if substraction:
                if random() < substraction_probability:
                    n = -n

            resultado += n
            problem_text += '{}.. '.format(n)

        if include_answer:
            solution_text += 'Resultado {}'.format(resultado)

        tts = gTTS(text=intro_text, lang='es')
        tts.save(file_name+'_intro.mp3')

        tts = gTTS(text=problem_text, lang='es', slow=slow)
        tts.save(file_name+'_problem.mp3')

        tts = gTTS(text=solution_text, lang='es')
        tts.save(file_name+'_solution.mp3')

        intro = AudioSegment.from_mp3(file_name+'_intro.mp3')
        problem = AudioSegment.from_mp3(file_name+'_problem.mp3')
        solution = AudioSegment.from_mp3(file_name+'_solution.mp3')

        exercise = intro + pause_1s + problem + pause + solution
        final = final+exercise
    os.system('rm {}_intro.mp3'.format(file_name))
    os.system('rm {}_problem.mp3'.format(file_name))
    os.system('rm {}_solution.mp3'.format(file_name))
    final.export(file_name, format="mp3")


if __name__ == "__main__":
    generate_audio(file_name='test.mp3', times=1, numbers=10, digits=1, substraction=False)
    os.system('mpg321 test.mp3')
