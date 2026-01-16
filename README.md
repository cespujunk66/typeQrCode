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
├── qrgen.html            # Versione web
└── assets/
    └── screenshot.png    # Screenshot dell'app
```

## Librerie Utilizzate

### Desktop
- **pygame** - Framework per interfaccia grafica
- **qrcode** - Generazione QR code
- **Pillow (PIL)** - Manipolazione immagini

### Web
- **QRCode.js** - Generazione QR code JavaScript
- **html2canvas** - Conversione elemento HTML a immagine

## Come Iniziare

### Desktop
```bash
# Clona il repository
git clone https://github.com/tuonome/type-your-qr-code.git
cd type-your-qr-code

# Installa le dipendenze
pip install pygame qrcode[pil]

# Esegui l'app
python qrgen.py
```

### Web
```bash
# Clona il repository
git clone https://github.com/tuonome/type-your-qr-code.git

# Apri il file nel browser
open qrgen.html
```

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

## Browser Supportati (Web)

- Chrome/Chromium (v90+)
- Firefox (v88+)
- Safari (v14+)
- Edge (v90+)

## Mobile

L'app web è completamente responsive e testata su:
- iPhone/iPad
- Android devices
- Tablet

## Licenza

MIT License - vedi LICENSE per dettagli

## Contributi

I contributi sono benvenuti! Per modifiche sostanziali:

1. Fai un fork del repository
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## Autore

Sviluppato come progetto personale - 2026

## Supporto

Per problemi o suggerimenti, apri un issue su GitHub.

## Roadmap

- [ ] Tema scuro (dark mode)
- [ ] Personalizzazione colori QR code
- [ ] Cronologia QR code generati
- [ ] Condivisione direttamente da web
- [ ] Lettura QR code (scanner)
- [ ] Versione mobile app (React Native)
