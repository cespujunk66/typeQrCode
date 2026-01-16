import pygame
import qrcode
from PIL import Image
import sys
from datetime import datetime

# Inizializzazione Pygame
pygame.init()

# Costanti
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
QR_SIZE = 600
TEXTAREA_WIDTH = 600
TEXTAREA_HEIGHT = 40
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 40
BUTTON_SIZE = 50

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (100, 100, 100)
LIGHT_ORANGE = (255, 228, 196)
ORANGE = (255, 165, 0)
ORANGE_HOVER = (255, 140, 0)
BLUE = (0, 120, 215)
BLUE_HOVER = (0, 100, 180)
RED = (255, 0, 0)

class TextArea:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.cursor_pos = 0
        self.cursor_visible = True
        self.cursor_timer = 0
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.cursor_pos > 0:
                    self.text = self.text[:self.cursor_pos-1] + self.text[self.cursor_pos:]
                    self.cursor_pos -= 1
            elif event.key == pygame.K_DELETE:
                self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos+1:]
            elif event.key == pygame.K_LEFT:
                self.cursor_pos = max(0, self.cursor_pos - 1)
            elif event.key == pygame.K_RIGHT:
                self.cursor_pos = min(len(self.text), self.cursor_pos + 1)
            elif event.key == pygame.K_HOME:
                self.cursor_pos = 0
            elif event.key == pygame.K_END:
                self.cursor_pos = len(self.text)
            else:
                # Gestisci caratteri stampabili
                if event.unicode and event.unicode.isprintable():
                    self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                    self.cursor_pos += 1
    
    def draw(self, surface, font):
        # Sfondo
        pygame.draw.rect(surface, LIGHT_GRAY, self.rect)
        pygame.draw.rect(surface, DARK_GRAY, self.rect, 2)
        
        # Testo
        if self.text:
            text_surface = font.render(self.text, True, BLACK)
            surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 8))
        
        # Cursore
        if self.active:
            self.cursor_timer += 1
            if self.cursor_timer % 30 < 15:
                cursor_x = self.rect.x + 5 + self.cursor_pos * 16
                cursor_y = self.rect.y + 5
                pygame.draw.line(surface, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 25), 2)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.is_hovered = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        return False
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False
    
    def draw(self, surface, font):
        # Colore del bottone (più scuro se hover)
        color = ORANGE_HOVER if self.is_hovered else ORANGE
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # Testo
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

def generate_qr_code(text):
    """Genera un QR code a partire dal testo"""
    if not text or text.strip() == "":
        return None
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        # Ridimensiona a 600x600
        img = img.resize((QR_SIZE, QR_SIZE), Image.Resampling.LANCZOS)
        
        return img
    except Exception as e:
        print(f"Errore nella generazione del QR code: {e}")
        return None

def pil_to_pygame(pil_image):
    """Converte un'immagine PIL a una superficie Pygame"""
    if pil_image is None:
        return None
    
    try:
        # Assicurati che l'immagine sia in RGB
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        # Usa pygame.image.fromstring con il modo corretto
        return pygame.image.fromstring(
            pil_image.tobytes(),
            pil_image.size,
            'RGB'
        )
    except Exception as e:
        print(f"Errore nella conversione immagine: {e}")
        return None

def save_qr_code(qr_image, text):
    """Salva il QR code in un file PNG"""
    if qr_image is None:
        return False
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"TypeMyQr_{timestamp}.png"
        qr_image.save(filename)
        print(f"QR code salvato come: {filename}")
        return True
    except Exception as e:
        print(f"Errore nel salvataggio: {e}")
        return False

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Type your QR Code!")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)
    font_button = pygame.font.Font(None, 18)
    
    # Componenti UI
    textarea = TextArea(
        x=(SCREEN_WIDTH - TEXTAREA_WIDTH) // 2,
        y=QR_SIZE + 50,
        width=TEXTAREA_WIDTH,
        height=TEXTAREA_HEIGHT
    )
    
    # Button allineati orizzontalmente
    button_y = textarea.rect.y + textarea.rect.height + 20
    button_spacing = 20
    total_button_width = BUTTON_WIDTH * 2 + button_spacing
    button_start_x = (SCREEN_WIDTH - total_button_width) // 2
    
    btn_salva = Button(button_start_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, "Salva")
    btn_esci = Button(button_start_x + BUTTON_WIDTH + button_spacing, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, "Esci")
    
    # Variabili di stato
    current_qr = None
    current_text = ""
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Gestione textarea
            textarea.handle_event(event)
            
            # Gestione button
            btn_salva.handle_event(event)
            btn_esci.handle_event(event)
            
            # Click sui button
            if btn_esci.is_clicked(event):
                running = False
            elif btn_salva.is_clicked(event):
                if current_qr:
                    save_qr_code(current_qr, current_text)
        
        # Genera QR code se il testo è cambiato
        if textarea.text != current_text:
            current_text = textarea.text
            current_qr = generate_qr_code(current_text)
        
        # Rendering
        screen.fill(LIGHT_ORANGE)
        
        # Disegna quadrato per QR code
        qr_rect = pygame.Rect(
            (SCREEN_WIDTH - QR_SIZE) // 2,
            30,
            QR_SIZE,
            QR_SIZE
        )
        pygame.draw.rect(screen, LIGHT_GRAY, qr_rect)
        pygame.draw.rect(screen, DARK_GRAY, qr_rect, 2)
        
        # Disegna QR code
        if current_qr:
            qr_surface = pil_to_pygame(current_qr)
            if qr_surface:
                screen.blit(qr_surface, qr_rect)
        
        # Disegna textarea e button
        textarea.draw(screen, font)
        btn_salva.draw(screen, font_button)
        btn_esci.draw(screen, font_button)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()