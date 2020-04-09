// 1003 피보나치 함수
#include <stdio.h>

int cnt[41];

int fibonacci(int n) {
    if (n == 0) {
        cnt[0] = 0;
        return 0;
    } else if (n == 1) {
        cnt[1] = 1;
        return 1;
    } if (cnt[n] != 0) {
        return cnt[n];
    } else {
        return cnt[n] = fibonacci(n-2) + fibonacci(n-1); 
    }
}

int main() {
    int T;
    int* data;
    scanf("%d", &T);
    data = (int*)malloc(sizeof(int) * T);
    for (int i = 0; i < T; i++) {
        scanf("%d", data + i);
    }
    for (int i = 0; i < T; i++) {
        if (data[i] == 0) {
            printf("%d %d\n", 1, 0);
        } else if (data[i] == 1) {
            printf("%d %d\n", 0, 1);
        } else {
            fibonacci(data[i]);
            printf("%d %d\n", cnt[data[i]-1], cnt[data[i]]);
        }
    }
    return 0;
}