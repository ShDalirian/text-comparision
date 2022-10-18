from Missmatch_Error import accuracy_cal

ideal_text:str= "this is a test\nmy email address is: sh.dalirian@ut.ac.ir\nwww.x_code.com\ntime is come\n"
text:str=       "this is a test\nmy email address is: sh.dalirian@ut.ac.ir\nwww.x_code.com\ntime iscome\n"

accuracy,correct_char_N,total_N=accuracy_cal(text,ideal_text,ignor_space=False,less_than_char_ignore=True,ignor_char_num=1)
print("accuracy = "+str(accuracy)+"\ntotal length = "+str(total_N)+"\ncorrect char length = "+str(correct_char_N))