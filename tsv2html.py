# <table style="width:100%">
#   <tr>
#     <th>Authors</th>
#     <th>Title</th>
#     <th>Year</th>
#     <th>Venue</th>
#     <th>Link(s)</th>
#     <th>Arxiv</th>
#   </tr>
#   <tr>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#     <td>?</td>
#   </tr>
#   ...
# </table>

rows = []

def get(text,col):
    columns = {'authors':0,'title':1,'year':3,'venue':2,'links':4,'arxiv':5,'tags':6}
    x = text.split('\t')[columns[col]]
    if x and x[0] == '"' and x[-1] == '"':
        x = x[1:-1]
    return x


def link(line):
    x = get(line,'links')
    if 'href' in x:
        return x
    elif x.strip():
        return f'<a href="{x}">pdf</a>'
    else:
        return ''

def arxiv(line):
    x = get(line,'arxiv')
    if x.strip():
        return f'<a href="{x}">arXiv</a>'
    else:
        return ''


topics = set()
def tags(line):
    tags = []
    x = get(line,'tags')
    x = x.split(', ')
    for tag in x:
        if not tag.strip(): continue
        tag = tag.replace('"','')
        topic = tag.lower().replace('+','').strip()
        topics.add(tag.strip())
        tags.append(f'<button topic="{topic}" on="0">{tag}</button>')
    return ' '.join(tags)

def authors(line):
    x = get(line,'authors')
    first_author = x.split()[1]
    return '<span style="display:none;">'+first_author+'</span>' + x

file = 'amr_papers.tsv'
file2 = 'index.html'
template = open('template.html','r',encoding='utf8').read()
with open(file, 'r', encoding='utf8') as f:
    i = 0
    l, r='{','}'
    for line in f:
        if i==0:
            i+=1
            continue
        bib = f'''
            <tr>
                <td>{get(line,'title')} </td>
                <td>{authors(line)}</td>
                <td>{get(line,'venue')}</td>
                <td>{get(line,'year')}</td>
                <td>{link(line)}</td>
                <td>{arxiv(line)}</td>
                <td>{tags(line)}</td>
            </tr>
        '''
        print(bib)
        rows.append(bib)
        i += 1

with open(file2, 'w', encoding='utf8') as f:
    heading = '''
    <table class="tablesorter">
    <thead>
        <tr>
            <th>Title</th>
            <th>Authors</th>
            <th>Venue</th>
            <th>Year</th>
            <th>Link(s)</th>
            <th>Arxiv</th>
            <th>Tags</th>
        </tr>
    </thead>
    <tbody>
    '''
    f.write(template.replace('{}', heading+''.join(rows)+'\n</tbody>\n</table>'))

for topic in sorted(topics):
    print(topic)