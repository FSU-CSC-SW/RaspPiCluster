import Prompts

def fileManager(recorded_data):
    #this function info dumps data to a text file
    answer = input("Would you like to dump to a text file (Enter 'Y' for yes)? ")
    if answer == "y" or answer == "Y":
        saved_output = '\n'+Prompts.Prompt_1+'\n'+Prompts.Prompt_2+recorded_data+'\n'+Prompts.Prompt_3
        file1 = open("ComputationLogCSC490.txt","a")
        file1.write(saved_output)
        file1.close()
        return
    else:
        return