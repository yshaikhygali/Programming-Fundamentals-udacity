import os


def rename_files():
    file_list = os.listdir(r"/Users/yerlanshaikh/Desktop/udacity_python/prog_fund/prank/")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"/Users/yerlanshaikh/Desktop/udacity_python/prog_fund/prank/")
    remove = "0123456789"
    table = str.maketrans("", "", remove)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(table))

    os.chdir(saved_path)


rename_files()

# intab = "aeiouxm"
# outtab = "1234512"
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print (str.translate(trantab)
