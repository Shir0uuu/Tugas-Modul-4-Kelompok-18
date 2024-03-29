class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print("Buku yang tersedia:")
        for book in self.available_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print(f"Anda telah meminjam {requested_book}")
            self.available_books.remove(requested_book)
        else:
            print("Maaf, buku tersebut tidak tersedia di perpustakaan.")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print("Anda telah mengembalikan buku. Terima kasih!")

def main():
    library = Library(["Buku 1", "Buku 2", "Buku 3"])
    while True:
        print("\nSelamat datang di perpustakaan!")
        print("1. Tampilkan buku yang tersedia")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Keluar")
        user_choice = int(input("Masukkan pilihan Anda: "))
        if user_choice == 1:
            library.display_available_books()
        elif user_choice == 2:
            requested_book = input("Masukkan nama buku yang ingin Anda pinjam: ")
            library.lend_book(requested_book)
        elif user_choice == 3:
            returned_book = input("Masukkan nama buku yang ingin Anda kembalikan: ")
            library.add_book(returned_book)
        elif user_choice == 4:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
    #apalah
