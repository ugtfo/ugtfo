#include "../inc/free.h"

void free_structs(product_t *arr, int k)
{
	for (int i = 0; i < k; i++)
		free(arr[i].name);
	free(arr);
}

