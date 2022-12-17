################ Handling exeption errors: TRY-EXCEPT ###################
new_list = [2, 4, 6, 'California']

for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number")
    