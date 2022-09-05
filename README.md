# graph-shellcode
Graph shellcode from a pure data file blob which would get injected into memory 

Steps:

1) Install miasm:
    `pip install git+https://github.com/cea-sec/miasm.git`
    
2) edit code to change the file name & architecture to be as desired

3) In the terminal convert the dot file to a png: `dot -Tpng output_file.dot > name_of_file.png`
     
4) Open the new PNG, in tandem with hex editor / ghidra.
