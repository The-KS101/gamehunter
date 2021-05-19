import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset = pd.read_csv('MetaCritic All games Gen 4 Draft 2.csv')

def LCS(a, names):
    lcsVal = []
    for i in names:
        grid = np.zeros((len(i), len(a)))
        for j in range(len(i)):
            for k in range(len(a)):
                if i[j] == a[k]:
                    grid[j][k] = 1 + grid[j-1][k-1]
                else:
                    grid[j][k] = 0
        maxVal = 0
        for i in grid:
            if max(i) > maxVal:
                maxVal = max(i)
        lcsVal.append(maxVal)
    return lcsVal.index(max(lcsVal))


def get_name(title):
    names = dataset['names'].str.lower()
    
    try:
        idx = names[names == title.lower()].index[0]
        print('Similar Games goten for {}'.format(names[idx]))
        
    except:
        idx = LCS(title.lower(), names)
        print('Given Name not found, displaying most similar name, {}'
              .format(dataset['names'][idx]))

    return names, idx


def getRecommend(title, dataset=dataset, console=None, sort=None, order=None):
    names, idx = get_name(title)


    gameShown = dataset['names'][idx]
    if console != None:
        eligible_index = dataset[dataset['platforms'] == console].index
        sims = cosine_sim_row(vec_matrix[idx], vec_matrix)
        print(f"look")
        mostSimIndex = np.argsort(sims)
        mostSimElig = [i for i in mostSimIndex if i in eligible_index]
        mostSim = mostSimElig[:: -1][1:30]
    else:
        sims = cosine_sim_row(vec_matrix[idx], vec_matrix)
        mostSimIndex = np.argsort(sims)
        mostSim = mostSimIndex[:: -1][1:30]
        print("we are here")

    similarGames = []
    if sort:
        simSort = {}
        for i in mostSim:
            simSort.update({names[i]: dataset[sort][i]})
        rev = True if order=="True" else False
        simSorted = sorted(simSort.items(), key=lambda x: x[1], reverse=rev)
        for key in simSorted:
            similarGames.append(key[0])
    else:
        [similarGames.append(names[i]) for i in mostSim if names[i] not in similarGames]

    return similarGames, gameShown

def cosine_sim_row(m, n):
    m = np.squeeze(np.asarray(m.A))
    sims = [np.dot(m, np.squeeze(np.asarray(i.A)))/(np.linalg.norm(m)*np.linalg.norm(np.squeeze(np.asarray(i.A)))) for i in n ]
    return sims

cv = CountVectorizer(stop_words='english')
vec_matrix = cv.fit_transform(dataset['combined words'])
print(vec_matrix.data.nbytes)


