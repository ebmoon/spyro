for x in {36..70}
do
sketch -V 5 partition.sk > out${x}.out
done
grep 'TOTAL TIME' out*.out | awk '{print($4/1000.0)"  "($7/1000)"  "($10/1000);}' > summary

