def rabits(months,offsprings):
    if months == 1 or months == 2:
        return 1
    #F(n)=F(n-1)+k*F(n-2)
    #Rabits after n months = rabits previous month + (offsprings * mature rabits)
    #                                                       new rabbits
    count = 2
    fn_2 = 1
    fn_1 = 1
    while count < months:
        #print(f"{fn_1}+({offsprings}*{fn_2})={fn_1+(offsprings*fn_2)}")
        temp = fn_1
        fn_1 = fn_1+(offsprings*fn_2)
        fn_2 = temp
        count+=1
    return fn_1
        
print(rabits(6,1))