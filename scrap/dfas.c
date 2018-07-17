#include <stdio.h>



int main ()
{
	int i=0, j=0, k=0, num=0, val=0, qt =0;
	
	printf ("DIGITE VALOR A SER SACADO: ");
	scanf ("%d", &num);
	printf ("DIGITE A QUANTIDADE DE NOTAS: ");
	scanf ("%d", &qt);
	
	for (i=0; ((i<num) && (i <= qt)); i++){
		
		for (j=0; ((j<num) && (i+j <= qt)); j++){
		
			for (k=0; ((k<num) && (i+j+k <= qt)); k++){
				
			val=2*k+5*j+10*i;
			
			if (val==num)
				break;
			
		
			}
			if (val==num)
			break;
		}
		if (val==num)
		break;
	}
	
	printf ("A QUANTIDADE DE NOTAS DE 2: %d, de 5: %d e 10: %d", k, j, i);
	
	return 0;
}
