# @inproceedings{ah2006,
#    author={Aggarwal, Gagan and Hartline, Jason D.},
#    year={2006},
#    title={Knapsack auctions},
#    booktitle={Proceedings of the 17th Annual ACM-SIAM Symposium on Discrete Algorithms},
#    pages={1083-1092},
#    publisher={Association for Computing Machinery},
#    address={New York}
# }

bibs = []

def get(text,col):
    return '{'+text.split('\t')[col]+'}'


file = 'amr_papers.tsv'
file2 = 'amr_papers.bib'
with open(file, 'r', encoding='utf8') as f:
    i = 0
    l, r='{','}'
    for line in f:
        if i==0:
            i+=1
            continue
        bib = f'''
        @inproceedings{l}bib{i},
            author={get(line,0)},
            year={get(line,3)},
            title={get(line,1)},
            venue={get(line,2)},
            link={get(line,4)},
            arxiv={get(line,5)}
        {r}   
        '''
        print(bib)
        bibs.append(bib)
        i += 1

with open(file2, 'w', encoding='utf8') as f:
    f.write(''.join(bibs))