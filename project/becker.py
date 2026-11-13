on = True
while on:
    option = input("Welcome to the Becker-Arjun Word and Statistics Sorter! Type 'math' for statistics or type word for word sorter. Type 'exit' to exit the program."e
if option == "math":
    num_stats()
elif option == "word":
    word_sorter()
elif option == "exit":
    print("Goodbye!")
    on = False
else:
    option= input("Please type only 'math', 'word', or 'exit', please.")
i the program."e)
num_list = []
variance_list = []
mean_absolute_deviation = []
word_list = []
word_ratios = []
lengt

name = "Michael"
def give_name(name):
    print(name)
_list = []
hhhhhh
def m_stats():


    # Reminder for    er of stuff:
    # mean, med     range, mode
    # int    artile range
    # variance and st    rd deviation
      min and max
    # skew and mean abs    e deviation

    amount = int(input("How many numbers would you li    o enter? "))
    if amount > 0 and amount.is_        == Tr                     else:
        print("Enter an in        o                
        
    for _ i        amount):
        a = float(input("Ent        ber: "))
        num    t.append(a)

    sorted_num_list =     ed(num_list)
    length_of_list = int    (num_list))

    mean = sum(num_list    ngth_of_list
    median = (sorted_num_list[length_of_list // 2] + sorted_num_list[(length_of_list    ) // 2]) / 2     mode = None
     ax_count = 0
    for item i        m_list):
        count = num_        nt(item)
        if cmat:
            count
            mode = item
    if        nt == 1:
         ode = 'None'
    range_of_nums_list = max(num_list) -     num_list)



    mid_point = (max(num_list) + mi    m_list)) / 2
    mid = len    of_list // 2
    first_half_list = sorte    m_list[:mid]
    second_half_list = sorte    m_list[mid:]
    median1 = (first_half_list[len(first_half_list) // 2] + first_half_list[(len(first_half_list)    ) // 2]) / 2
    median2 = (second_half_list[len(second_half_list) // 2] + second_half_list[(len(second_half_list)    ) // 2]) / 2
    interquartile_range = abs(med     - median2)

    for         um_list:
        b = (        an) ** 2
        varianc    st.append(b)
    p_variance = sum(variance_list)     ngth_of_list
    s_variance = sum(variance_list) / ( lengt    _list - 1 )

    standard_deviation = p    iance ** 0.5
         an == 0:
        coefficient_of_    ation            else:
        coefficient_of_variation = standard_d    tion / mean

    for         um_list:
        c =         - mean)
        mean_absolute_dev    on.append(c)
    mean_absolute_deviation_amount = sum(mean_absolute_deviation) / len(mean_absolut    viation)




    print(    an: {mean}")
    print(f"M    n {median}")
    print(    de: {mode}")
    print(f"Range: {range    nums_list}")
    print(f"Midpoin    mid_point}")
    print(f"Max: {    num_list)}")
    print(f"Min: {    num_list)}")
    print(f"Sum: {    num_list)}")
    print(f"Quartil     {median1}")
    print(f"Quartil     {median2}")
    print(f"Interquartile range: {interq    ile_range}")
    print(f"Population variance    _variance}")
    print(f"Sample variance    _variance}")
    print(f"Standard deviation: {stand    deviation}")
    if coefficient_of_va        is None:
        print("Coefficient of variat    (CV):            else:
        print(f"Coefficient of variation (CV): {coefficient_of_    ation:.2%}")
    print(f"Mean absolute deviation: {mean_absolute_deviation_amount}")

de    rd_sorte    
    #filler
      alphabetical
    # reve    alphabetical
    # numb    f     acters
    

    total_words = int(input("How many words would you like to enter? (Remember enter 1    a time): "))
    for _ in ran        _words):
        d = input("        word: ")
        word    t.    nd(d)

    

    alphabetically = sorted(wor    st, key=str)
    reverse_alphabetically = sorted(word_list, reverse    e, key=str)

    print(reverse_alphabetically, al    etically)



    vowel    'aeiouAEIOU'
    for wo        rd_list:
        amoun        ants = 0
        a        wels = 0
        for            ord:
            if letter in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPAS                
                if l                                     am                
                                          amount                
                
            if amo                
                            0000
                 
                ratio = amount_consonants     ount_vowels

    word_ratios.append    tio, word])

    lowest_highest = sor    word_ratios)
    highest_lowest = sorted(word_ratio   r    se=True)
   
    length    word








    print(f"Alphabetically: {a    betically}")
    print(f"Reverse alphabetically: {reverse_a    betically}")
    print(f"Ratio highest to lowest: {h    st_lowest}")
    print(f"Ratio lowest to highest: {l    t_highest}")
    print(f"B    rd length:"      print(f""      print(f""      print(f""      print(f"")        nt(f"")

        
num_stats()