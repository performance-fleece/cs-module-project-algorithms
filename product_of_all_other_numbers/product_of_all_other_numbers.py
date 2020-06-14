'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    total = 1
    prev_results = {}
    final_result = []

    for i in arr:
        total = total * i
    # print(total)

    for i in arr:
                  
        if i not in prev_results:
            temp_res = total/i
            prev_results[i] = temp_res
            final_result.append(temp_res)
        else:
            final_result.append(prev_results[i])


    return final_result
    
    # result = [ result(i) for i in arr]



    

    
testarr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
expected = [13547520, 10536960, 94832640, 11854080, 15805440, 13547520, 11854080, 11854080, 13547520, 9483264]

print(product_of_all_other_numbers(testarr))

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
