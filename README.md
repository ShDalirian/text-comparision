# text comparision
first of all I apologize for my english. (;<br />
Here i create some codes to be published.<br />
for the beginning i write a code to compare two text as missmatch error.<br />
The distinctive feature of this code is that in this code **each line** is compare separatly and it try to **start comparision from begining or end depending on which side is better matched**.<br />
in the future i will apply some change to ignore Placement of words in error calculation. for example consider one word is deleted in this case all next words will detect as error while there is just one placement and it should be detected as one error not error for all next words.<br />
if there is a problem cantact me using my email address: sh.dalirian@ut.ac.ir

# run: main.py

# application:
suppose there is two text that one is ideal text and the other is extracted text (for example in OCR). so you need to compare them to calculate error rate.<br/>
# adjustable parameters:
ignor_space:bool =>it determine the space should be important in comparision or not.<br/>
less_than_char_ignore:bool => suppose there is some very short chars that are extracted incorrectly using OCR or another application. then you can ignor them using activate this parameter. by default number of ignor char is 1 but if you want to change it you can use next parameter named "ignor_char_num".<br/>
ignor_char_num:int =>Set the minimum length of a string to be ignored

# example:
here is an example:<br/>
ideal_text:str= "this is a test\nmy email address is: sh.dalirian@ut.ac.ir\nwww.x_code.com\ntime is come\n"<br/>
text:str=       "this is a test\nmy email address is: sh.dalirian@ut.ac.ir\nwww.x_code.com\ntime is come\n"<br/>
accuracy,correct_char_N,total_N=accuracy_cal(text,ideal_text,ignor_space=False,less_than_char_ignore=True,ignor_char_num=1)
the result is :<br/>
      accuracy = 100.0
      total length =  85
      correct char length =  85
as you can see, there are some adjustable parameters to define is spaces important or not. 
