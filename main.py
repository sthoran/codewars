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
from kyu7.cat_and_mouse import cat_mouse
from kyu7.responsible_drinking import hydrate
from kyu7.sayhello import greet
from kyu7.character_count import validate_word
from kyu7.odder_than_the_rest import odd_one
from kyu7.fix_my_phone_number import is_it_a_num
from kyu7.debug_function import multi,add,reverse
from kyu6.norm_out_of_range_array_index import  norm_index_test
from kyu8.no_boring_zeros import no_boring_zeros
from kyu7.substring_fun import nth_char
from kyu7.sortby import sort_list
from kyu7.strong_password import check_password
#from kyu6.ticker import ticker
from kyu6.wordify import wordify
from kyu8.vowel import is_vow


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
    cat_mouse('C....m')
    hydrate("1 beer")
    greet("Jakob")
    validate_word("abcabc")
    odd_one([2,16,98,10,13,78])
    is_it_a_num("S:)0207ERGQREG88349F82!efRF)")
    multi([8,2,5])
    add([1,15,3])
    reverse("Hello Word")
    norm_index_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    no_boring_zeros(12090)
    nth_char(['yoda', 'best', 'has'])
    sort_list("b", [ {"a": 2, "b": 2},{"a": 3, "b": 40},{"a": 1, "b": 12}] )
    check_password("P1@p")
    #ticker('Beautiful is better than ugly.', 10, 41)
    wordify(220)
    is_vow(["e",121,110,113,113,103,121,121,"e",107,103 ])
    
if __name__ == "__main__":
    main()