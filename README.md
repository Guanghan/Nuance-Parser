# Nuance-Parser
Parsing the output json file of Nuance speech recognition

--------

## Prerequisites

- Python 3.0+

--------
## Getting Started

### 1. Run Demo

	python ./parse_csv.py

### 2. I/O

**Input**

The input file is the csv file given here: [nuance_output.csv](https://github.com/Guanghan/Nuance-Parser/blob/master/nuance_ouput.csv). 

Each line is a query sentence followed by a json structure, which is the response from the nuance speech recognition system. 

**Output**

The first output is a json file [output.json](https://github.com/Guanghan/Nuance-Parser/blob/master/output.json), where each item is consisted of the four attributes explained below:

[Query]: The query sentence   

[Type]: The type of this entity

[Keys]: The hierarchy structure of keys that led to this key

[Value]: The value of this key that matched the query sentence


The second output is a txt file [output.txt](https://github.com/Guanghan/Nuance-Parser/blob/master/output.txt), which is of the same content, but more human readable for the sake of poor naked eyes. 
