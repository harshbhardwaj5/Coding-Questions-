#include <stdio.h>



int count(int arr[], int bot, int top){
  int flag = 0;
  if(bot==top) return 0;

  else{
    int med = (bot+top)/2;
    if(arr[med]==arr[med+1])
    {
        
        flag = arr[med-1];
        if(flag != arr[med])
            n++;
        
    }
    return n;

    }
    int n = count(arr, bot, med) + count(arr, med+1, top);
    
}
int main(void) {
    // your code goes here
    int a[16] = {1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,5};
    int out = count(a,0,15);
    printf("%d\n",out);
    return 0;
}