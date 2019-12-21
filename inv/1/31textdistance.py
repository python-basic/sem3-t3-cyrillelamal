"""
Sorry for no requirements
pip install textdistance
"""
from functools import reduce
import textdistance as td


USER_S_INPUT = 'je cherche du texte'


pages = [
    {'s': 'looking for text', 'link': 'http:foo'},
    {'s': 'cherche texte', 'link': 'http:bar'}
]


def compare(p1, p2):
    sim1 = td.hamming.normalized_similarity(USER_S_INPUT, p1['s'])
    sim2 = td.hamming.normalized_similarity(USER_S_INPUT, p2['s'])
    return p1 if sim1 > sim2 else p2


best_addr = reduce(compare, pages)['link']
print(best_addr)
