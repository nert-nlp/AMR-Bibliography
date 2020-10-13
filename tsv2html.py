from collections import defaultdict, Counter

file = 'data/amr_papers.tsv'
file2 = 'index.html'
template = open('template.html' ,'r' ,encoding='utf8').read()

# <table style="width:100%">
#   <tr>
#     <th>#</th>
#     <th>Title</th>
#     <th>Authors</th>
#     <th>Venue</th>
#     <th>Year</th>
#     <th>Link(s)</th>
#     <th>Arxiv</th>
#     <th>Tags</th>
#   </tr>
#   <tr>
#     <td>?</td>
#     <td>?</td>
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

paperCounts = defaultdict(Counter)  # topic => {year => count}

def get(text ,col):
    columns = {'authors' :0 ,'title' :1 ,'year' :3 ,'venue' :2 ,'links' :4 ,'arxiv' :5 ,'tags' :6,'review' :7}
    x = text.split('\t')[columns[col]]
    if x and x[0] == '"' and x[-1] == '"':
        x = x[1:-1]
    return x.strip()


def link(line):
    x = get(line ,'links')
    if x and x[0] == '{' and x[-1] == '}':
        x = x[1:-1]
        links = {}
        x = x.split(',')
        for l in x:
            if ':' not in l: continue
            s = l.split(':', 1)
            links[s[0].strip()] = s[1].strip()
        return ', '.join(f'<a href="{links[l]}" target="_blank">{l}</a>' for l in links)
    elif 'href' in x:
        return x
    elif x.strip():
        return f'<a href="{x}" target="_blank">pdf</a>'
    else:
        return ''

def arxiv(line):
    x = get(line ,'arxiv')
    if x.strip():
        return f'<a href="{x}" target="_blank">arXiv</a>'
    else:
        return ''

years = set()
year = ''
def get_year():
    global year # dirty hack so year is available in tags()
    year = get(line,'year')
    years.add(year)
    return year

topics = set()
def tags(line):
    tags = []
    tag_buttons = []
    x = get(line ,'tags')
    x = x.split(', ')
    for tag in x:
        if not tag.strip(): continue
        tag = tag.replace('"' ,'').strip()
        tags.append(tag)
        topic = tag.lower().replace('+' ,'').strip()
        topics.add(tag.strip())
        tag_buttons.append(f'<button topic="{topic}" on="0">{tag}</button>')
    # Count paper by its first tag
    if tags:
        firsttag = tags[0]
        # don't display these tag in chart
        if tags[0] == 'Shared Task Overview':
            firsttag = tags[1]
    else:
        firsttag = 'Misc'
    paperCounts[firsttag][year] += 1
    return ' '.join(tag_buttons)

def authors(line):
    x = get(line ,'authors')
    first_author = x.split(',')[0].strip()
    first_author = first_author.split()[-1]
    return '<span style="display:none;">' +first_author +'</span>' + x

with open(file, 'r', encoding='utf8') as f:
    i = 0
    l, r= '{', '}'
    for line in f:
        if i == 0:
            i += 1
            continue
        bib = f'''
            <tr>
                <td>{i}</td>
                <td>{get(line,'title')} </td>
                <td>{authors(line)}</td>
                <td>{get(line,'venue')}</td>
                <td>{get_year()}</td>
                <td>{link(line)}</td>
                <td>{arxiv(line)}</td>
                <td>{tags(line)}</td>
            </tr>
        '''
        rows.append(bib)
        i += 1

# Black + Tol palette from https://davidmathlogic.com/colorblind/
COLOR_PALETTE = ['#332288', '#117733', '#44AA99', '#88CCEE', '#DDCC77', '#CC6677', '#AA4499', '#882255', '#000000']

counts = []

years = sorted(years)

if '' in years: # entries with no date: count them but don't display in chart
    years.remove('')

nPapers = 0

iColor = 0

for tag in sorted(paperCounts.keys()):
    nPapers += sum(paperCounts[tag].values())
    if sum(paperCounts[tag][y] for y in years)>0:
        counts.append('{\n' + f'''label: {tag!r},
                data: {[paperCounts[tag][year] for year in years]!r},
                backgroundColor: {COLOR_PALETTE[iColor % len(COLOR_PALETTE)]!r}''' + '\n},')
        iColor += 1

with open(file2, 'w', encoding='utf8') as f:
    heading = '''
    <table class="tablesorter">
    <thead>
        <tr>
            <th>#</th>
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
    f.write(template.replace('{NPAPERS}', str(nPapers)).replace('{YEARS}', str(years)).replace('{COUNTS}', '\n'.join(counts)).replace('{ROWS}', heading + ''.join(rows) + '\n</tbody>\n</table>'))

for topic in sorted(topics):
    print(topic)
