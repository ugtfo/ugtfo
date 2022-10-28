#include "../inc/check_main.h"

START_TEST(test_ok_read)
{
	FILE *f = fopen("./func_tests/pos_01_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	read_file(f, &arr, &n);

	product_t arr_res[3];

	arr_res[0].name = "a";
	arr_res[1].name = "b";
	arr_res[2].name = "c";

	arr_res[0].price = 1;
	arr_res[1].price = 2;
	arr_res[2].price = 3;

	int c = compare_arrs(arr, n, arr_res, 4);

	ck_assert_int_eq(c, OK);

	free_structs(arr, n);
}
END_TEST

START_TEST(test_read_clear_file)
{
	FILE *f = fopen("./func_tests/neg_01_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);
}
END_TEST

START_TEST(test_read_wrong_name)
{
	FILE *f = fopen("./func_tests/neg_02_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);
}
END_TEST

START_TEST(test_read_wrong_price)
{
	FILE *f = fopen("./func_tests/neg_03_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);
}
END_TEST

START_TEST(test_read_negative_price)
{
	FILE *f = fopen("./func_tests/neg_04_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);
}
END_TEST

START_TEST(test_read_wrong_elems_num)
{
	FILE *f = fopen("./func_tests/neg_05_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);

	free_structs(arr, n);
}
END_TEST

START_TEST(test_read_elems_num_different)
{
	FILE *f = fopen("./func_tests/neg_06_in.txt", "r");

	product_t *arr = NULL;
	int n = 0;
    
	int c = read_file(f, &arr, &n);

	ck_assert_int_eq(c, NOT_OK);
}
END_TEST

Suite *read_suite(Suite *s)
{
	TCase *tc_pos;
	TCase *tc_neg;

	tc_pos = tcase_create("positives");

	tcase_add_test(tc_pos, test_ok_read);

	suite_add_tcase(s, tc_pos);

	tc_neg = tcase_create("negatives");

	tcase_add_test(tc_neg, test_read_clear_file);
	tcase_add_test(tc_neg, test_read_wrong_name);
	tcase_add_test(tc_neg, test_read_wrong_price);
	tcase_add_test(tc_neg, test_read_negative_price);
	tcase_add_test(tc_neg, test_read_wrong_elems_num);
	tcase_add_test(tc_neg, test_read_elems_num_different);

	suite_add_tcase(s, tc_neg);

	return s;
}
