#include "../inc/file_work.h"
#include "../inc/free.h"

int main(int argc, char *argv[])
{
	int price_limit;
	int c = 0;
	int k = 0;
	product_t *arr = NULL;
	FILE *f;

	setbuf(stdout, NULL);

	if (argc != 3)
		return NOT_OK;

	f = fopen(argv[1], "r");
	if (f == NULL)
		return NOT_OK;

	if (sscanf(argv[2], "%d", &price_limit) != 1)
		return NOT_OK;

	if (price_limit <= 0)
		return NOT_OK;

	//c = check_args(argc, argv, &f_name, &price_limit);
	//if (c != OK)
		//return NOT_OK;

	c = read_file(f, &arr, &k);
	fclose(f);
	if (c != OK)
	{
		return NOT_OK;
	}

	//print_arr(arr, k);

	c = create_arr_work(arr, &k, price_limit);
	if (c != OK)
	{
		free_structs(arr, k);
		return NOT_OK;
	}

	free_structs(arr, k);

	return OK;
}
