import sys
import utils.file as file
import time

if __name__ == "__main__":
    if len(sys.argv) > 3:
        log_dir = sys.argv[1]
        file_prefix = sys.argv[2]
        appended_file = sys.argv[3]
    else:
        log_dir = '/home/hosseinamiri/Downloads/pol-archived-main/data/sample_logs_raw_small'
        file_prefix = 'Checkin'
        appended_file = '/home/hosseinamiri/Downloads/pol-archived-main/data/sample_logs_raw_small/check-in.tsv'
    print(f"Integrating log files from {log_dir} with prefix {file_prefix} into {appended_file}")
    time.sleep(5)
    file.integrate_log_files(log_dir, file_prefix, appended_file)

