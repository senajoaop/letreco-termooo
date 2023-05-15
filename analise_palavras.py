import os, sys
import re
import string
import unidecode
import matplotlib.pyplot as plt


class Letra:
    def __init__(self, source='palavras_wordle.txt'):
        dic5 = []

        # path = 'C:\\Users\\SENA\\Desktop\\mon_tonton\\palavras.txt'
        # path = 'C:\\Users\\SENA\\Desktop\\letreco_termooo\\palavras_termooo.txt'
        # path = 'C:\\Users\\SENA\\Desktop\\letreco_termooo\\palavras_letreco.txt'
        # path = 'C:\\Users\\SENA\\Desktop\\letreco_termooo\\palavras_wordle.txt'
        # path = 'palavras_wordle.txt'

        path = os.path.join(os.getcwd(), "data", source)

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                lineStrip = line.strip()

                if len(lineStrip)==5:
                    dic5.append(lineStrip)

        dic5Origin = [word.lower() for word in dic5 if not any(ch in string.punctuation for ch in word)]
        dic5 = [unidecode.unidecode(word.lower()) for word in dic5 if not any(ch in string.punctuation for ch in word)]

        united = ''.join(dic5)
        unitedOrder = [''.join([word[p] for word in dic5]) for p in range(5)]

        united1 = ''.join([word[0] for word in dic5])
        united2 = ''.join([word[1] for word in dic5])
        united3 = ''.join([word[2] for word in dic5])
        united4 = ''.join([word[3] for word in dic5])
        united5 = ''.join([word[4] for word in dic5])


        alphabet = list(string.ascii_lowercase)

        counter = {}
        counterOrder = {}
        counter1, counter2, counter3, counter4, counter5 = {}, {}, {}, {}, {}

        for letter in alphabet:
            counter[letter] = len(re.findall(letter, united))
            counterOrder[letter] = [len(re.findall(letter, item)) for item in unitedOrder]

            counter1[letter] = len(re.findall(letter, united1))
            counter2[letter] = len(re.findall(letter, united2))
            counter3[letter] = len(re.findall(letter, united3))
            counter4[letter] = len(re.findall(letter, united4))
            counter5[letter] = len(re.findall(letter, united5))


        counterAll = [counter1, counter2, counter3, counter4, counter5]

        scoreP1, scoreP2, scoreP3 = [], [], []

        weightP1 = []
        scoreP1W = []

        for word in dic5:
            scoreAux1 = 0
            scoreAux2 = 0
            scoreAux3 = 0
            
            for idx, letter in enumerate(word):
                scoreAux1 += counter[letter]
                scoreAux2 += counterAll[idx][letter]
                scoreAux3 += counterOrder[letter][idx]

            weight = len(set(word))
            weightP1.append(weight)

            scoreP1.append(scoreAux1)
            scoreP1W.append(scoreAux1 * weight)
            scoreP2.append(scoreAux2)
            scoreP3.append(scoreAux3)


        scoreP1WOrdered, dic5OrderedP1W, dic5OrderedP1WOrigin = map(list, zip(*sorted(zip(scoreP1W, dic5, dic5Origin), reverse=True)))
        print(scoreP1WOrdered[:5], dic5OrderedP1W[:5])

        scoreP2Ordered, dic5OrderedP2, dic5OrderedP2Origin = map(list, zip(*sorted(zip(scoreP2, dic5, dic5Origin), reverse=True)))
        print(scoreP2Ordered[:5], dic5OrderedP2[:5])

        for i in range(20):
            print(f'P1: {dic5OrderedP1WOrigin[i]} ({scoreP1WOrdered[i]})  --  P2: {dic5OrderedP2Origin[i]} ({scoreP2Ordered[i]})')



        # pathP1 = 'C:\\Users\\SENA\\Desktop\\letreco_termooo\\P1_50.txt'
        # pathP2 = 'C:\\Users\\SENA\\Desktop\\letreco_termooo\\P2_50.txt'
        pathP1 = 'P1_50.txt'
        pathP2 = 'P2_50.txt'

        with open(pathP1, 'w') as file:
            for idx, name in enumerate(dic5OrderedP1WOrigin[:60]):
                file.write(f'{idx+1} - {name}\n')

        with open(pathP2, 'w') as file:
            for idx, name in enumerate(dic5OrderedP2Origin[:60]):
                file.write(f'{idx+1} - {name}\n')


        counterBest7Let = sorted(counter, key=counter.get, reverse=True)[:7]
        counterBest7 = [counter[c] for c in counterBest7Let]

        counter1Best3Let = sorted(counter1, key=counter1.get, reverse=True)[:3]
        counter1Best3 = [counter1[c] for c in counter1Best3Let]
        counter2Best3Let = sorted(counter2, key=counter2.get, reverse=True)[:3]
        counter2Best3 = [counter1[c] for c in counter2Best3Let]
        counter3Best3Let = sorted(counter3, key=counter3.get, reverse=True)[:3]
        counter3Best3 = [counter1[c] for c in counter3Best3Let]
        counter4Best3Let = sorted(counter4, key=counter5.get, reverse=True)[:3]
        counter4Best3 = [counter1[c] for c in counter4Best3Let]
        counter5Best3Let = sorted(counter5, key=counter5.get, reverse=True)[:3]
        counter5Best3 = [counter1[c] for c in counter5Best3Let]

        plotBar1 = [counter1Best3[0], counter2Best3[0], counter3Best3[0], counter4Best3[0], counter5Best3[0]]
        plotBar1Let = [counter1Best3Let[0], counter2Best3Let[0], counter3Best3Let[0], counter4Best3Let[0], counter5Best3Let[0]]
        plotBar2 = [counter1Best3[1], counter2Best3[1], counter3Best3[1], counter4Best3[1], counter5Best3[1]]
        plotBar2Let = [counter1Best3Let[1], counter2Best3Let[1], counter3Best3Let[1], counter4Best3Let[1], counter5Best3Let[1]]
        plotBar3 = [counter1Best3[2], counter2Best3[2], counter3Best3[2], counter4Best3[2], counter5Best3[2]]
        plotBar3Let = [counter1Best3Let[2], counter2Best3Let[2], counter3Best3Let[2], counter4Best3Let[2], counter5Best3Let[2]]

        fig, ax = plt.subplots()
        ax.bar(counterBest7Let, counterBest7, color ='palevioletred', width = 0.4, edgecolor ='grey')
        plt.xlabel('Letras não ordenadas')
        plt.ylabel('Número de ocorrências')
        plt.title('Ocorrência')
        plt.show()


        fig, ax = plt.subplots()

        barWidth = 0.25
        br1 = range(len(plotBar1))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        
        rects1 = plt.bar(br1, plotBar1, width = barWidth, edgecolor ='grey', label ='IT', color='coral')
        rects2 = plt.bar(br2, plotBar2, width = barWidth, edgecolor ='grey', label ='ECE', color='yellowgreen')
        rects3 = plt.bar(br3, plotBar3, width = barWidth, edgecolor ='grey', label ='CSE', color='violet')

        plt.xticks([r + barWidth for r in range(len(plotBar1))], ['Letra 1', 'Letra 2', 'Letra 3', 'Letra 4', 'Letra 5'])

        def autolabel(rects, names):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for name, rect in zip(names, rects):
                height = rect.get_height()
                ax.annotate('{}'.format(name),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')


        autolabel(rects1, plotBar1Let)
        autolabel(rects2, plotBar2Let)
        autolabel(rects3, plotBar3Let)


        plt.xlabel('Posição da letra')
        plt.ylabel('Número de ocorrências')
        plt.title('Ocorrência por posição')


        plt.show()


if __name__=='__main__':
    Letra()
