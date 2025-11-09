"""
GENERATORE DI PASSWORD CASUALI
==============================
Programma didattico per imparare:
- Funzioni e modularità del codice
- Cicli for e while
- Liste e manipolazione stringhe
- Libreria random
- Input/output utente
"""

import random


# =============================================================================
# FUNZIONI DI UTILITÀ
# =============================================================================

def genera_password_base(lunghezza):
    """
    Genera una password iniziale solo con lettere minuscole.
    
    Args:
        lunghezza (int): Numero di caratteri della password
        
    Returns:
        str: Password con sole lettere minuscole
        
    Esempio:
        >>> genera_password_base(5)
        'abxyz'
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    
    # Costruiamo la password lettera per lettera
    for _ in range(lunghezza):
        # Scegliamo un indice casuale nell'alfabeto
        indice_casuale = random.randint(0, len(alfabeto) - 1)
        # Aggiungiamo la lettera corrispondente
        password += alfabeto[indice_casuale]
    
    return password


def aggiungi_numeri(password, quanti_numeri=2):
    """
    Sostituisce alcuni caratteri con numeri casuali.
    
    Args:
        password (str): Password da modificare
        quanti_numeri (int): Quanti numeri inserire (default 2)
        
    Returns:
        str: Password con numeri inseriti
    """
    password_modificata = password
    
    # Inseriamo numeri nella prima metà della password
    for _ in range(quanti_numeri):
        # Scegliamo una posizione casuale nella prima metà
        posizione = random.randint(0, len(password_modificata) // 2 - 1)
        numero_casuale = random.randint(0, 9)
        
        # Ricostruiamo la password: parte prima + numero + parte dopo
        password_modificata = (
            password_modificata[:posizione] +
            str(numero_casuale) +
            password_modificata[posizione + 1:]
        )
    
    return password_modificata


def aggiungi_maiuscole(password, quante_maiuscole=2):
    """
    Converte alcuni caratteri in maiuscolo.
    
    Args:
        password (str): Password da modificare
        quante_maiuscole (int): Quante maiuscole inserire (default 2)
        
    Returns:
        str: Password con lettere maiuscole
    """
    password_modificata = password
    
    # Inseriamo maiuscole nella seconda metà della password
    for _ in range(quante_maiuscole):
        # Scegliamo una posizione casuale nella seconda metà
        inizio_seconda_meta = len(password_modificata) // 2
        posizione = random.randint(inizio_seconda_meta, 
                                  len(password_modificata) - 1)
        
        # Convertiamo il carattere in maiuscolo
        password_modificata = (
            password_modificata[:posizione] +
            password_modificata[posizione].upper() +
            password_modificata[posizione + 1:]
        )
    
    return password_modificata


def aggiungi_caratteri_speciali(password, quanti_speciali=1):
    """
    Sostituisce alcuni caratteri con simboli speciali casuali.
    
    I simboli speciali rendono la password più sicura e difficile da indovinare.
    
    Args:
        password (str): Password da modificare
        quanti_speciali (int): Quanti simboli speciali inserire (default 1)
        
    Returns:
        str: Password con simboli speciali inseriti
        
    Esempio:
        >>> replace_with_special_chars("abc123DEF", 2)
        'a!c123D@F'
    """
    # Lista dei caratteri speciali più comuni e sicuri
    caratteri_speciali = "!@#$%&*?+-="
    password_modificata = password
    
    # Inseriamo simboli speciali in posizioni casuali
    for _ in range(quanti_speciali):
        # Scegliamo una posizione casuale in tutta la password
        posizione = random.randint(0, len(password_modificata) - 1)
        
        # Scegliamo un carattere speciale casuale
        simbolo = random.choice(caratteri_speciali)
        
        # Ricostruiamo la password inserendo il simbolo
        password_modificata = (
            password_modificata[:posizione] +
            simbolo +
            password_modificata[posizione + 1:]
        )
    
    return password_modificata


def genera_password_sicura(lunghezza):
    """
    Genera una password completa con lettere, numeri, maiuscole e simboli.
    
    Args:
        lunghezza (int): Lunghezza desiderata della password
        
    Returns:
        str: Password sicura generata
    """
    # STEP 1: Creiamo una password base solo con lettere minuscole
    password = genera_password_base(lunghezza)
    print(f"  Step 1 - Password base:      {password}")
    
    # STEP 2: Aggiungiamo numeri casuali
    password = aggiungi_numeri(password)
    print(f"  Step 2 - Con numeri:         {password}")
    
    # STEP 3: Aggiungiamo lettere maiuscole
    password = aggiungi_maiuscole(password)
    print(f"  Step 3 - Con maiuscole:      {password}")
    
    # STEP 4: Aggiungiamo caratteri speciali
    password = aggiungi_caratteri_speciali(password)
    print(f"  Step 4 - Finale (+ simboli): {password}")
    
    return password


# =============================================================================
# FUNZIONI PER L'INTERAZIONE CON L'UTENTE
# =============================================================================

def chiedi_numero_intero(messaggio, minimo=1):
    """
    Chiede all'utente un numero intero con validazione.
    
    Args:
        messaggio (str): Domanda da mostrare all'utente
        minimo (int): Valore minimo accettato
        
    Returns:
        int: Numero valido inserito dall'utente
    """
    while True:
        try:
            numero = int(input(messaggio))
            if numero >= minimo:
                return numero
            else:
                print(f"⚠️  Errore: inserisci un numero >= {minimo}")
        except ValueError:
            print("⚠️  Errore: devi inserire un numero!")


def main():
    """
    Funzione principale del programma.
    Gestisce l'interazione con l'utente e coordina le altre funzioni.
    """
    print("=" * 60)
    print("🔐 GENERATORE DI PASSWORD SICURE")
    print("=" * 60)
    print()
    
    # Chiediamo quante password generare
    numero_password = chiedi_numero_intero(
        "Quante password vuoi generare? "
    )
    print()
    
    # Chiediamo la lunghezza di ogni password
    print("📏 Lunghezza minima consigliata: 8 caratteri")
    print("💡 Le password includeranno: lettere, MAIUSCOLE, numeri e !@#$")
    print()
    
    lunghezze = []
    for i in range(numero_password):
        lunghezza = chiedi_numero_intero(
            f"Lunghezza della password #{i + 1}: ",
            minimo=3
        )
        lunghezze.append(lunghezza)
    
    print()
    print("=" * 60)
    print("🔄 GENERAZIONE IN CORSO...")
    print("=" * 60)
    print()
    
    # Generiamo tutte le password
    password_generate = []
    for i, lunghezza in enumerate(lunghezze, start=1):
        print(f"Password #{i} (lunghezza {lunghezza}):")
        password = genera_password_sicura(lunghezza)
        password_generate.append(password)
        print()
    
    # Mostriamo il riepilogo finale
    print("=" * 60)
    print("✅ RIEPILOGO PASSWORD GENERATE")
    print("=" * 60)
    for i, password in enumerate(password_generate, start=1):
        print(f"Password #{i}: {password}")
    
    print()
    print("💡 Suggerimento: copia le password in un posto sicuro!")
    print("🔒 Caratteri speciali usati: !@#$%&*?+-=")
    print()


# =============================================================================
# PUNTO DI INGRESSO DEL PROGRAMMA
# =============================================================================

if __name__ == "__main__":
    # Questo blocco viene eseguito solo se il file viene lanciato direttamente
    # Non viene eseguito se il file viene importato come modulo
    main()
