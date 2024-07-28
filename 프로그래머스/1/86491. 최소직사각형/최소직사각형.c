#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int** sizes, size_t sizes_rows, size_t sizes_cols) {
    int max[2] = {0, 0};
    
    for(int i = 0; i < sizes_rows; i ++) {
        if(sizes[i][1] > sizes[i][0]) {
            int temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
        
        if (sizes[i][0] > max[0]) max[0] = sizes[i][0];
        if (sizes[i][1] > max[1]) max[1] = sizes[i][1];
    }    
    
    return max[0] * max[1];
}