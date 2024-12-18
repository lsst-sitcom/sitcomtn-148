#python
#erplace pandoc thing with figure
import os
import fileinput
import shutil
import re



def doFile(inFile ):
	"find pandoc line replace with figure block"
	count =0
	pdre = re.compile(r"^.+\{(.+)\}")

	f=inFile
	of = f + ".bak"
	shutil.copyfile(f,of)
	print("Processing " + f)
	fin = open (of,'r')
	fout = open (f,'w')
	for line in fin :
            if 'pandocbounded'  in line:
                count= count + 1
                pan = pdre.match(line)
                imgpath = pan.groups(1)[0]
                imgpath=imgpath.replace('}','')
                print(imgpath)
                fout.write(r"\begin{figure}" +"\n")
                fout.write(r"\begin{centering}" +"\n")
                fout.write(fr"\includegraphics[width=0.9\textwidth]{{{imgpath}}}" +"\n")
                fout.write(r"\end{centering}" +"\n")
                fout.write(r"\end{figure} " +"\n")
            else:
                fout.write(line)
	fout.close()
	fin.close()

	print(f"{inFile} .... {count} figures ")
	return;
 # End DoDir




### MAIN
doFile("body.tex")
