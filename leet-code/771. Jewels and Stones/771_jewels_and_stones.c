#include <string.h>

int numJewelsInStones(char* jewels, char* stones) {
    int count['z' + 1] = {0};
    const int j_length = (int)strlen(jewels);
    for (int i = 0; i < j_length; i++) {
        count[(unsigned char)jewels[i]]++;
    }
    int result = 0;
    const int s_length = (int)strlen(stones);
    for (int i = 0; i < s_length; i++) {
        if (count[(unsigned char)stones[i]] > 0) {
            result++;
        }
    }
    return result;
}
