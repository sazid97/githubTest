package Main;
import NewProject.*;

class Librarian extends User{

    public Librarian(int userid, String name) {
        super(userid, name);
    }
    public void addBook(Library library, Book book){
        library.getBooks().add(book);
        System.out.println("Book Added " + book.getTitle());
    }
    public void removeBook(Library library, Book book){
        if (library.getBooks().remove(book)){
            System.out.println("Book removed: " + book.getTitle());
        }else {
            System.out.println("Book Not found!! ");
        }



    }}
    public class LibraryManagementSystem {
        public static void main(String[] args){
            Library library= new Library();
            Librarian librarian = new Librarian(1, "MOU");
            User user = new User(2, "Sazid");

            Book book1 = new Book(102, "Organization", "Sayed Abul Ala Moududi", true);
            Book book2 = new Book(103, "Methodlogy", "Muna", false);
            Book book3 = new Book(104, "Akhirat", "Sazidul", true);

            librarian.addBook(library, book1);
            librarian.addBook(library, book3);

            library.displayBooks();

            user.borrowBook(book2);
            library.displayBooks();

            user.returnBook(book1);
            library.displayBooks();
        }
    }




