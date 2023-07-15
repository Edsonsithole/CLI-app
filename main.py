def main():
    # initializing book list
     try:   
        bookslist = []
        infile = open("theBookList", "r")
        line = infile.readline()
        while line:
            bookslist.append(line.rstrip("\n").split(","))
            line.infile.readline()
        infile.close

     except FileNotFoundError:
            
            print("Starting a new books list!")
            bookslist = []

     choice = 0
     while choice != 4:
                print("*** Books Manager***")
                print('1- Add a book')
                print('2- Lookup a book')
                print('3- Display books')
                print('4- Quit')
                choice = int(input())

                if choice == 1:
                    print("Adding a book...")
                    nbook = input("Enter the name of the book >>>")
                    nAuthor = input('Enter the name of an Author >>>')
                    nPages = input('Enter the number of pages >>>')
                    bookslist.append([nbook, nAuthor, nPages])
                
                elif choice == 2:
                    print('Looking up for a book...')
                    keyword = input('Enter Search Term: ')
                    for book in bookslist:
                        if keyword in book:
                            print(book)

                elif choice == 3:
                    print('Displaying all Books')
                    for i in range(len(bookslist)):
                        print(bookslist[i])
                
                elif choice == 4:
                    print('Quitting Program')
                print('Program terminated!')
        # Saving to External TXT file
     outfile = open("theBooklist.txt", "w")
     for book in bookslist:
            outfile.write(",".join(book) + "\n")
     outfile.close()

        
if __name__ =="__main__":
    main()