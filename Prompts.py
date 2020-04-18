#this file provides print statements for python's ide and gets recorded to the text file should the user select that option during runtime

from test_data import num, worstCaseArray, num_Extensive, worstCaseArray_Extensive

Prompt_1 = "*************************\n\nInitializing...\n\nThe Variable 'worstCaseArray' is set to:\n    "+str(worstCaseArray)+"\nThe Variable 'num' is set to: "+str(num)
Prompt_1_Extensive = "*************************\n\nInitializing...\n\nThe Variable 'worstCaseArray_Extensive' is set to:\n    "+str(worstCaseArray_Extensive)+"\nThe Variable 'num_Extensive' is set to: "+str(num_Extensive)
Prompt_2 = "\n~~Beginning Computations~~\n"
Prompt_3 = "~~Competitions are Complete~~\n"
Prompt_dev = "*************************\n\nInitializing...\n\nUtilizing Both Heavy and Light Test Cases"

def Printer(given_list):
    #input: takes a list of data
    #output: prints out the data and constructs a prompt to return to the main file
    prompt_tracker = ""
    for prompt in given_list:
        print(prompt)
        print("\n")
        prompt_tracker = prompt_tracker + "\n" + prompt
    return prompt_tracker