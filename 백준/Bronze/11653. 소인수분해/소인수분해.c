#include <stdio.h>

int main() {
	int a;
	scanf("%d", &a);
	
	for (int i=2;i<=a;i++) {
		while (a % i == 0) {
			printf("%d\n", i);
			a /= i;
		}
	}
	
	return 0;
}