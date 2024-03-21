#This script was written by Kori Price
#Date: March 21, 2024
#Purpose: Extract answers for jeoparDIY project

if [ -f $1 ]; then

grep "correct_response\">" $1 | sort > answers.txt

wc -l *.txt

else
echo "Invalid or Missing filename"
echo -n "Usage: "
echo "$0 <filename>"
echo ""

fi