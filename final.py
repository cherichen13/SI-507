import csv

'''Read the csv file and put it into a list'''
song_info = []


filename = 'C:/Users/xy_ch/Desktop/umich/507/final/spo.csv'
with open(filename,encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers =next(f_csv)
    
    for row in f_csv:
        song_info.append(row)


'''Get the music genres'''
gen = []
genres = []
for item in song_info:
    gen.append(item[2])
    genres = list(set(gen))  # get the unique music genres
genres.sort()  # make the order of the elements fixed, since the order of the result of set() is random


'''Get the artist types, same as getting the music genres'''
ar_type = []
artist_type = []
for item in song_info:
    ar_type.append(item[-1])
    artist_type = list(set(ar_type))
artist_type.sort()


'''Create some genreal music genre lists to store the more detailed music genres'''
pop = []
rap = []
soul = []
hiphop = []
rock = []
house = []
dance = []
indie = []
rnb = []
others = []

music_genre = ['pop','rap','soul','hiphop','rock',
               'house','dance','indie','rnb','others']

for i in genres:
    if i[-3:] == 'pop':
        pop.append(i)
    elif i[-4:] == ' rap' or i == 'rap':
        rap.append(i)
    elif i[-4:] == 'soul':
        soul.append(i)
    elif i[-7:] == 'hip hop':
        hiphop.append(i)
    elif i[-4:] == 'rock':
        rock.append(i)
    elif i[-5:] == 'house':
        house.append(i)
    elif i[-5:] == 'dance':
        dance.append(i)
    elif i[-5:] == 'indie':
        indie.append(i)
    elif i[-3:] == 'r&b':
        rnb.append(i)
    else:
        others.append(i)


'''Create some artist type lists to store the songs of that artist type'''
Duo = []
Band_Group = []
Trio = []
Solo = []

for s in song_info:
    if s[-1] == 'Duo':
        Duo.append(s)
    elif s[-1] == 'Band/Group':
        Band_Group.append(s)
    elif s[-1] == 'Trio':
        Trio.append(s)
    else:
        Solo.append(s)

type_lst = [Band_Group,Duo,Solo,Trio]


'''Create an empty tree to store the data'''
song_tree = {'Duo':{'pop':[],'rap':[],'soul':[],
                    'hiphop':[],'rock':[],'house':[],
                    'dance':[],'indie':[],'rnb':[],
                    'others':[]},
             'Band/Group':{'pop':[],'rap':[],'soul':[],
                           'hiphop':[],'rock':[],'house':[],
                           'dance':[],'indie':[],'rnb':[],
                           'others':[]},
             'Trio':{'pop':[],'rap':[],'soul':[],
                     'hiphop':[],'rock':[],'house':[],
                     'dance':[],'indie':[],'rnb':[],
                     'others':[]},
             'Solo':{'pop':[],'rap':[],'soul':[],
                     'hiphop':[],'rock':[],'house':[],
                     'dance':[],'indie':[],'rnb':[],
                     'others':[]}}


'''Define a function to append the songs to the tree'''
def buildtree(lst):
    for t in range(len(lst)):
        for s in lst[t]:
            if s[2] in pop:
                song_tree[artist_type[t]]['pop'].append(s)
            elif s[2] in rap:
                song_tree[artist_type[t]]['rap'].append(s)
            elif s[2] in soul:
                song_tree[artist_type[t]]['soul'].append(s)
            elif s[2] in hiphop:
                song_tree[artist_type[t]]['hiphop'].append(s)
            elif s[2] in rock:
                song_tree[artist_type[t]]['rock'].append(s)
            elif s[2] in house:
                song_tree[artist_type[t]]['house'].append(s)
            elif s[2] in dance:
                song_tree[artist_type[t]]['dance'].append(s)
            elif s[2] in indie:
                song_tree[artist_type[t]]['indie'].append(s)
            elif s[2] in rnb:
                song_tree[artist_type[t]]['rnb'].append(s)
            else:
                song_tree[artist_type[t]]['others'].append(s)
    return song_tree

tree = buildtree(type_lst)


'''The interactive part: '''
Q1 = 'Which year are you looking for?'
Q2 = 'What artist type are you looking for?'
Q3 = 'What music genre are you looking for?'

while True:
    songyear = input(f'{Q1} Choose from: 2015-2019 (enter "q" to quit)\n')
    if songyear != 'q':
        artisttype = input(f'{Q2} Choose from: {artist_type}\n')
        musicgenre = input(f'{Q3} Chhose from: {music_genre}\n')
        final_list = []
        song_list = tree[artisttype][musicgenre]
        for s in song_list:
            if s[-2] == songyear:
                final_list.append(s)
        if len(final_list) == 0:
            print('No songs')
        else:
            for song in final_list:
                print(f'{song[0]} ({song[1]})')
    else:
        print('bye!')
        break