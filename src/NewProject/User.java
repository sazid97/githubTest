package NewProject;

import java.util.ArrayList;
import java.util.List;

public class User{
    int userid;
    String name;
    List <Book> borrowedBook;

    public User(int userid, String name) {
        this.userid = userid;
        this.name = name;
        this.borrowedBook = new ArrayList<>();
    }
    public void borrowBook (Book book){
        if (book.isAvailable){
            borrowedBook.add(book);
            book.setAvailable(false);
            System.out.println(name + "Borrowed" + book.getTitle());
        }else {
            System.out.println(book.getTitle() + " Is not available. ");
        }
    }
     public void returnBook(Book book){
        if (borrowedBook.remove(book)){
            book.setAvailable(true);
            System.out.println(name + " returned " + book.getTitle());
        }else {
            System.out.println("book not found in borrow list");
        }
     }


}