FCM := ../../../../flow_cytometry

all : 20170216_confirm_uhf_hits.svg 

20170216_confirm_uhf_hits.svg : $(FCM)/fold_change.py $(FCM)/data/20170216_confirm_uhf_hits.yml
	$^ -o $@ -v -O 6x6 -d 6e-3,2e0
