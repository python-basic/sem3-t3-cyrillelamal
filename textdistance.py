import textdistance as td

page1 = {'s': 'looking for text', 'link': 'http:foo'}
page2 = {'s': 'cherche texte', 'link': 'http:bar'}

user_s_input = 'je cherche du texte'

sim1 = td.hamming.normalized_similarity(user_s_input, page1['s'])
sim2 = td.hamming.normalized_similarity(user_s_input, page2['s'])
print(sim1, sim2)

if sim1 > sim2:
    print(page1['link'])
else:
    print(page2['link'])
