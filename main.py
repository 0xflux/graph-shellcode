from miasm.analysis.binary import Container
from miasm.analysis.machine import Machine
from miasm.core.locationdb import LocationDB


"""

Steps:

1) Install miasm:
    pip install git+https://github.com/cea-sec/miasm.git  (note requires LLVM, should be fine on linux)

2) edit code to change the file name & architecture to be as desired

3) In the terminal convert the dot file to a png:
     dot -Tpng output_file.dot > name_of_file.png

4) Open the new PNG, in tandem with hex editor / ghidra.

"""


def main():
    filename = "filename"  # EDIT AS DESIRED

    with open(filename, 'rb') as f:
        buf = f.read()

    loc_db = LocationDB()
    container = Container.from_string(buf, loc_db)

    machine = Machine('x86_32')  # EDIT AS DESIRED

    mdis = machine.dis_engine(container.bin_stream, loc_db=loc_db)
    mdis.follow_call = True
    mdis.dontdis_retcall = True

    disasm = mdis.dis_multiblock(offset=0)

    output_file_name = 'output_file.dot'
    open(output_file_name, 'w').write(disasm.dot())


if __name__ == '__main__':
    main()

