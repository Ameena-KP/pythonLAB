#include<stdio.h>
#define MAX 100
int parent[MAX];
void makeset(int n){
for (int i=0;i<n;i++){
parent [i]=i;
}
}
int find(int x){
if (parent[x]==x)
return x;
else
return find (parent[x]);
}
void unionset(int x,int y)
{
int px=find(x);
int py=find(y);
if (px != py){
parent[py]=px;
printf("union done between %d and %d \n",x,y);
}
else{
printf("%d and %d already in the sumset \n",x,y);
}
}
int main(){
int n,choice,x,y;
printf("enter number of elements: ");
scanf("%d",&n);
makeset(n);
do{
printf("\n ---Disjoint Set Menu--- \n");
printf("1.union \n");
printf("2.find \n");
printf("3.display parent array \n");
printf("4. exit \n");
printf("enter your choice");
scanf("%d",&choice);
switch(choice){
case 1:
printf("enter two elements to union:");
scanf("%d %d",&x,&y);
unionset (x,y);
break;

case 2:
printf("enter elements to find parent:");
scanf("%d",&x);
printf("parent of  %d is %d \n",x,
                find(x));
break;

case 3:
printf("parent array:\n");
for (int i=0;i<n;i++)
printf("parent [%d]=%d \n",i,parent[i]);
break;

case 4:
printf("exiting...\n");
break;
default:printf("invalid choice \n");
}
}
while (choice !=4);
return 0;
}

~              
