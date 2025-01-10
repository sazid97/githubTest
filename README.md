import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        final byte Month_in_Year = 12;
        final byte Percent = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float annualInterestRate = scanner.nextFloat();
        float monthlyInterest = annualInterestRate / Percent / Month_in_Year;


        System.out.print("Period: ");
        byte years = scanner.nextByte();
        int numberOfPayments = years * Month_in_Year;


        double Mortgage = principal * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);
        NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);
        String result = currency.format(Mortgage);

        System.out.println(" Your Mortgage: " + result + "  per month, For " + years + "years ");
}
}
