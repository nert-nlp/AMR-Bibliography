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
    return text.split('\t')[columns[col]]


file = 'amr_papers.tsv'
file2 = 'amr_papers.html'
with open(file, 'r', encoding='utf8') as f:
    i = 0
    l, r='{','}'
    for line in f:
        if i==0:
            i+=1
            continue
        bib = f'''
            <tr>
                <td>"{get(line,'title')}" </td>
                <td>({get(line,'authors')}).</td>
                <td>{get(line,'venue')}, </td>
                <td>{get(line,'year')}.</td>
                <td><a href="{get(line,'links')}">link</a>, </td>
                <td><a href="{get(line,'arxiv')}">arxiv</a>, . </td>
                <td><b>[{get(line,'tags')}]</b></td>
            </tr>
        '''
        print(bib)
        rows.append(bib)
        i += 1

with open(file2, 'w', encoding='utf8') as f:
    heading = '''
    <table>
        <tr>
            <th>Title</th>
            <th>Authors</th>
            <th>Venue</th>
            <th>Year</th>
            <th>Link(s)</th>
            <th>Arxiv</th>
            <th>Tags</th>
        </tr>
    '''
    f.write(heading+''.join(rows)+'\n</table>')