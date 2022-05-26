
#################### Fig 1 code -- makes various plots that were combined to form Fig. 1 in Illustrator
library (ggplot2)

in_data5<-read.table("Dataframe_ordered_by_tree_final3.txt", header = TRUE)
print(in_data5)

ggplot(data = in_data5, aes(x = TreeOrder, y = Assembly_Length)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 4000000000), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = all_repeats_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 1), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+
  
ggplot(data = in_data5, aes(x = TreeOrder, y = LINEs_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = LTRs_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = DNA_trans_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = Repeat_BUSCOs)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 400), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = unclassified_prop_reps)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 1), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = empties)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 700), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = unclassified_prop_reps)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, 1), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = SINEs_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = tandem_repeats_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

ggplot(data = in_data5, aes(x = TreeOrder, y = other_repeats_proportion)) +
  geom_bar(stat='identity') + coord_cartesian(ylim = c(0, .3), expand = FALSE) + theme_minimal()#+ scale_fill_manual(values=bar_cols)+

