import lorem


html = ''
for i in range(10):
    html += f'<p>{lorem.paragraph()}</p>\n'

print(html)
