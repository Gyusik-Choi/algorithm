#include <stdlib.h>

static int find_biggest(const int* arr, const int size)
{
    int biggest = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (biggest < arr[i])
        {
            biggest = arr[i];
        }
    }
    return biggest;
}

int* counting_sort(const int* arr, const int size)
{
    const int max_number = find_biggest(arr, size);
    const int max_arr_length = max_number + 1;
    int* max_arr = malloc(max_arr_length * sizeof(int));
    for (int i = 0; i < size; i++)
    {
        max_arr[i] += arr[i];
    }
    for (int i = 1; i < max_arr_length; i++)
    {
        max_arr[i] += max_arr[i - 1];
    }
    int* answer = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
    {
        max_arr[arr[i]] -= 1;
        answer[max_arr[arr[i]]] = arr[i];
    }
    free(max_arr);
    free(answer);
    return answer;
}

// [1, 1, 2, 5, 5, 5, 3]
// [0, 0, 0, 0, 0, 0]
// [0, 2, 1, 1, 0, 3]
// [0, 2, 3, 4, 4, 7]
// => [1, 1, 2, 3, 5, 5, 5]


