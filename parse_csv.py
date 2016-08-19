# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:52:39 2016

@author: Guanghan Ning
"""

import json
from io import StringIO
from check_value import check_string

def recursive_process(entity, query_str, key_history, type_str):    
    if not isinstance(entity, str):  
        for key in entity:
            print("key: %s , value: %s" % (key, entity[key]) )

            # Add key_history
            key_history.append(key)

            # Get the type
            if isinstance(key, str):
                if check_string(key, 'type'):
                    type_str = entity[key]
            
            # Check if the value is in the query sentence, if so, output information
            if isinstance(entity[key], str):
                if check_string(query_str, entity[key]):
                    print("\n_________Found string: [%s]" % entity[key])
                    print("_________From Query: [%s]" % query_str)
                    print("_________Key History: %s" % key_history)
                    txtfile.write("\nFound string: [%s]\n" % entity[key])
                    txtfile.write("From Query: [%s]\n" % query_str)
                    txtfile.write("Key Hierarchy: %s\n" % key_history)
                    if type_str: 
                        print("_________type: %s\n" % type_str)
                        txtfile.write("Type: %s\n" % type_str)
                    else: 
                        print("")
                        txtfile.write('\n')
                    mydict= {
                        'Value': entity[key],
                        'Query': query_str,
                        'Keys': key_history,
                        'type': type_str
                    }
                    json.dump(mydict, outputfile) 
                    outputfile.write(',\n')
            
            # Do recursion
            if isinstance(entity[key], dict):
                recursive_process(entity[key], query_str, key_history, type_str)
            elif isinstance(entity[key], list):
                for i in range(len(entity[key])):
                    recursive_process(entity[key][i], query_str, key_history, type_str)
            else: # Clear key_history if reaching the end of a branch
                key_history[:]= []


def parse_json_file(csv_file):
    with open(csv_file) as f:        
        content = f.readlines()
        print("Totally %d queries" % len(content))
        for i in range(len(content)):  
            print("\n -----------------Currently working on %d th query--------------------" % i)
            
            ind= content[i].find(';[')+1
            query_str= content[i][0:(ind-1)]            
            json_str= content[i][ind:]
            
            file = StringIO(json_str)
            data= json.load(file)
            
            for j in range(len(data)):
                print('\n',  end="")
                recursive_process(data[j], query_str, [], '')            


def demo():
    parse_json_file('output_7419.csv')
    
    
'''------------------------------------------------------------------------'''

if __name__ == '__main__':
    mydict= {
        'Value': 0,
        'Query': 0,
        'Keys': 0,
        'type': 0
    }
    feeds= []
    
    txtfile= open("output.txt", "w")            
    outputfile= open("output.json","w")
    outputfile.write('[')    

    demo()
    
    outputfile.write('{}]')
    outputfile.close()
    txtfile.close()
    
    


'''-------------other things we can do-------------------------------------'''
#print(data)             # display the original json string
    
#print(data[0].keys())    # give all the available keys
#print(data[0].values())  # give all the available values
#print(data[0].items())    # give all the key-value pairs

#print(data[0]['domain'])  # get a particular value given a key
#print(data[0]['type'])   # get a particular value given a key  