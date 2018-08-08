
class book:
    title = ''
    author = ''
    ISBN = ''
    category = ''
    def __init__(self,strtitle,strauthor,strISBN,strcategory):
        self.title = strtitle
        self.author = strauthor
        self.ISBN = strISBN
        self.category = strcategory
    def d_title(self):
        return self.title
    def d_author(self):
        return self.author
    def d_category(self):
        return self.category

def add_book(library):
    tit = input('\nEnter Title of the Book: ')
    aut = input("Enter Author's Name: ")
    isbn = input('Enter ISBN: ')
    cat = input('Enter Category: ')
    bk = book(tit,aut,isbn,cat)
    library.append(bk)

def display_books(library):
    if len(library) > 0:
        print('\nThe books in the library are\n')
        print('Book Title -- Author -- Category')
        print('==================================')
        for bk in library:
            print(str(bk.d_title())+' -- '+str(bk.d_author())+' -- '+str(bk.d_category()))
        v = input('\nPress any key to continue...')
    else:
        print('\nLibrary is empty. Please try entering book info first')
        v = input('\nPress any key to continue...')
library = []
print('Welcome to the Library Management System')
while True:
    print('\nPress 1. to Enter Book Info')
    print('Press 2. to View Library')
    print('Press 3. to Save')
    print('Press 0. to Quit')
    selection = int(input('\nEnter Selection: '))
    if selection == 1:
        add_book(library)
    elif selection == 2:
        display_books(library)    
    elif selection == 0:
        print('\nThank you for using library management system!')
        break
    else:
        v = input('Invalid Selection. Press any key to continue..')
