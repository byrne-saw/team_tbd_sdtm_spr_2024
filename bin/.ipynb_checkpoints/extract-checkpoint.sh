#This script was written by Kori Price
#Date: January 27, 2024
#Purpose: Software Development Lab 2, extract Jeopardy clues


wget -O game_"${1}".html https://j-archive.com/showgame.php?game_id="${1}" 

if [ -f $1 ]; then
grep "clue_text\">" $1 | sort > clues.txt #get all clues and copy to clues.txt

wc -l *.txt #print counts

else #if file does not exist
echo "Invalid or Missing filename"
echo -n "Usage: "
echo "$0 <filename>"
echo ""

fi

