import gdown
import os

def download_from_google_drive(file_id, output_path):
  """Downloads a file from Google Drive using its file ID.

  Args:
      file_id: The ID of the file on Google Drive.
      output_path: The path where the file should be saved.
  """
  try:
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False, fuzzy=True) # Use fuzzy=True for large files
    print(f"File downloaded successfully to: {output_path}")
  except Exception as e:
    print(f"Error downloading file: {e}")
    exit(1)  # Exit with an error code if download fails

if __name__ == "__main__":
  file_id = os.getenv("1mbP66SZCS0jK7DKeQKb3PcvdgtmDdDNq")
  if not file_id:
    print("Error: GOOGLE_DRIVE_FILE_ID environment variable not set.")
    exit(1)

  output_filename = "Server.zip"
  output_directory = "."

  output_path = os.path.join(output_directory, output_filename)
  download_from_google_drive(file_id, output_path)
