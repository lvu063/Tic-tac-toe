def effaceTableau(tab):
    '''
    (list) -> None
    Cette fonction prepare le tableau de jeu (la matrice) 
    en mettant '-' dans tous les elements.
    Elle ne crée pas une nouvelle matrice
    Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    for i in range(len(tab)):
        for k in range(len(tab[i])):
            tab[i][k] = "-"
                

def verifieGagner(tab):
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    if testLignes(tab) == "X" or testCols(tab) == "X" or testDiags(tab) == "X":
      print("Joueur X a gagné!")
      return True
    elif testLignes(tab) == "O" or testCols(tab) == "O" or testDiags(tab) == "O":
        print("Joueur O a gagné!")
        return True
    elif testMatchNul == True:
        print("Match nul")
        return True
    else:
        return False


def testLignes(tab):
    ''' (list) ->  str
    * verifie s’il y a une ligne gagnante.
    * cherche trois 'X' ou trois 'O' dans une ligne.  
    * Si on trouve, le caractere 'X' ou 'O' est retourné, sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    if (tab[0][0] == 'X' and tab[0][1] == 'X' and tab[0][2] == 'X'):
        return "X"
    elif (tab[0][0] == 'O' and tab[0][1] == 'O' and tab[0][2] == 'O'):
        return "O"
    elif (tab[1][0] == 'X' and tab[1][1] == 'X' and tab[1][2] == 'X'):
        return "X"
    elif (tab[1][0] == 'O' and tab[1][1] == 'O' and tab[1][2] == 'O'):
        return "O"
    elif (tab[2][0] == 'X' and tab[2][1] == 'X' and tab[2][2] == 'X'):
        return "X"
    elif (tab[2][0] == 'O' and tab[2][1] == 'O' and tab[2][2] == 'O'):
        return "O"
    else:
        return "-"


def testCols(tab):
    ''' (list) ->  str
    * verifie s’il y a une colonne gagnante.
    * cherche trois 'X' ou trois 'O' dans une colonne.  
    * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    if (tab[0][0] == 'X' and tab[1][0] == 'X' and tab[2][0] == 'X'):
        return "X"
    elif (tab[0][0] == 'O' and tab[1][0] == 'O' and tab[2][0] == 'O'):
        return "O"
    elif (tab[0][1] == 'X' and tab[1][1] == 'X' and tab[2][1] == 'X'):
        return "X"
    elif (tab[0][1] == 'O' and tab[1][1] == 'O' and tab[2][1] == 'O'):
        return "O"
    elif (tab[0][2] == 'X' and tab[1][2] == 'X' and tab[2][2] == 'X'):
        return "X"
    elif (tab[0][2] == 'O' and tab[1][2] == 'O' and tab[2][2] == 'O'):
        return "O"
    else:
        return "-"


def testDiags(tab):
    ''' (list) ->  str
    * cherche trois 'X' ou trois 'O' dans une diagonale.  
    * Si on trouve, le caractere 'X' ou 'O' et retourné
    * sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    if (tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X'):
        return "X"
    elif (tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O'):
        return "O"
    elif (tab[0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X'):
        return "X"
    elif (tab[0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O'):
        return "O"
    else:
        return "-"


def testMatchNul(tab):
    ''' (list) ->  bool
    * verifie s’il y a un match nul
    * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
    * Si on ne trouve pas de '-' dans la matrice, retourne True. 
    * S'il y a de '-', retourne false.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    row = 0
    while row < len(tab):
        col = 0
        while col < len(tab[row]):
            A[row][col] == "X" or A[row][col] == "O"
            return True
            col += 1
        row += 1
    return False
