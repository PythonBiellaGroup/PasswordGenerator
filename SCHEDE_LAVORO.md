### **Scheda di lavoro 1: Aggiungere un'Opzione per Personalizzare i Caratteri da Includere**

**Obiettivo**: Aggiungere un'opzione che consenta all'utente di scegliere i caratteri da includere nella password (numeri, maiuscole, simboli speciali).

---

#### **Descrizione del compito**
Modifica il programma in modo che l'utente possa scegliere se includere numeri, lettere maiuscole e simboli speciali. Crea una funzione che permette all'utente di definire quale tipo di caratteri vuole nella password.

#### **Passaggi per completare il compito**

1. **Modifica la funzione principale**: Aggiungi un menu in cui l'utente può selezionare quali tipi di caratteri includere nella password.
   
2. **Modifica la funzione `genera_password_sicura`** per accettare i parametri di personalizzazione (numeri, maiuscole, simboli).
   
3. **Test della funzione**: Verifica che la password venga generata correttamente in base alle scelte dell'utente.

---

#### **Codice di esempio per iniziare**:
```python
def genera_password_sicura_custom(lunghezza, includi_numeri, includi_maiuscole, includi_speciali):
    password = genera_password_base(lunghezza)
    
    if includi_numeri:
        password = aggiungi_numeri(password)
    
    if includi_maiuscole:
        password = aggiungi_maiuscole(password)
    
    if includi_speciali:
        password = aggiungi_caratteri_speciali(password)
    
    return password
```

---

### **Scheda di lavoro 2: Aggiungere una Funzione per Controllare la Sicurezza della Password**

**Obiettivo**: Creare una funzione che valuta la sicurezza di una password basata su vari criteri (lunghezza, presenza di maiuscole, numeri e simboli speciali).

---

#### **Descrizione del compito**
Devi implementare una funzione che valuta la sicurezza di una password. La funzione deve controllare:

- La **lunghezza** della password (minimo 8 caratteri).
- La presenza di almeno **una lettera maiuscola**.
- La presenza di almeno **un numero**.
- La presenza di almeno **un simbolo speciale**.

La funzione dovrà restituire un punteggio da 1 a 5, dove 1 significa password debole e 5 significa password molto sicura.

---

#### **Passaggi per completare il compito**

1. **Analisi della password**:
   - Controlla la lunghezza della password.
   - Verifica se ci sono lettere maiuscole, numeri e simboli speciali.
   
2. **Restituzione del punteggio**:
   - Assegna il punteggio in base ai criteri sopra descritti.
   
3. **Test della funzione**:
   - Testa la tua funzione con password di esempio, come `"abc123"`, `"Abc123!"`, e `"A1b2C3#@"`.

---

#### **Codice di esempio per iniziare**:
```python
def valuta_sicurezza_password(password):
    punteggio = 0
    
    # Controlla la lunghezza
    if len(password) >= 8:
        punteggio += 1
    
    # Controlla se ci sono lettere maiuscole
    if any(c.isupper() for c in password):
        punteggio += 1
    
    # Controlla se ci sono numeri
    if any(c.isdigit() for c in password):
        punteggio += 1
    
    # Controlla se ci sono simboli speciali
    simboli_speciali = "!@#$%&*?+-="
    if any(c in simboli_speciali for c in password):
        punteggio += 1
    
    return punteggio
```

---

### **Scheda di lavoro 3: Espandere la Lista di Caratteri Speciali**

**Obiettivo**: Aggiungere nuovi caratteri speciali alla lista predefinita per aumentare la varietà dei simboli usati nelle password.

---

#### **Descrizione del compito**
Modifica la lista dei caratteri speciali per includere simboli aggiuntivi (ad esempio, `[{]}()^~_`). Implementa una funzione che permetta all'utente di scegliere se utilizzare una lista personalizzata di simboli speciali.

#### **Passaggi per completare il compito**

1. **Modifica la lista di simboli speciali**: Aggiungi simboli come parentesi quadre, parentesi tonde, e altri caratteri.
   
2. **Personalizzazione simboli**: Permetti all'utente di personalizzare la lista di simboli speciali, magari chiedendo un input tramite terminale o un file di configurazione.
   
3. **Test della funzione**: Prova a generare delle password con simboli speciali nuovi.

---

#### **Codice di esempio per iniziare**:
```python
def aggiungi_caratteri_speciali(password, quanti_speciali=1, simboli_personalizzati=None):
    if simboli_personalizzati is None:
        simboli_personalizzati = "!@#$%&*?+-="
    
    password_modificata = password
    
    for _ in range(quanti_speciali):
        posizione = random.randint(0, len(password_modificata) - 1)
        simbolo = random.choice(simboli_personalizzati)
        password_modificata = (
            password_modificata[:posizione] +
            simbolo +
            password_modificata[posizione + 1:]
        )
    
    return password_modificata
```

---

### **Scheda di lavoro 4: Salvare le Password Generate in un File**

**Obiettivo**: Aggiungere la funzionalità di salvataggio delle password generate in un file di testo o JSON.

---

#### **Descrizione del compito**
Crea una funzione che permetta di **salvare le password generate** in un file di testo o JSON, in modo che l'utente possa consultarle successivamente.

#### **Passaggi per completare il compito**

1. **Modifica la funzione principale**: Aggiungi un'opzione per salvare le password generate.
   
2. **Scrivi le password in un file**: Scegli un formato di salvataggio, ad esempio un file `.txt` o un file `.json`, e salva tutte le password generate in quel file.
   
3. **Test della funzione**: Verifica che le password vengano effettivamente salvate e che possano essere lette dal file.

---

#### **Codice di esempio per iniziare**:
```python
import json

def salva_passwords(passwords, filename="passwords.json"):
    with open(filename, 'w') as f:
        json.dump(passwords, f)

# Uso:
passwords = ["abc123", "Def!567", "P@ssw0rd"]
salva_passwords(passwords)
```