def solution(order):
    lista=list(str(order))                      #int->string->list data type transfer
    clap=["3","6","9"]                          #clap digit
    count=0
    for i in lista:                             #in lista
        if i in clap:                           #find 3,6,9
            count+=1                            #clap
    return count





def solution(phone_number):
    answer = []                                 #to use append, transfer empty list
    phone_n_list=list(phone_number)             #to use range, transfer string->list
    minus_four=len(phone_n_list)-4              #last four digits return digits
    
    for i in phone_n_list[:minus_four]:         
        answer.append("*")
    for i in phone_n_list[minus_four:]:
        answer.append(i)
    return "".join(answer)                      #list->string