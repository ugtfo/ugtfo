#include "../inc/file_work.h"
#include "../inc/free.h"

int check_args(int argc, char *argv[], char **f_name, int *limit_price)
{
	*f_name = argv[1];

	if (argc != 3)
		return NOT_OK;

	if (sscanf(argv[2], "%d", limit_price) != 1)
		return NOT_OK;

	if (*limit_price <= 0)
		return NOT_OK;

	return OK;
}

//int check_empty(FILE *f)
//{
	//long size;

	////if (fseek(f, 0, SEEK_END) != 0)
		////return NOT_OK;

	//size = ftell(f);
	//if (size <= 0)
		//return NOT_OK;

	//return fseek(f, 0, SEEK_SET);
//}

int read_struct(FILE *f, product_t *arr, int *k, int num)
{
	size_t len = 0;
	char *line = NULL;
	int c = getline(&line, &len, f);

	if (c < 1)
	{
		free(line);
		if (feof(f))
			return FILE_END;
		else
			return NOT_OK;
	}

	arr[*k].name = line;

	c = fscanf(f, "%d\n", &arr[*k].price);

	if (c == 0)
	{
		*k += 1;
		return NOT_OK;
	}
	else if (c == EOF)
		return FILE_END;
	else if (arr[*k].price <= 0)
	{
		*k += 1;
		return NOT_OK;
	}

	*k += 1;

	return OK;
}


int read_file(FILE *f, product_t **arr, int *k)
{
	int c = 0;
	int num;

	//c = check_empty(f);
	//if (c != 0)
		//return NOT_OK;

	if ((fscanf(f, "%d\n", &num) != 1) || (num < 0))
		return NOT_OK;

	product_t *arr_tmp = calloc(num, sizeof(product_t));
	c = 0;

	while (c == 0)
		c = read_struct(f, arr_tmp, k, num);

	//printf("%d ", c);
	if (c == NOT_OK)
	{
		free_structs(arr_tmp, *k);
		return NOT_OK;
	}
	//printf("7");
	else if (num != *k)
	{
		free_structs(arr_tmp, *k);
		return NOT_OK;
	}

	//printf("8");
	*arr = arr_tmp;
	return OK;
}

int copy_struct(product_t *struct1, product_t *struct2)
{
	//if (!strdup(struct1->name))
		//return NOT_OK;

	struct2->name = struct1->name;
	struct2->price = struct1->price;

	return OK;
}

void print_arr(product_t *arr, int k)
{
	for (int i = 0; i < k; i++)
	{
		printf("%s", arr[i].name);
		printf("%d\n", arr[i].price);
	}
}

int create_arr_work(product_t *arr, int *k, int price_limit)
{
	int new_elems = 0;
	int num = 0;

	if (price_limit <= 0)
		return NOT_OK;

	for (int i = 0; i < *k; i++)
		if (price_limit > arr[i].price)
			new_elems++;

	product_t *new_tmp = calloc(new_elems, sizeof(product_t));
	if (!new_tmp)
	{
		free_structs(arr, *k);
		return NOT_OK;
	}

	for (int i = 0; i < *k; i++)
		if (price_limit > arr[i].price)
			if (copy_struct(&arr[i], &new_tmp[num++]) != OK)
				return NOT_OK;

	print_arr(new_tmp, new_elems);
	free_structs(new_tmp, new_elems);

	return OK;
}







