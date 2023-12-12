set -e

tables="/content/drive/MyDrive/CMPE_258/C3SQL-master/data/spider/tables.json"
dataset_path="/content/drive/MyDrive/CMPE_258/C3SQL-master/data/spider/dev.json"
db_dir="/content/drive/MyDrive/CMPE_258/C3SQL-master/data/spider/database"
output_dataset_path="/content/drive/MyDrive/CMPE_258/C3SQL-master/predicted_sql.txt"

processed_dataset_path="/content/drive/MyDrive/CMPE_258/C3SQL-master/generate_datasets/C3_dev.json"

# preprocess data
bash /content/drive/MyDrive/CMPE_258/C3SQL-master/scripts/prepare_dataset.sh $tables $dataset_path $db_dir $processed_dataset_path
# run prediction
python /content/drive/MyDrive/CMPE_258/C3SQL-master/src/generate_sqls_by_gpt3.5.py --input_dataset_path $processed_dataset_path  --output_dataset_path $output_dataset_path --db_dir $db_dir

