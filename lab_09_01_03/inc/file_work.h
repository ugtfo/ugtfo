#define _GNU_SOURCE
#define _POSIX_C_SOURCE 200809L
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifndef FILE_WORK_H
#define FILE_WORK_H

#define OK 0
#define NOT_OK -10
#define LEN 25
#define FILE_END 1

typedef struct
{
	char *name;
	int price;
} product_t;

int read_file(FILE *f, product_t **arr, int *k);
int check_args(int argc, char *argv[], char **f_name, int *limit_price);
int filter_arr(product_t *arr, int *k, int price_limit, product_t **new_arr);
int create_arr_work(product_t *arr, int *k, int price_limit);
void print_arr(product_t *arr, int k);

#endif
