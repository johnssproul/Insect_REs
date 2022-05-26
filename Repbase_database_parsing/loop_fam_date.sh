#!/bin/bash


while read -r line; 
do 
   grep -m 1 "$line" repbase_table_clean_final_fam_date.txt >> grep_fam_date.txt
done < repbase_table_clean_final_fam_uniq.txt



# while read -r line; 
# do 
#    grep -c "$line" repbase_table_clean_final_order.txt >> grep_order_count.txt
# done < repbase_table_clean_final_order_uniq.txt
