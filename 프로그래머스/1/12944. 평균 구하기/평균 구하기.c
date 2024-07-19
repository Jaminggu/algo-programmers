#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

double solution(int arr[], size_t arr_len) {
    double total = 0;
    
    for(int i = 0; i < arr_len; i ++) total += arr[i];  
    
    return total / arr_len;
}