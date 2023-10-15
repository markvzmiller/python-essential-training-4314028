letters = 'AAAAABBBBCCCDDEEF'

smile = '''

                                                                               
                                                                               
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                      
                    %%%%%%%%                         %%%%%%%%                  
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%            
           %%%%%%                                               %%%%%          
          %%%%%                                                   %%%%%        
        %%%%%                                                       %%%%%      
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%    
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%  
    %%%%                    %%%%%              %%%%%                     %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%  
    %%%%       %%%%%%                                        %%%%%       %%%%  
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%    
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%        
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%          
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                        
                                   %%%%%%%%%%%%                                
                                                                               
                                                                                 

'''

giraffe = '''

                                       ._ o o
                                       \_`-)|_
                                    ,""       \
                                  ,"  ## |   ಠ ಠ.
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


'''

man = '''
              %%%%%%%%
            %%        %%
           %%   0  0   %%
                ____

                %%%%  
             %%%%%%%%%%%
'''

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]  # sets to first char in string
    count = 0
    for char in stringVal:  # first char will not cause a change because it set to first char in string
        if prevChar != char:
            encodedList.append((prevChar, count)) # loop will count char until a change is detected, then append char and count as a tuple to list
            count = 0  # sets the count back to 0 for next char count
        prevChar = char
        count = count + 1 # keeps track of how many chars we see without a change
   
    encodedList.append((prevChar, count))  # this appends the last char and countas a tuple, because no change, the if won't append them, so we do it here
  # if you want to see encodedList uncomment the following line
  # print encodedList
    return encodedList

def decodeString(encodedList): # input the list of tuples
    decodedStr = ''
    for item in encodedList: # go through each item in the list and multiply the item by the count
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr
###
# Run example:
# encodedLetters = encodeString(letters) calls function and assigns to variable
# print(encodedLetters) to see list of tuples
# print(decodeString(encodedLetters)) call function with variable and prints
#
# encodedMan = encodeString(man) calls function and assigns to variable
# print(decodeString(encodedMan)) call function with variable and prints
#
# encodedSmile = encodeString(smile)
# print(decodeString(encodedSmile))
#
# encodedGiraffe = encodeString(giraffe)
# print(decodeString(encodedGiraffe))

	
