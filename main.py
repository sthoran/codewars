from kyu8.is_the_string_uppercase import kyu8_is_uppercase
from kyu8.grasshopper_grade_book import get_grade
from kyu7.even_num_array import even_numbers
from kyu7.create_matrix import get_matrix
from kyu7.increment import incrementer
from kyu7.large_matrix_expected_value import expected_value
from kyu7.factorizing import factorial
from kyu8.counting_sheep import count_sheeps
from kyu8.age_range_comp import  dating_range
from kyu7.catch_sign_change import catch_sign_change
from kyu7.string_of_first_characters import make_string
from kyu8.reserved_strings import solution
from kyu7.find_missing_number import  missing_no
from kyu7.largest_element import largest

nums = list(range(0,101))
nums.remove(5)

def main():
    kyu8_is_uppercase('+H%)O9Z`JHPNQ4M*JK_@8N&{W 05\\SAYBV"')
    get_grade(94,90,93)
    even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    get_matrix(5)
    incrementer([4, 6, 7, 1, 3]) 
    expected_value(11, 5)
    factorial(5)
    count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ])
    catch_sign_change([-7,-7,7,0])
    dating_range(17)
    make_string("sees eyes xray yoat")
    solution('world')
    missing_no(nums)
    largest(2,[10,9,8,7,6,5,4,3,2,1]) 
    
    
if __name__ == "__main__":
    main()