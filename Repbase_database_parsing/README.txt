#README
#file containing Repbase Hexapoda sequences is "repbase_full_insecta_corr.txt"

#grep command that returns a subset of lines we care about from the database -- it produces the file grep.out
grep -oh -e "ID " -e "DT .*Created)" -e "KW .*" -e "; Archaeognatha;" -e "Blattodea;" -e "Coleoptera;" -e "; Collembola;" -e "; Dermaptera;" -e "; Diptera;" -e "; Ephemeroptera;" -e "; Hemiptera;" -e "; Hymenoptera;" -e "; Lepidoptera;" -e "; Megaloptera;" -e "; Odonata;" -e "; Orthoptera;" -e "; Phasmatodea;" -e "; Phthiraptera;" -e "; Plecoptera;" -e "; Siphonaptera;" -e "; Strepsiptera;" -e "; Thysanoptera;" -e "; Trichoptera;" -e "\w*idae;" repbase_full_insecta_corr.txt > grep.out

#ran the grep_to_table.py script to convert the grep output into a tab-delimited text file which we cleaned up manually (e.g., remove unnecessary codes and semicolons) in a text editor
./grep_to_table.py grep.out

#I pasted just the family column of data to a text file and saved it as repbase_table_clean_final_fam.txt
#I then sorted and did uniq to get all unique families
sort repbase_table_clean_final_fam.txt | uniq >  repbase_table_clean_final_fam_uniq.txt

#I then made a file where the two repeat columns were omitted, I sorted it by date (oldest to newest), saved with columns in that order, and 
#used the loop_fam_date.sh script to grep out just the oldest entry for each unique family with this code:

while read -r line; 
do 
   grep -m 1 "$line" repbase_table_clean_final_fam_date.txt >> grep_fam_date.txt
done < repbase_table_clean_final_fam_uniq.txt


# I got unique orders by making text file with all orders from repbase_table_clean_final_orders.txt by pasting order column from repbase_table_clean_final.txt

sort repbase_table_clean_final_orders.txt | uniq > repbase_table_clean_final_orders_uniq.txt

# I used the unique families and orders files as lists for grep searches that summarized lots of aspects of the data in the file grep_loops.sh -- I pasted output into a spreadsheet to build relevant data tables.

