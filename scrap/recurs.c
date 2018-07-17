#include <stdio.h>

int solve (int qt2, int qt5, int qt10, int val, int limit){
	int total = qt2*2 + qt5*5 + qt10*10;
	int sum = qt2 + qt5 + qt10;
	
	if (total > val || sum > limit)
	return 0;
	
	if (total == val){
	printf ("%d %d %d", qt2, qt5, qt10);
	return 1;}
	
	if (solve (qt2+1, qt5, qt10, val, limit))
	return 1;
	
	if (solve (qt2, qt5+1, qt10, val, limit))
	return 1;

	if (solve (qt2, qt5, qt10+1, val, limit))
	return 1;
	
	
	return 0;
}

int main ()
{
	int val, limit, i;
	printf ("DIGITE O VALOR EM SEGUIDA A QUANTIDADE: \n");
	scanf ("%d %d", &val, &limit);
	
	for (i=0; i<=limit; i++){
	if (solve (0, 0, 0, val, i))
	
	break;
	
	
	}
	
	
	return 0;
}
