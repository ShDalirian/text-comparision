def accuracy_cal(detected_text:str,ideal_text:str,ignor_space:bool=True,less_than_char_ignore:bool=True,ignor_char_num:int=1,endfire_priority:bool=True):
    sub:int=0
    sub_ideal:int=0
    if ideal_text[-1]!="\n":
        ideal_text+="\n"
        sub_ideal=1
    if detected_text[-1]!="\n":
        sub=1
        detected_text+="\n"
    CD_text=detected_text
    CI_text=ideal_text
    if ignor_space:
        CI_text=CI_text.replace(" ","")
        CD_text=CD_text.replace(" ","")
        ideal_text=ideal_text.replace(" ","")
    total_char:int=len(ideal_text)-sub_ideal
    correct_char:int=0
    ignor_char_count:int=0
    line_number:int=0
    while CI_text.find("\n")!=-1:
        if less_than_char_ignore==True and ((CD_text.find("\n")<=ignor_char_num and CD_text.find("\n")!=-1) or
        (CI_text.find("\n")<=ignor_char_num and CI_text.find("\n")!=-1)):
            if CD_text.find("\n")<=ignor_char_num:
                CD_text=CD_text.replace(CD_text[0:CD_text.find("\n")+1],"",1)
            if CI_text.find("\n")<=ignor_char_num:
                CI_text=CI_text.replace(CI_text[0:CI_text.find("\n")+1],"",1)
                ignor_char_count    +=1

        else:
            if CI_text.find("\n")!=-1 and CD_text.find("\n")!=-1:
                if (CI_text[CI_text.find("\n")-1].upper()==CD_text[CD_text.find("\n")-1].upper() and CI_text[CI_text.find("\n")-2].upper()==CD_text[CD_text.find("\n")-2].upper()
                    and endfire_priority):
                    LI:int=CI_text.find("\n")-1
                    LD:int=CD_text.find("\n")-1
                    b=+1
                else:
                    LI=0
                    LD=0
                    b=-1
                for a in range(min(CI_text.find("\n"),CD_text.find("\n"))):
                    if CI_text[LI-(b*a)].upper()==CD_text[LD-(b*a)].upper():
                        correct_char +=1
            CI_text=CI_text.replace(CI_text[0:CI_text.find("\n")+1],"",1)
            CD_text=CD_text.replace(CD_text[0:CD_text.find("\n")+1],"",1)
            line_number+=1
    accuracy=(correct_char+line_number-sub-2*sub_ideal)/total_char*100 #+1 is for "\n"
    return accuracy,correct_char+line_number-sub,total_char
