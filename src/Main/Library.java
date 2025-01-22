package Main;

import NewProject.Book;

import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<Book> books;

    public Library(){
        books = new ArrayList<>();
    }
    public List<Book> getBooks(){
        return books;
    }
    public void displayBooks(){
        for (Book book : books){
            System.out.println(book.getTitle() + " By " + book.getAuthor()
            + ((book.isAvailable()) ? "Available " : "Not Available "));
        }
    }
}
