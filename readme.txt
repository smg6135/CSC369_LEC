tr-headloop.ref

Number of instruction pages: 7
Number of data pages: 135
Most accessed page in instructions: 0x108
Most accessed page in datas: 0x1fff000

0x108 has the highest page access count maybe due to storing a variable that is frequently need to be accessed in the instructions, hence it could be some constant variable that refstring.py has such as data. Every time the loop runs, this has to be accessed. 

0x1fff000 has the highest page access count maybe due to storing a local variable that is frequently reaccessed to re-define and use it as a conditions in if conditions and many more. addr and instr is frequently used through out refstring.py in if conditions and print calls. 

tr_matmul.ref

Number of instruction pages: 10
Number of data pages: 397
Most accessed page in instructions: 0x108
Most accessed page in datas: 0x1fff000

same as the headloop, 0x108 has the highest page access count maybe due to storing a variable that is frequently need to be accessed in the instructions, hence it could be some constant variable that refstring.py has such as data. Every time the loop runs, this has to be accessed. 

also same as the headloop, 0x1fff000 has the highest page access count maybe due to storing a local variable that is frequently reaccessed to re-define and use it as a conditions in if conditions and many more. addr and instr is frequently used through out refstring.py in if conditions and print calls. 