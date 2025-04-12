class library:
   def __init_(self, name):
      
      self.name = name
      self.books = [ ]

      def add_book(self, book_name) :
         
         self.books.append(book_name)
         print('📖"{book_name)" added to the library')

         def show_bOOks (self) :

            if self.books:
               print(f"\n books available in {self.name}:")
               for book in self.books:
                  print(f"- {book}")
               else:
                  print( "No books in the library!" )

                 if book_name in self.books:
                  self.books.remove(book_name)
                  print(f' sorry, "{book_name}" is not available')
                
                # Create a library object
                my_library = Library("Kids'Library")

               # Add books 
            my_library.addbook ("HArry Potter")
            my_library. ("Harry potter")
            my _ library. ("Alice in Wonderland")
            my_library. ("Charlie and the Chocolate Factory") 

    # Show available books
    my_library.show_books()                   
    
                     