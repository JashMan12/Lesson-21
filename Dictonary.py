# 1) Create a dictionary `test_dict` with words as keys and numbers as values.
test_dict={'Food':90,'Juice': 90, 'Art':80}
print(test_dict)
K=90
count=0
for i in test_dict:
    if test_dict[i]==K:
        count+=1
print("The value of count is", count)

# 5) Use a `for` loop to iterate through each `key` in the dictionary:
# a) Check if the value of the current key `test_dict[key]` is equal to `K`.

# b) If yes, increase the counter `res` by 1.

# 6) After the loop finishes, print the final count `res`

# which represents the frequency of value `K` in the dictionary.