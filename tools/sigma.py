import os
import io
import numpy
import csv

d = "/Volumes/NicoExternalDrive/WorkInProgress/2-ColorProject/bead_sigma/t"
result = []
for f in os.listdir(d):
   print f
   fp = os.path.join(d, f)
   print fp
   if (fp.endswith(".txt")):
      s = []
      ms = []
      fparts = f.split();
      result.append(fparts[0])
      result.append(fparts[2])
      fo = open(fp, "r")
      # read the first two lines
      fo.readline()
      fo.readline()
      vals = fo.readlines()
      for val in vals:
         v = val.split('\t')
         s.append(float(v[14]))
         ms.append(float(v[18]))
      print numpy.mean(s)
      print numpy.mean(ms)
      result.append(numpy.mean(s))
      result.append(numpy.mean(ms))

outname = os.path.join(d, "output.csv")
with (open(outname, "wb")) as fout:
   outwriter = csv.writer(fout, delimiter='\t')
   for i in range(0, len(result)):
      if (i%4 == 0):
         outwriter.writerow([result[i], result[i+1], result[i+2], result[i+3]])
   fout.close
