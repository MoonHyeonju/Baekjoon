import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int n = scanner.nextInt();
		int tmp = n;
		int count = 0;
		
		while(true) {
			int ten = tmp / 10;
			int one = tmp % 10;
			tmp = one * 10 + (ten + one) % 10;
			count++;
			if(n == tmp) {
				break;
			}
		}
		
		System.out.println(count);
	}
}