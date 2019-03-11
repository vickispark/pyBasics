is_male = True
is_tall = False

if is_male:
    print("you are a male")
else:
    print("not a male")


if is_male and is_tall:
    print("male or tall")
    if is_tall:
        print("tall")
    if is_male:
        print("male")
    if is_male and is_tall:
        print("both")
    else:
        print("either one")
elif is_tall and not is_male:
    print("tall not male")
elif not(is_tall) and is_male:
    print("male not tall")
else:
    print("not both")








