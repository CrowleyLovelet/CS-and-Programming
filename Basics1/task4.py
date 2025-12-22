time_shtuka =[int(chis) for chis in input("wright time like this hh:mm:ss").split(":")]
if 0<= time_shtuka[0] <=24 and 0<= time_shtuka[1] <=60 and 0<= time_shtuka[2] <=60:
    print("everything is ok")
else:
    print("do u know hot time works?")

