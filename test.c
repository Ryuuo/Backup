#include <stdio.h>
#include <time.h>
int combination(int n, int r){
    if(n==r || r==0){
        return 1;
    }
    else if(r==1){
        return n;
    }
    else{
        return combination(n-1,r)+combination(n-1,r-1);
    }
}

int main(void){
        int n = 56;
        int r = 10;
        clock_t start,end;
        start = clock();
        time_t t = time(NULL);
        int com = combination(n,r);
        end = clock();
        printf("n=%d\n\rr=%d\n\rcombination=%d\n\rstart=%sexecution time=%.2f\n\r\a\a\a",n,r,com,ctime(&t),(double)(end-start)/CLOCKS_PER_SEC);
        return 0;
}
