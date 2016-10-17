import data_models
import csv
import sys

mov_daily_path = sys.argv[1]+"movisens_daily.csv"
mov_fv_path = sys.argv[1]+"movisens_fv.csv"
fm_pre_path = sys.argv[1]+"findmind_pre.csv"
fm_post_path = sys.argv[1]+"findmind_post.csv"

id_path = sys.argv[1]+"0_ID_MASTER.csv"
screening_path = sys.argv[1]+"1_SCREENING_MASTER.csv"
fv_text_path = sys.argv[1]+"2_FV_MASTER.csv"
post_path = sys.argv[1]+"3_POST_MASTER.csv"

with open(id_path):
