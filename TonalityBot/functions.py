import requests


def define_tonality(audio):
    attrubites = [1, 1, 1]

    return f'Тональность: {attrubites[0]}\nКлюч: {attrubites[1]}\nТемп: {attrubites[2]} bpm'
