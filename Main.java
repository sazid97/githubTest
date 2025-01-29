import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the book name: ");
        String bookName = sc.next();

        System.out.print("Enter the author name: ");
        String authorName = sc.next();

        System.out.print("Enter the ISBN: ");
        int newIsbn = sc.nextInt();

    BookCollection myCollection = new BookCollection();

    myCollection.addBook(bookName, authorName, newIsbn);
    myCollection.listBooks();
    myCollection.removeBookByIsbn(2018);
        System.out.println("After removal");
        myCollection.listBooks();
    }
}