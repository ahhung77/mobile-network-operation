gsh create_ue_trace -id 452021071980304 -type imsi -ref 021071980304 -depth maximum -ifl all -iflm all -ip NULL -ent enodeb

gsh check_config
gsh activate_config_pending

uetracer_parser.pl -i 452022148896424

gsh action_ue_trace_start -id 452022220123366 -ref 022220123366 -type imsi -depth maximum -ifl all -iflm all
gsh action_ue_trace_stop -id  452021113873939![image](https://user-images.githubusercontent.com/45506820/110086035-754d6300-7dc4-11eb-9923-8c4f290e9d84.png)
