#! /usr/bin/python3

import re

pattern = re.compile(".*idae;")
pattern2 = re.compile("; DNA transposon;")


with open('repbase_table.txt', 'w') as final_out:
	with open ("grep_out.txt", 'r') as name_data:
	
		for line in name_data:
			line_clean = line.strip('\n') #strips out beginning and end of line characters
			if "ID " in line_clean:
				final_out.write('\n') #only place with carriage return
			elif "Created" in line_clean:
				line_clean_parsed = re.split(r'[-,\s]\s*',line_clean)
				#dates = re.split(r'[-,\s]\s*',tennis_greats)
				final_out.write(line_clean_parsed[1] + '\t' + line_clean_parsed[2] + '\t' + line_clean_parsed[3])			
			elif "; Non-LTR Retrotransposon;" in line_clean:
				line_clean_parsed = re.split(r'[;,\s]\s*',line_clean)
				final_out.write('\t' + "Non-LTR Retrotransposon" + '\t' + line_clean_parsed[1])				
			elif pattern2.search(line_clean):
			#elif "; DNA transposon;" in line_clean:
				line_clean_parsed = re.split(r'[;,\s]\s*',line_clean)
				final_out.write('\t' + "DNA transposon" + '\t' + line_clean_parsed[1])			
			elif "; LTR Retrotransposon;" in line_clean:
				line_clean_parsed = re.split(r'[;,\s]\s*',line_clean)
				final_out.write('\t' + "LTR Retrotransposon" + '\t' + line_clean_parsed[1])				
			elif "Archeognatha" in line_clean:	
				final_out.write('\t' + 'Archeognatha')
			elif "Blattodea" in line_clean:
				final_out.write('\t' + 'Blattodea')
			elif "Coleoptera" in line_clean:
				final_out.write('\t' + 'Coleoptera')
			elif "Collembola" in line_clean:
				final_out.write('\t' + 'Collembola')
			elif "Dermaptera" in line_clean:
				final_out.write('\t' + 'Dermaptera')
			elif "Diptera" in line_clean:
				final_out.write('\t' + 'Diptera')
			elif "Ephemeroptera" in line_clean:
				final_out.write('\t' + 'Ephemeroptera')
			elif "Hemiptera" in line_clean:
				final_out.write('\t' + 'Hemiptera')
			elif "Hymenoptera" in line_clean:
				final_out.write('\t' + 'Hymenoptera')
			elif "Lepidoptera" in line_clean:
				final_out.write('\t' + 'Lepidoptera')
			elif "Megaloptera" in line_clean:
				final_out.write('\t' + 'Megaloptera')
			elif "Odonata" in line_clean:
				final_out.write('\t' + 'Odonata')
			elif "Orthoptera" in line_clean:
				final_out.write('\t' + 'Orthoptera')
			elif "Phasmatodea" in line_clean:
				final_out.write('\t' + 'Phasmatodea')
			elif "Phthiraptera" in line_clean:
				final_out.write('\t' + 'Phthiraptera')
			elif "Plecoptera" in line_clean:
				final_out.write('\t' + 'Plecoptera')
			elif "Siphonaptera" in line_clean:
				final_out.write('\t' + 'Siphonaptera')
			elif "Strepsiptera" in line_clean:
				final_out.write('\t' + 'Strepsiptera')
			elif "Thysanoptera" in line_clean:
				final_out.write('\t' + 'Thysanoptera')
			elif "Trichoptera" in line_clean:
				final_out.write('\t' + 'Trichoptera')
			elif pattern.search(line_clean):
				#print(pattern.search(line_clean).group())
				final_out.write('\t' + pattern.search(line_clean).group())
								
print ("first pass done")

RepClasses = ['	Non-LTR Retrotransposon', '	LTR Retrotransposon', '	DNA transposon']
#print(RepClasses)


