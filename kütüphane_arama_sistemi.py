# ===== RENK KODLARI =====
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"


# ===== Kitap Sınıfı =====
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"{CYAN}Kitap Adı:{RESET} {self.name}, {CYAN}Yazar:{RESET} {self.author}, {CYAN}Yayın Yılı:{RESET} {self.year}"


# ===== Kütüphane Sınıfı =====
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, year):
        self.books.append(Book(name, author, year))
        print(f"{GREEN}>> {name} başarıyla eklendi.{RESET}")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print(f"{GREEN}>> {name} başarıyla silindi.{RESET}")
                return
        print(f"{RED}>> Kitap bulunamadı.{RESET}")

    def search_by_name(self, name):
        print(f"{YELLOW}>> Arama Sonuçları:{RESET}")
        found = False
        for book in self.books:
            if name.lower() in book.name.lower():
                print(f">> {book}")
                found = True
        if not found:
            print(f"{RED}>> Kitap bulunamadı.{RESET}")

    def search_by_author(self, author):
        print(f"{YELLOW}>> Arama Sonuçları:{RESET}")
        found = False
        for book in self.books:
            if author.lower() in book.author.lower():
                print(f">> {book}")
                found = True
        if not found:
            print(f"{RED}>> Yazara ait kitap bulunamadı.{RESET}")

    def list_books(self):
        print(f"{BLUE}>> Kütüphanedeki Kitaplar:{RESET}")
        if not self.books:
            print(f"{RED}>> Kütüphanede kitap yok.{RESET}")
        else:
            for book in self.books:
                print(f">> {book}")


# ===== Ana Menü =====
def menu():
    library = Library()

    while True:
        print(f"""
{BOLD}{BLUE}KÜTÜPHANE KİTAP ARAMA SİSTEMİ{RESET}
{CYAN}>> 1.{RESET} Kitap Ekle
{CYAN}>> 2.{RESET} Kitap Sil
{CYAN}>> 3.{RESET} Kitap Ara (İsme Göre)
{CYAN}>> 4.{RESET} Kitap Ara (Yazara Göre)
{CYAN}>> 5.{RESET} Tüm Kitapları Listele
{CYAN}>> 6.{RESET} Çıkış
""")

        choice = input(f"{YELLOW}>> Seçiminizi yapın (1-6): {RESET}")

        if choice == "1":
            name = input(">> Kitap Adı: ")
            author = input(">> Yazar: ")
            year = input(">> Yayın Yılı: ")
            library.add_book(name, author, year)

        elif choice == "2":
            name = input(">> Silinecek Kitap Adı: ")
            library.remove_book(name)

        elif choice == "3":
            name = input(">> Aramak istediğiniz kitabın adını girin: ")
            library.search_by_name(name)

        elif choice == "4":
            author = input(">> Aramak istediğiniz yazar adını girin: ")
            library.search_by_author(author)

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            print(f"{GREEN}>> Programdan çıkılıyor...{RESET}")
            break

        else:
            print(f"{RED}>> Hatalı seçim!{RESET}")


# ===== Programı Başlat =====
menu()
