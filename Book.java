import java.util.ArrayList;
import java.util.List;

public class Book {
    private String Title;
    private String Author;
    private int ISBN;

    public Book(String title, String author, int isbn){
        this.Title = title;
        this.Author = author;
        this.ISBN = isbn;
    }

    public String getTitle() {
        return Title;
    }

    public void setTitle(String title) {
        Title = title;
    }

    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String author) {
        Author = author;
    }

    public int getISBN() {
        return ISBN;
    }

    public void setISBN(int ISBN) {
        this.ISBN = ISBN;
    }
}
class BookCollection{
    private List<Book>Books;

    public BookCollection(){
        Books = new ArrayList<>();
    }
    //Add

    public void addBook(String title, String author, int isbn){
        Book book = new Book(title, author, isbn);
        Books.add(book);
        System.out.println("Book added: " + book.getTitle());
    }
    //Remove
    public void removeBookByIsbn(int ISBN){
        Books.removeIf(book -> book.getISBN() == ISBN);
        System.out.println("Book with " + ISBN + " removed");
    }

    public void listBooks(){
        if (Books.isEmpty()){
            System.out.println("No Books in hte collection");
        }else {
            for (Book book: Books){
                System.out.println(book.getTitle());
            }
        }
    }

}