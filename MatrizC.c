#include <stdio.h>

int main(){
  int n,x,y;
    scanf("%d %d %d",&n,&x,&y);
  int a = x*y;
  int soma=0, ma[x][y],i=1,cont=1;
    while(i<=a){
      soma+=i;
      i++;
    printf("%d ",soma);
    }
  if(soma != n){
    printf("-1");
  }else{
    for(int e=0;e<x;e++){ // e = 0 ; caso e menor do que x ; e + 1 
      for(int f=0;f<y;f++){
        ma[e][f] = cont;
        cont++; 
        printf("posicao %d",ma[e][f]);
      }
    }
  } // 3
return 0;
}