import pandas as pd
import os
from datetime import datetime
import shutil
import traceback

# Paths
input_folder = "input"
output_folder = "output"
archive_folder = "archive"
log_file = "logs/process.log"
error_threshold_mb = 50  # Warn if file is too large

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def process_file(file_path):
    try:
        log(f"🚀 Starting processing: {file_path}")

        # File size check
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > error_threshold_mb:
            log(f"⚠️ WARNING: File {file_path} is {file_size_mb:.2f}MB (above {error_threshold_mb}MB)")

        df = pd.read_csv(file_path)
        total_rows = len(df)

        # Filter rows
        filtered = df[df["sales"] > 600]
        filtered_rows = len(filtered)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"{output_folder}/filtered_{ts}.csv"
        filtered.to_csv(output_path, index=False)

        log(f"✅ Processed: {total_rows} rows → {filtered_rows} passed filter")
        log(f"📤 Filtered data saved to {output_path}")

        # Archive original
        base_name = os.path.basename(file_path)
        archive_path = f"{archive_folder}/{base_name[:-4]}_{ts}.csv"
        shutil.move(file_path, archive_path)
        log(f"🗃️ Archived original file to {archive_path}")

    except Exception as e:
        log(f"❌ ERROR while processing {file_path}: {e}")
        log(traceback.format_exc())

def main():
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            process_file(os.path.join(input_folder, file))

if __name__ == "__main__":
    main()
