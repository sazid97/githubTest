import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        byte Percent = 100;
        byte Month_in_Year = 12;

        int principal = 0;
        float annualInterestRate = 0;
        byte years = 0;


        while (true){
            System.out.print("Principal($1K - $1M): ");
            principal = scanner.nextInt();
            if (principal >= 1000 && principal <= 1_00_000)
                break;
            System.out.println("please enter amount between 1000 and 1,000,000.");

        }

        while (true) {System.out.print("Annual Interest Rate: ");
        annualInterestRate = scanner.nextFloat();
        if (annualInterestRate >= 1 && annualInterestRate <= 30)
            break;
        System.out.println("enter value greater than 0 and less than or equal to 30");
        }

        float monthlyInterest = annualInterestRate / Percent / Month_in_Year;


        while (true) {
            System.out.print("Period: ");
            years = scanner.nextByte();
            if (years >= 1 && years <= 30)
                break;
            System.out.println("Should be more than 1");
        }
        int numberOfPayments = years * Month_in_Year;


        double Mortgage = principal * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);
        String result = currency.format(Mortgage);

        System.out.println(" Your Mortgage: " + result + "  per month, For " + years + "years ");
    }
}
