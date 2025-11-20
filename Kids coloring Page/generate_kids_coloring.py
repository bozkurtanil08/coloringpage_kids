# =================================================================================
#    ÇOCUKLAR İÇİN KİTAP ÜRETİCİSİ (Başlıkları Önden Gösteren Versiyon)
# =================================================================================
#
# AÇIKLAMA:
# Bu versiyon, öncelikle belirtilen adette benzersiz kitap başlığı üretir
# ve bunları arayüzde listeler. Ardından listedeki her başlık için
# 100 sayfalık kitap içeriğini oluşturur. Benzersizlik garantilidir.
#
# =================================================================================

import customtkinter
import random
import time
import threading
import queue
import os
import re
from datetime import datetime

print("Çocuklar İçin Kitap Üretici (Başlıkları Önden Gösteren) Başlatılıyor...")

# --- KONFİGÜRASYON ---
BOOKS_DIRECTORY = "Oluşturulan_Kitaplar"
MASTER_LIST_FILE = "tum_kitap_basliklari.txt"
PAGES_PER_BOOK = 100
MIN_WORDS_PER_IDEA = 2
MAX_WORDS_PER_IDEA = 5

# --- YARDIMCI FONKSİYONLAR ---
def sanitize_filename(name):
    name = name.replace(' ', '_')
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name

def load_existing_ideas(filename):
    ideas = set()
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped = line.strip()
                    if stripped:
                        parts = stripped.split(',', 1)
                        if len(parts) > 1:
                            ideas.add(parts[1])
                        else:
                            ideas.add(stripped)
            print(f"'{filename}' dosyasından {len(ideas):,} mevcut kitap başlığı yüklendi.")
        except Exception as e:
            print(f"Mevcut başlıklar yüklenirken hata oluştu: {e}.")
    else:
        print(f"'{filename}' bulunamadı. Yeni dosya oluşturulacak.")
    return ideas

existing_ideas_set = load_existing_ideas(MASTER_LIST_FILE)

# --- FİKİR VE SAYFA ÜRETME MANTIĞI (Değişiklik yok) ---
subjects = ["Puppy", "Kitten", "Bunny", "Teddy Bear", "Dinosaur", "Unicorn", "Dragon", "Lion Cub", "Baby Elephant", "Friendly Monster", "Little Fox", "Happy Bee", "Ladybug", "Butterfly", "Goldfish", "Frog", "Duckling", "Penguin", "Monkey", "Piglet", "Lamb", "Owl", "Turtle", "Bear", "Mouse", "Squirrel", "Giraffe", "Zebra", "Pony", "Mermaid", "Fairy", "Toy Car", "Train", "Airplane", "Boat", "Rocket Ship", "Building Blocks", "Ball", "Doll", "Robot", "Crayon", "Book", "Gift Box", "Balloon", "Kite", "Bucket and Spade", "Swing Set", "Slide", "Bicycle", "Tricycle", "Castle", "House", "Tent", "Drum", "Guitar", "Apple", "Banana", "Cupcake", "Ice Cream Cone", "Donut", "Cookie", "Pizza Slice", "Birthday Cake", "Lollipop", "Sun", "Moon", "Star", "Cloud", "Rainbow", "Flower", "Tree", "Leaf", "Mushroom House", "Mountain", "River", "Beach Ball", "Snowflake", "Raindrop", "Puddle", "Garden", "Letter A", "Number 1", "Circle Shape", "Heart Shape", "Star Shape", "Smiling Boy", "Happy Girl", "Baby", "Astronaut", "Pirate", "Princess", "Knight", "Superhero", "Firefighter", "Doctor", "Teacher", "Chef", "Farmer"]
styles_formats = ["Simple Outline", "Bold Lines", "Cartoon Style", "Cute Style", "Kawaii Style", "Chibi Style", "Doodle Style", "Big Shapes", "Easy to Color", "Learning Page", "Activity Page Style", "With Dotted Lines", "Beginner Level", "Preschool Style", "Toddler Friendly", "Character Pose", "Full Page Scene", "Icon Style", "Sticker Style"]
themes_settings = ["in the Park", "at the Beach", "in the Forest", "on the Farm", "in the Jungle", "under the Sea", "in Outer Space", "in a Castle", "at School", "in the Playground", "at Home", "in the Garden", "in the Sky", "in the Snow", "Playing", "Sleeping", "Eating", "Reading", "Drawing", "Singing", "Dancing", "Birthday Party", "Christmas Time", "Halloween Fun", "Summer Vacation", "Bedtime Story", "Magic Land", "Dinosaur World", "Fairy Garden", "Superhero Mission", "Pirate Adventure"]
descriptors_actions_simple = ["Happy", "Smiling", "Laughing", "Sleepy", "Silly", "Goofy", "Cute", "Little", "Big", "Tiny", "Round", "Fluffy", "Sparkly", "Friendly", "Brave", "Playful", "Waving", "Hugging", "Sitting", "Standing", "Peeking", "Floating", "Flying", "Swimming", "Climbing", "Riding"]
elements_additions_simple = ["with Stars", "with Hearts", "with Bubbles", "with Balloons", "with Flowers", "with Simple Background", "with Dotted Outline", "Thick Lines", "Easy Shapes", "Large Areas", "Name Practice Space", "Word Trace Below", "Funny Face", "Cute Eyes", "Wearing a Hat", "On a Cloud"]

def generate_kids_coloring_idea():
    for _ in range(50):
        # ... (Önceki versiyonla aynı, uzun fonksiyon içeriği)
        idea_words = []
        format_choice = random.randint(1, 17)
        subj = random.choice(subjects)
        style = random.choice(styles_formats)
        theme = random.choice(themes_settings)
        desc = random.choice(descriptors_actions_simple)
        element = random.choice(elements_additions_simple)
        try:
            if format_choice == 1: idea_words = [desc, subj]
            elif format_choice == 2: idea_words = [subj] + style.split()
            elif format_choice == 3: idea_words = [subj] + theme.split()
            elif format_choice == 4: idea_words = theme.split() + [subj]
            elif format_choice == 5: idea_words = [subj] + element.split()
            elif format_choice == 6: idea_words = [desc] + [subj] + style.split()
            elif format_choice == 7: idea_words = [desc, subj]
            elif format_choice == 8: idea_words = style.split() + theme.split()
            elif format_choice == 9: idea_words = [subj] + element.split()
            elif format_choice == 10: idea_words = [desc] + [subj] + theme.split()
            elif format_choice == 11: idea_words = [theme, "Learning", "Page"]
            elif format_choice == 12: idea_words = [subj, "with", desc]
            elif format_choice == 13: idea_words = ["Simple", "Scene", "of", theme]
            elif format_choice == 14: idea_words = style.split() + [subj]
            elif format_choice == 15:
                 if "Letter" in subj or "Number" in subj:
                     assoc_subj = random.choice([s for s in subjects if "Letter" not in s and "Number" not in s])
                     idea_words = [subj, "is", "for", assoc_subj]
                 else: idea_words = [desc, subj]
            elif format_choice == 16: idea_words = ["Set", "of", desc, subj+"s"]
            else:
                 subj2 = random.choice(subjects); idea_words = [subj, "and", subj2] if subj != subj2 else [desc, subj]
        except IndexError: idea_words = ["Kids", "Coloring", "Idea"]
        unique_sequential_words = []
        if idea_words:
            current_word = str(idea_words[0])
            unique_sequential_words.append(current_word)
            for i in range(1, len(idea_words)):
                next_word = str(idea_words[i])
                if next_word.lower() != current_word.lower():
                    unique_sequential_words.append(next_word)
                    current_word = next_word
        final_words = unique_sequential_words[:MAX_WORDS_PER_IDEA]
        word_count = len(final_words)
        if MIN_WORDS_PER_IDEA <= word_count <= MAX_WORDS_PER_IDEA:
            final_string = " ".join(final_words).strip()
            if len(final_string) > 5 and ' ' in final_string:
                 return final_string.title()
    return f"{random.choice(descriptors_actions_simple).title()} {random.choice(subjects).title()}"

def generate_page_idea_for_book(book_title):
    title_keywords = [word for word in book_title.split() if word in subjects]
    main_subject = random.choice(title_keywords) if title_keywords else random.choice(subjects)
    page_format = random.randint(1, 5)
    if page_format == 1: page_idea = f"{main_subject} {random.choice(themes_settings)}"
    elif page_format == 2: page_idea = f"{random.choice(descriptors_actions_simple)} {main_subject}"
    elif page_format == 3: page_idea = f"{main_subject} {random.choice(elements_additions_simple)}"
    elif page_format == 4:
        other_subject = random.choice(subjects)
        if other_subject != main_subject: page_idea = f"{main_subject} and {other_subject}"
        else: page_idea = f"{main_subject} {random.choice(elements_additions_simple)}"
    else: page_idea = f"{main_subject} in a {random.choice(['Simple', 'Cute', 'Cartoon', 'Doodle'])} Style"
    return ' '.join(page_idea.split()).title()

# --- ARKA PLAN ÜRETİM FONKSİYONU (TAMAMEN YENİLENDİ) ---
stop_generation_flag = threading.Event()
def generation_thread_func(q, target_new_books):
    stop_generation_flag.clear()
    start_time = time.time()
    
    # --- AŞAMA 1: Benzersiz Kitap Başlıklarını Önceden Üret ---
    q.put(('status', f"{target_new_books} adet benzersiz kitap başlığı üretiliyor..."))
    titles_to_create = []
    temp_ideas_set = existing_ideas_set.copy() # Mevcut set'i kopyala
    while len(titles_to_create) < target_new_books and not stop_generation_flag.is_set():
        book_title = generate_kids_coloring_idea()
        if book_title not in temp_ideas_set:
            temp_ideas_set.add(book_title)
            titles_to_create.append(book_title)
            q.put(('progress', len(titles_to_create) / target_new_books))

    if stop_generation_flag.is_set():
        q.put(('complete', "İşlem başlangıçta durduruldu."))
        return
        
    # --- AŞAMA 2: Üretilen Başlıkları Arayüzde Göster ve Kitapları Oluştur ---
    q.put(('show_titles', titles_to_create)) # Arayüze listeyi gönder
    os.makedirs(BOOKS_DIRECTORY, exist_ok=True)
    
    with open(MASTER_LIST_FILE, 'a', encoding='utf-8') as master_file:
        for index, book_title in enumerate(titles_to_create):
            if stop_generation_flag.is_set():
                break

            q.put(('status', f"Kitap {index+1}/{target_new_books}: '{book_title}' oluşturuluyor..."))
            
            # Kitap içeriğini oluştur
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            book_filename = sanitize_filename(book_title) + ".txt"
            book_filepath = os.path.join(BOOKS_DIRECTORY, book_filename)
            book_pages = set()
            while len(book_pages) < PAGES_PER_BOOK:
                book_pages.add(generate_page_idea_for_book(book_title))
            
            with open(book_filepath, 'w', encoding='utf-8') as book_file:
                book_file.write(f"--- Kitap Başlığı: {book_title} ---\n")
                book_file.write(f"--- Oluşturulma Tarihi: {timestamp} ---\n")
                book_file.write("-" * 40 + "\n\n")
                for page in sorted(list(book_pages)):
                    book_file.write(page + '\n')
            
            # Kitap bittikten sonra ana listeye ve sete ekle
            master_file.write(f"{timestamp},{book_title}\n")
            master_file.flush()
            existing_ideas_set.add(book_title)
            
            q.put(('progress', (index + 1) / target_new_books))

    # --- Tamamlanma ---
    total_time = time.time() - start_time
    final_message = f"Durduruldu." if stop_generation_flag.is_set() else f"Tamamlandı! Toplam süre: {total_time:.2f}s"
    final_status_full = f"{final_message} Kitaplar '{BOOKS_DIRECTORY}' klasöründe."
    q.put(('complete', final_status_full))

# --- ANA UYGULAMA SINIFI (YENİ METİN KUTUSU EKLENDİ) ---
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Çocuklar İçin Kitap Üretici (Başlıkları Gösteren)")
        self.geometry("800x600") # Arayüzü biraz büyütelim
        customtkinter.set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1) # Metin kutusu için satır ağırlığı
        
        # Üst kontrol paneli
        self.control_frame = customtkinter.CTkFrame(self)
        self.control_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.target_label = customtkinter.CTkLabel(self.control_frame, text="Kaç Yeni Kitap Oluşturulsun?")
        self.target_label.grid(row=0, column=0, padx=10, pady=10)
        self.target_entry = customtkinter.CTkEntry(self.control_frame, placeholder_text="10")
        self.target_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.start_button = customtkinter.CTkButton(self.control_frame, text="Üretimi Başlat", command=self.start_generation)
        self.start_button.grid(row=0, column=2, padx=10, pady=10)
        self.stop_button = customtkinter.CTkButton(self.control_frame, text="Durdur", command=self.stop_generation, state="disabled")
        self.stop_button.grid(row=0, column=3, padx=(0,10), pady=10)

        # Durum ve ilerleme paneli
        self.status_frame = customtkinter.CTkFrame(self)
        self.status_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.status_frame.grid_columnconfigure(0, weight=1)
        self.status_label = customtkinter.CTkLabel(self.status_frame, text="Başlamaya hazır.", anchor="w")
        self.status_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.progressbar = customtkinter.CTkProgressBar(self.status_frame)
        self.progressbar.set(0)
        self.progressbar.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Bilgi ve başlık listesi paneli
        self.list_frame = customtkinter.CTkFrame(self)
        self.list_frame.grid(row=2, column=0, rowspan=2, padx=20, pady=10, sticky="nsew")
        self.list_frame.grid_rowconfigure(1, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)

        self.list_label = customtkinter.CTkLabel(self.list_frame, text="Oluşturulacak Kitap Başlıkları:")
        self.list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        # EKLENDİ: Başlıkları göstermek için metin kutusu
        self.titles_textbox = customtkinter.CTkTextbox(self.list_frame, state="disabled")
        self.titles_textbox.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.total_count_label = customtkinter.CTkLabel(self.list_frame, text=f"Mevcut Kitap Sayısı: {len(existing_ideas_set):,}")
        self.total_count_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.q = queue.Queue()
        self.process_queue()

    def start_generation(self):
        try:
            target_count = int(self.target_entry.get())
            if target_count <= 0: raise ValueError
        except (ValueError, TypeError):
            self.status_label.configure(text="HATA: Lütfen pozitif bir sayı girin.")
            return
            
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.progressbar.set(0)
        self.titles_textbox.configure(state="normal")
        self.titles_textbox.delete("1.0", "end")
        self.titles_textbox.configure(state="disabled")
        
        threading.Thread(target=generation_thread_func, args=(self.q, target_count), daemon=True).start()

    def stop_generation(self):
        self.status_label.configure(text="Durduruluyor...")
        stop_generation_flag.set()
        self.stop_button.configure(state="disabled")

    def process_queue(self):
        try:
            message = self.q.get_nowait()
            msg_type = message[0]
            if msg_type == 'status':
                self.status_label.configure(text=message[1])
            elif msg_type == 'progress':
                self.progressbar.set(message[1])
            elif msg_type == 'show_titles': # DÜZENLENDİ: Yeni mesaj tipi
                self.titles_textbox.configure(state="normal")
                self.titles_textbox.delete("1.0", "end")
                for title in message[1]:
                    self.titles_textbox.insert("end", title + "\n")
                self.titles_textbox.configure(state="disabled")
            elif msg_type == 'complete':
                self.status_label.configure(text=message[1])
                self.start_button.configure(state="normal")
                self.stop_button.configure(state="disabled")
                self.total_count_label.configure(text=f"Mevcut Kitap Sayısı: {len(existing_ideas_set):,}")
        except queue.Empty:
            pass
        finally:
            self.after(100, self.process_queue)

if __name__ == "__main__":
    app = App()
    app.mainloop()
