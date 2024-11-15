#include <stdio.h>
int main(){
    int op;
    float x, y;
    printf("Pick an option:\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Divison\n");
    scanf("%d", &op);
    
    switch(op){
        case 1:
        printf("Set two values to effectuate a sum!\n");
        scanf("%f %f", &x, &y);
        if(x == 0 && y == 0){
            printf("The result is zero");
        }
        else{
            printf("The sum of %f and %f is: %f", x, y, x + y);
        }
        break;
        
        case 2:
        printf("Set two values to effectuate a subtraction!\n");
        scanf("%f %f", &x, &y);
        if(x == 0 && y == 0){
            printf("The result is zero");
        }
        else{
            printf("The subtraction of %f and %f is: %f", x, y, x + y);
        }
        break;
        
        case 3:
        printf("Set two values to effectuate a multiplication!\n");
        scanf("%f %f", &x, &y);
        if(x == 0 && y == 0){
             printf("The result is zero");
        }
        else{
            printf("The multiplication of %f and %f is: %f", x, y, x * y);
        }
        break;
        
        case 4:
        printf("Set two values to effectuate a divison!\n");
        scanf("%f %f", &x, &y);
        if(y == 0){
            printf("The result is undefined");
        }
        else{
            printf("The divison of %f and %f is: %f", x, y, x / y);
        }
        break;
    }
}
