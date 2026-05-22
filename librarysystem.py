import json
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Dict, List

DATA_DIR = Path(__file__).resolve().parent
BOOKS_FILE = DATA_DIR / 'books.json'
MEMBERS_FILE = DATA_DIR / 'members.json'

@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    category: str
    copies_total: int
    copies_available: int

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        return Book(**data)

@dataclass
class Member:
    id: int
    name: str
    email: str
    borrowed_books: List[int] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> 'Member':
        return Member(**data)

class Library:
    def __init__(self) -> None:
        self.books: Dict[int, Book] = self._load_books()
        self.members: Dict[int, Member] = self._load_members()

    def _load_books(self) -> Dict[int, Book]:
        if BOOKS_FILE.exists():
            with BOOKS_FILE.open('r', encoding='utf-8') as handle:
                data = json.load(handle)
            return {int(key): Book.from_dict(value) for key, value in data.items()}
        return {}

    def _load_members(self) -> Dict[int, Member]:
        if MEMBERS_FILE.exists():
            with MEMBERS_FILE.open('r', encoding='utf-8') as handle:
                data = json.load(handle)
            return {int(key): Member.from_dict(value) for key, value in data.items()}
        return {}

    def _save_books(self) -> None:
        with BOOKS_FILE.open('w', encoding='utf-8') as handle:
            json.dump({book_id: book.to_dict() for book_id, book in self.books.items()}, handle, indent=2)

    def _save_members(self) -> None:
        with MEMBERS_FILE.open('w', encoding='utf-8') as handle:
            json.dump({member_id: member.to_dict() for member_id, member in self.members.items()}, handle, indent=2)

    def _save_all(self) -> None:
        BOOKS_FILE.parent.mkdir(parents=True, exist_ok=True)
        self._save_books()
        self._save_members()

    def _next_book_id(self) -> int:
        return max(self.books.keys(), default=0) + 1

    def _next_member_id(self) -> int:
        return max(self.members.keys(), default=0) + 1

    def add_book(self, title: str, author: str, isbn: str, category: str, copies: int) -> Book:
        book_id = self._next_book_id()
        book = Book(id=book_id, title=title.strip(), author=author.strip(), isbn=isbn.strip(), category=category.strip(), copies_total=copies, copies_available=copies)
        self.books[book_id] = book
        self._save_books()
        return book

    def add_member(self, name: str, email: str) -> Member:
        member_id = self._next_member_id()
        member = Member(id=member_id, name=name.strip(), email=email.strip())
        self.members[member_id] = member
        self._save_members()
        return member

    def search_books(self, query: str) -> List[Book]:
        query_text = query.strip().lower()
        return [book for book in self.books.values() if query_text in book.title.lower() or query_text in book.author.lower() or query_text in book.isbn.lower() or query_text in book.category.lower()]

    def borrow_book(self, member_id: int, book_id: int) -> str:
        if member_id not in self.members:
            return 'Member not found.'
        if book_id not in self.books:
            return 'Book not found.'

        member = self.members[member_id]
        book = self.books[book_id]

        if book.copies_available <= 0:
            return f'"{book.title}" is currently not available.'
        if book_id in member.borrowed_books:
            return f'Member already borrowed "{book.title}".'

        book.copies_available -= 1
        member.borrowed_books.append(book_id)
        self._save_all()
        return f'"{book.title}" has been borrowed by {member.name}. '

    def return_book(self, member_id: int, book_id: int) -> str:
        if member_id not in self.members:
            return 'Member not found.'
        if book_id not in self.books:
            return 'Book not found.'

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed_books:
            return f'{member.name} does not have "{book.title}" borrowed.'

        book.copies_available += 1
        member.borrowed_books.remove(book_id)
        self._save_all()
        return f'"{book.title}" has been returned by {member.name}. '

    def list_books(self) -> List[Book]:
        return sorted(self.books.values(), key=lambda item: item.id)

    def list_members(self) -> List[Member]:
        return sorted(self.members.values(), key=lambda item: item.id)

    def book_summary(self) -> str:
        lines = ['ID | Title | Author | ISBN | Category | Available/Total']
        for book in self.list_books():
            lines.append(f'{book.id} | {book.title} | {book.author} | {book.isbn} | {book.category} | {book.copies_available}/{book.copies_total}')
        return '\n'.join(lines)

    def member_summary(self) -> str:
        lines = ['ID | Name | Email | Borrowed IDs']
        for member in self.list_members():
            lines.append(f'{member.id} | {member.name} | {member.email} | {member.borrowed_books}')
        return '\n'.join(lines)


def prompt_int(prompt_text: str, minimum: int = 1) -> int:
    while True:
        value = input(prompt_text).strip()
        if value.isdigit() and int(value) >= minimum:
            return int(value)
        print(f'Please enter a whole number >= {minimum}.')


def main() -> None:
    library = Library()
    actions = {
        '1': 'Add a new book',
        '2': 'Register a new member',
        '3': 'Search for books',
        '4': 'Borrow a book',
        '5': 'Return a book',
        '6': 'List all books',
        '7': 'List all members',
        '0': 'Exit'
    }

    while True:
        print('\n=== Library System ===')
        for key, desc in actions.items():
            print(f'{key}. {desc}')
        choice = input('Choose an option: ').strip()

        if choice == '1':
            title = input('Book title: ').strip()
            author = input('Author name: ').strip()
            isbn = input('ISBN: ').strip()
            category = input('Category: ').strip()
            copies = prompt_int('Number of copies: ', minimum=1)
            book = library.add_book(title, author, isbn, category, copies)
            print(f'Book added: {book.id} - {book.title}')

        elif choice == '2':
            name = input('Member name: ').strip()
            email = input('Member email: ').strip()
            member = library.add_member(name, email)
            print(f'Member registered: {member.id} - {member.name}')

        elif choice == '3':
            query = input('Search by title, author, ISBN, or category: ').strip()
            matches = library.search_books(query)
            if not matches:
                print('No book records matched your search.')
            else:
                for book in matches:
                    print(f'{book.id}: {book.title} by {book.author} ({book.copies_available}/{book.copies_total} available)')

        elif choice == '4':
            member_id = prompt_int('Member ID: ')
            book_id = prompt_int('Book ID: ')
            print(library.borrow_book(member_id, book_id))

        elif choice == '5':
            member_id = prompt_int('Member ID: ')
            book_id = prompt_int('Book ID: ')
            print(library.return_book(member_id, book_id))

        elif choice == '6':
            print(library.book_summary())

        elif choice == '7':
            print(library.member_summary())

        elif choice == '0':
            print('Saving changes and exiting. Goodbye!')
            break

        else:
            print('Invalid option, please try again.')

if __name__ == '__main__':
    main()
