import Prompts

def fileManager(recorded_data):
    #input: this function takes a string of containing a combination of prompts and data
    #output: this function info dumps data to a text file
    answer = input("Would you like to dump to a text file (Enter 'Y' for yes)? ")
    if answer == "y" or answer == "Y":
        saved_output = '\n'+Prompts.Prompt_1+'\n'+Prompts.Prompt_2+recorded_data+'\n'+Prompts.Prompt_3
        file1 = open("ComputationLogCSC490.txt","a")
        file1.write(saved_output)
        file1.close()
        return
    else:
        return

def fileManager_Autosaver(recorded_data):
    #input: this function takes a string of containing a combination of prompts and data
    #output: this function info dumps data to a text file
    saved_output = '\n'+Prompts.Prompt_1+'\n'+Prompts.Prompt_2+recorded_data+'\n'+Prompts.Prompt_3
    file1 = open("ComputationLogCSC490.txt","a")
    file1.write(saved_output)
    file1.close()
    return


def Para_fileManager(recorded_data, test_data):
    #input1: a string of containing a combination of prompts and data
    #input2: a string of a keyword indicative of data entered into application
    #output: this function info dumps data to a text file
    answer = input("Would you like to dump to a text file (Enter 'Y' for yes)? ")
    if answer == "y" or answer == "Y":
        if test_data == "extensive":
            saved_output = '\n'+Prompts.Prompt_1_Extensive+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
            file1 = open("ComputationLogCSC490.txt","a")
            file1.write(saved_output)
            file1.close()
            return
        elif test_data == "dev":
            saved_output = Prompts.Prompt_dev+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
            file1 = open("ComputationLogCSC490.txt","a")
            file1.write(saved_output)
            file1.close()
            return
        else:
            saved_output = Prompts.Prompt_1+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
            file1 = open("ComputationLogCSC490.txt","a")
            file1.write(saved_output)
            file1.close()
            return
    else:
        return

def Para_fileManager_Autosaver(recorded_data, test_data):
    #input1: a string of containing a combination of prompts and data
    #input2: a string of a keyword indicative of data entered into application
    #output: this function info dumps data to a text file
    if test_data == "extensive":
        saved_output = '\n'+Prompts.Prompt_1_Extensive+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
        file1 = open("ComputationLogCSC490.txt","a")
        file1.write(saved_output)
        file1.close()
        return
    elif test_data == "dev":
        saved_output = '\n'+Prompts.Prompt_dev+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
        file1 = open("ComputationLogCSC490.txt","a")
        file1.write(saved_output)
        file1.close()
        return
    else:
        saved_output = '\n'+Prompts.Prompt_1+'\n'+Prompts.Prompt_2+recorded_data+'\n\n'+Prompts.Prompt_3
        file1 = open("ComputationLogCSC490.txt","a")
        file1.write(saved_output)
        file1.close()
        return