import random

hang = ["""
H A N G M A N - Footballer Edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def lojtari_random():
    lojtaret = ['benzema', 'salah', 'mbappe', 'haaland', 'lewandowski', 'modric', 'pogba', 'foden',
                'kante', 'vinicius', 'pedri', 'fati', 'ronaldo', 'messi', 'ozil', 'neymar', 'pele', 'maradona',
                'zidane', 'gnabry', 'kane', 'mane', 'alcantara', 'mahrez', 'virgil']

    lojtari = random.choice(lojtaret)
    return lojtari


def shfaqja(hang, shkronja_gabim, shkronja_e_sakte, lojtari_sekret):
    print(hang[len(shkronja_gabim)])
    print()

    print('Shkronjat gabim:', end=' ')
    for shkronja in shkronja_gabim:
        print(shkronja, end=' ')
    print("\n")

    zbrastirat = '_' * len(lojtari_sekret)

    for i in range(len(lojtari_sekret)):
        if lojtari_sekret[i] in shkronja_e_sakte:
            zbrastirat = zbrastirat[:i] + lojtari_sekret[i] + zbrastirat[i + 1:]

    for shkronja in zbrastirat:
        print(shkronja, end=' ')
    print("\n")


def hamendsimi(te_hamendesuarat):
    while True:
        hamendeso = input('Hamendesoni nje shkronje: ')
        hamendeso = hamendeso.lower()
        if len(hamendeso) != 1:
            print('Ju lutem shkruani nje shkronje te vetme.')
        elif hamendeso in te_hamendesuarat:
            print('Ju tashme e keni hamendesuar ate shkronje.Ju lutem zgjidhni nje shkronje tjeter perseri.')
        elif hamendeso not in 'abcdefghijklmnopqrstuvwxyz':
            print('Ju lutem shkruani nje shkronje.')
        else:
            return hamendeso


def luani_perseri():
    return input("\nDeshironi te luani perseri? ").lower().startswith('p')


shkronja_gabim = ''
shkronja_e_sakte = ''
lojtari_sekret = lojtari_random()
loja_ka_mbaruar = False

while True:
    shfaqja(hang, shkronja_gabim, shkronja_e_sakte, lojtari_sekret)

    hamendeso = hamendsimi(shkronja_gabim + shkronja_e_sakte)

    if hamendeso in lojtari_sekret:
        shkronja_e_sakte = shkronja_e_sakte + hamendeso

        te_gjitha_shkronjats = True
        for i in range(len(lojtari_sekret)):
            if lojtari_sekret[i] not in shkronja_e_sakte:
                te_gjitha_shkronjats = False
                break
        if te_gjitha_shkronjats:
            print('\nJu keni gjetur lojtarin. Lojtari sekret eshte:  "' +
                  lojtari_sekret + '"! Urime, keni fituar!!')
            loja_ka_mbaruar = True
    else:
        shkronja_gabim = shkronja_gabim + hamendeso

        if len(shkronja_gabim) == len(hang) - 1:
            shfaqja(hang, shkronja_gabim,
                    shkronja_e_sakte, lojtari_sekret)
            print(
                'Ju kane mbaruar hamendesimet!\nPas ' + str(len(shkronja_gabim)) + ' hamendesimeve te humbura dhe ' +
                str(len(shkronja_e_sakte)) + ' hamendesimeve te sakta, lojtari ishte "' + lojtari_sekret + '"')
            loja_ka_mbaruar = True

    if loja_ka_mbaruar:
        if luani_perseri():
            shkronja_gabim = ''
            shkronja_e_sakte = ''
            loja_ka_mbaruar = False
            lojtari_sekret = lojtari_random()
        else:
            break
