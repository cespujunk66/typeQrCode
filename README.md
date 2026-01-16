# Type your QR Code!

Un'applicazione per generare QR code in tempo reale, disponibile sia come applicazione desktop con Pygame che come web app.

## Caratteristiche

- ✨ Generazione QR code in tempo reale mentre digiti
- 📱 Interfaccia responsiva (desktop e mobile)
- 💾 Download dei QR code come file PNG
- 🎨 Design moderno stile Google Material Design
- ⚡ Zero dipendenze backend (web app)

## Versioni

### 1. Applicazione Desktop (Pygame)
Un'interfaccia grafica completa con Pygame.

**Requisiti:**
- Python 3.8+
- pygame
- qrcode[pil]

**Installazione:**
```bash
pip install pygame qrcode[pil]
```

**Utilizzo:**
```bash
python qrgen.py
```

**Caratteristiche Desktop:**
- Quadrato QR code 600x600px
- Input testo a riga singola
- Button Download e Esci
- Design con sfondo light grey

### 2. Applicazione Web
Una single-page application HTML/CSS/JavaScript.

**Requisiti:**
- Browser moderno (Chrome, Firefox, Safari, Edge)
- Connessione internet (per le CDN)

**Utilizzo:**
1. Apri `qrgen.html` in un browser
2. Digita il testo per generare il QR code
3. Clicca Download per scaricare l'immagine PNG

**Caratteristiche Web:**
- Interfaccia completamente responsive
- Funziona anche offline (dopo il caricamento)
- Design stile Google Material Design
- Notifiche toast per il feedback

## Struttura del Progetto

```
type-your-qr-code/
├── README.md
├── .gitignore
├── qrgen.py              # Versione desktop con Pygame
└── qrgen.html            # Versione web
```

## Librerie Utilizzate

### Desktop
- **pygame** - Framework per interfaccia grafica
- **qrcode** - Generazione QR code
- **Pillow (PIL)** - Manipolazione immagini

### Web
- **QRCode.js** - Generazione QR code JavaScript
- **html2canvas** - Conversione elemento HTML a immagine


## Utilizzo

### Desktop
1. Digita il testo nel campo di input
2. Il QR code si genera automaticamente nel quadrato
3. Clicca "Download" per salvare il file PNG
4. Clicca "Esci" per chiudere l'applicazione

### Web
1. Digita il testo nel campo di input
2. Il QR code si genera automaticamente
3. Clicca "Download" per scaricare il file PNG
4. L'app è responsive e funziona su mobile

## Personalizzazione

### Colori (Desktop)
Modifica le costanti nel file `qrgen.py`:
```python
LIGHT_ORANGE = (255, 228, 196)
ORANGE = (255, 165, 0)
LIGHT_GRAY = (240, 240, 240)
```

### Colori (Web)
Modifica i colori nel CSS di `qrgen.html`:
```css
background-color: #f8f9fa;  /* Sfondo */
background-color: #1f73db;  /* Button */
```


## Autore

Sviluppato come progetto personale - 2026

## Supporto

Per problemi o suggerimenti, apri un issue su GitHub.

## Roadmap

- [ ] Tema scuro (dark mode)
- [ ] Personalizzazione colori QR code
- [ ] Condivisione direttamente da web
