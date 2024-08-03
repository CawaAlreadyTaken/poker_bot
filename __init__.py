from random import shuffle, random, randint

POKER = 0
FULL = 0
COLORE = 0
SCALA = 0
TRIS = 0
DOPPIA_COPPIA = 0
COPPIA = 0
CARTA_ALTA = 0
PARI = 0

POKER_GIOCATORE = 0
FULL_GIOCATORE = 0
COLORE_GIOCATORE = 0
SCALA_GIOCATORE = 0
TRIS_GIOCATORE = 0
DOPPIA_COPPIA_GIOCATORE = 0
COPPIA_GIOCATORE = 0
CARTA_ALTA_GIOCATORE = 0
PARI = 0

valori = [
    "CARTA ALTA",
    "COPPIA",
    "DOPPIA COPPIA",
    "TRIS",
    "SCALA",
    "COLORE",
    "FULL",
    "POKER"
]

def createMazzo(mieCarte = [], flop = []):
    mazzo = [x for x in range(52)]
    shuffle(mazzo)
    for x in mieCarte:
        mazzo.remove(x)
    for i in range(len(flop)):
        x = flop[i]
        mazzo[mazzo.index(x)] = mazzo[i]
        mazzo[i] = x
    return mazzo

def poker(tutte, giocatore=False):
    global POKER_GIOCATORE
    ordered = sorted([x % 13 for x in tutte])
    last = ordered[-1]
    _poker = -1
    trovate = 1
    
    for carta in ordered[-2::-1]:
        if carta == last:
            trovate += 1
            if trovate == 4:
                _poker = carta
                break
        else:
            trovate = 1
        last = carta
    
    if _poker == -1:
        return False

    ordered.pop(ordered.index(_poker))
    ordered.pop(ordered.index(_poker))
    ordered.pop(ordered.index(_poker))
    ordered.pop(ordered.index(_poker))

    if giocatore:
        POKER_GIOCATORE+=1

    return ("POKER", _poker, ordered[-1])


def full(tutte, giocatore=False):
    global FULL_GIOCATORE
    ordered = [x % 13 for x in tutte]
    is_tris = tris(ordered)
    if is_tris == False:
       return False
    _, _tris, _ = is_tris
    others = []
    for x in ordered:
        if x == _tris:
            continue
        others.append(x)
    
    is_coppia = coppia(others)
    if is_coppia == False:
        return False
    
    if giocatore:
        FULL_GIOCATORE += 1

    return ("FULL", _tris, is_coppia[1])

def colore(tutte, giocatore=False):
    global COLORE_GIOCATORE
    colori = [int(x//13) for x in tutte]
    if colori.count(0) >= 5 or colori.count(1) >= 5 or colori.count(2) >= 5 or colori.count(3) >= 5:
        if giocatore:
            COLORE_GIOCATORE += 1
        return ("COLORE", _)
    return False


def scala(tutte, giocatore=False):
    global SCALA_GIOCATORE
    ordered = sorted(list(set([x % 13 for x in tutte])))
    last = ordered[-1]
    _scala = -1
    trovate = 1
    
    for carta in ordered[-2::-1]:
        if carta == last-1:
            trovate += 1
            if trovate == 5:
                _scala = carta
                break
        else:
            trovate = 1
        last = carta
    
    if _scala == -1:
        if (ordered[0] + ordered[1] + ordered[2] + ordered[3]) == 6 and 12 in ordered:
            if giocatore:
                SCALA_GIOCATORE+=1
            return ("SCALA", ordered[3])
        return False
    
    if giocatore:
        SCALA_GIOCATORE+=1
    return ("SCALA", _scala)


def tris(tutte, giocatore=False):
    global TRIS_GIOCATORE
    ordered = sorted([x % 13 for x in tutte])
    last = ordered[-1]
    _tris = -1
    trovata = False
    
    for carta in ordered[-2::-1]:
        if carta == last:
            if trovata:
                _tris = carta
                break
            else:
                trovata = True
        else:
            trovata = False
        last = carta
    
    if _tris == -1:
        return False

    ordered.pop(ordered.index(_tris))
    ordered.pop(ordered.index(_tris))
    ordered.pop(ordered.index(_tris))

    if giocatore:
        TRIS_GIOCATORE += 1

    return ("TRIS", _tris, ordered[-1:-3:-1])



def doppia_coppia(tutte, giocatore=False):
    global DOPPIA_COPPIA_GIOCATORE
    ordered = sorted([x % 13 for x in tutte])
    last = ordered[-1]
    coppiaPrima = -1
    coppiaSeconda = -1

    for carta in ordered[-2::-1]:
        if carta == last:
            coppiaPrima = carta
            break
        last = carta

    if coppiaPrima == -1:
        return False
    ordered.pop(ordered.index(coppiaPrima))
    ordered.pop(ordered.index(coppiaPrima))
    last = ordered[-1]

    for carta in ordered[-2::-1]:
        if carta == last:
            coppiaSeconda = carta
            break
        last = carta

    if coppiaSeconda == -1:
        return False

    ordered.pop(ordered.index(coppiaSeconda))
    ordered.pop(ordered.index(coppiaSeconda))

    if giocatore:
        DOPPIA_COPPIA_GIOCATORE += 1

    return ("DOPPIA COPPIA", coppiaPrima, coppiaSeconda, ordered[-1])

def coppia(tutte, giocatore=False):
    global COPPIA_GIOCATORE

    ordered = sorted([x % 13 for x in tutte])
    last = ordered[-1]
    _coppia = -1

    for carta in ordered[-2::-1]:
        if carta == last:
            _coppia = carta
            break
        last = carta

    if _coppia == -1:
        return False
    ordered.pop(ordered.index(_coppia))
    ordered.pop(ordered.index(_coppia))

    if giocatore:
        COPPIA_GIOCATORE += 1
    return ("COPPIA", _coppia, ordered[-1:-4:-1])

def strCarta(valore):
    return "23456789TJQKA"[valore%13] + " di " + ["picche", "cuori", "quadri", "fiori"][valore//13]


def calcolaValore(carte, altre_5, giocatore=False):
    global POKER, FULL, COLORE, SCALA, TRIS, DOPPIA_COPPIA, COPPIA, CARTA_ALTA, CARTA_ALTA_GIOCATORE
    _poker = poker(carte + altre_5, giocatore)
    if _poker != False:
        POKER += 1
        return _poker
    _full = full(carte + altre_5, giocatore)
    if _full != False:
        FULL += 1
        return _full
    _colore = colore(carte + altre_5, giocatore)
    if _colore != False:
        COLORE += 1
        return _colore
    _scala = scala(carte + altre_5, giocatore)
    if _scala != False:
        SCALA += 1
        return _scala
    _tris = tris(carte + altre_5, giocatore)
    if _tris != False:
        TRIS += 1
        return _tris
    _doppia_coppia = doppia_coppia(carte + altre_5, giocatore)
    if _doppia_coppia != False:
        DOPPIA_COPPIA += 1
        return _doppia_coppia
    _coppia = coppia(carte + altre_5, giocatore)
    if _coppia != False:
        COPPIA += 1
        return _coppia
    CARTA_ALTA += 1
    if giocatore:
        CARTA_ALTA_GIOCATORE += 1
    return ("CARTA ALTA", sorted([x % 13 for x in carte + altre_5])[:-5:-1])




def spareggio(valore1, valore2):
    # Ritorna vinto_il_primo, valore
    match valore1[0]:
        case "CARTA ALTA":
            for x, y in zip(valore1[1], valore2[1]):
                if x > y:
                    return 1, valore1
                if x < y:
                    return -1, valore2
        case "COPPIA":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
            for x, y in zip(valore1[2], valore2[2]):
                if x > y:
                    return 1, valore1
                if x < y:
                    return -1, valore2
        case "DOPPIA COPPIA":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
            if valore1[2] > valore2[2]:
                return 1, valore1
            if valore1[2] < valore2[2]:
                return -1, valore2
            if valore1[3] > valore2[3]:
                return 1, valore1
            if valore1[3] < valore2[3]:
                return -1, valore2
        case "TRIS":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
            for x, y in zip(valore1[2], valore2[2]):
                if x > y:
                    return 1, valore1
                if x < y:
                    return -1, valore2
        case "SCALA":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
        case "COLORE":
            pass
        case "FULL":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
            if valore1[2] > valore2[2]:
                return 1, valore1
            if valore1[2] < valore2[2]:
                return -1, valore2
        case "POKER":
            if valore1[1] > valore2[1]:
                return 1, valore1
            if valore1[1] < valore2[1]:
                return -1, valore2
    # Assumendo che in caso di pareggio totale vinca "io"
    return 0, valore1

def fintoSpareggio(quantiGiocatoriUguali):
    return random() <= (1/quantiGiocatoriUguali)

def play(mieCarte = [], flop = []):
    global PARI
    mazzo = createMazzo(mieCarte, flop=flop)

    altre = mazzo[:5]
    mazzo = mazzo[5:]

    if mieCarte is not None:
        mine = mieCarte
    else:
        mine = mazzo[:2]
        mazzo = mazzo[2:]
    giocatori =  [[] for _ in range(N_PLAYERS-1)]
    for mano in giocatori:
        mano.append(mazzo[0])
        mano.append(mazzo[1])
        mazzo = mazzo[2:]

    valoreMio = calcolaValore(mine, altre, True)
    valoreMax = None

    for mano in giocatori:
        valore = calcolaValore(mano, altre)
        if valoreMax is None or valori.index(valore[0]) > valori.index(valoreMax[0]):
            valoreMax = valore
        elif valori.index(valore[0]) == valori.index(valoreMax[0]):
            _, valoreMax = spareggio(valoreMax, valore)

    if valoreMio[0] == valoreMax[0]:
        res = spareggio(valoreMio, valoreMax)[0]
        if res == 1:
            vinto = True
        elif res == -1:
            vinto = False
        else:
            PARI += 1
            vinto = False
    elif valori.index(valoreMio[0]) > valori.index(valoreMax[0]):
        vinto = True
    else:
        vinto = False

    return vinto

N_PLAYERS = 6
N_GAMES = 30000

if __name__ == "__main__":
    mieCarte = [0, 15]
    flop = [13, 28, 31, 35, 42]
    vinte = 0
    for _ in range(N_GAMES):
        vinte += play(mieCarte=mieCarte, flop=flop)
    print(f"Su {N_GAMES} partite di {N_PLAYERS} giocatori")
    print(f"Percentuale vittorie: {vinte*100/N_GAMES}%")
    print(f"Percentuale pareggi: {PARI*100/N_GAMES}%")
    if mieCarte is not None:
        print(f"Carte in mano: {strCarta(mieCarte[0])}, {strCarta(mieCarte[1])}")
    for carta in flop:
        print(f"Flop: {strCarta(carta)}")
    print(f"Poker: {POKER}")
    print(f"Full: {FULL}")
    print(f"Colore: {COLORE}")
    print(f"Scala: {SCALA}")
    print(f"Tris: {TRIS}")
    print(f"Doppia coppia: {DOPPIA_COPPIA}")
    print(f"Coppia: {COPPIA}")
    print(f"Carta Alta: {CARTA_ALTA}")
    print()
    print(f"Poker - giocatore: {POKER_GIOCATORE*100/N_GAMES}%")
    print(f"Full - giocatore: {FULL_GIOCATORE*100/N_GAMES}%")
    print(f"Colore - giocatore: {COLORE_GIOCATORE*100/N_GAMES}%")
    print(f"Scala - giocatore: {SCALA_GIOCATORE*100/N_GAMES}%")
    print(f"Tris - giocatore: {TRIS_GIOCATORE*100/N_GAMES}%")
    print(f"Doppia coppia - giocatore: {DOPPIA_COPPIA_GIOCATORE*100/N_GAMES}%")
    print(f"Coppia - giocatore: {COPPIA_GIOCATORE*100/N_GAMES}%")
    print(f"Carta Alta - giocatore: {CARTA_ALTA_GIOCATORE*100/N_GAMES}%")

