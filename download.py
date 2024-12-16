limport gdown
import os

def download_from_google_drive(file_id, output_path):
  """Downloads a file from Google Drive using its file ID.

  Args:
      file_id: The ID of the file on Google Drive.
      output_path: The path where the file should be saved.
  """
  try:
    gdown.download(id=file_id, output=output_path, quiet=False)
    print(f"File downloaded successfully to: {output_path}")
  except Exception as e:
    print(f"Error downloading file: {e}")

if __name__ == "__main__":
  file_id = "1mbP66SZCS0jK7DKeQKb3PcvdgtmDdDNq"  # Substitua pelo ID do arquivo no Google Drive
  output_filename = "hell.zip"
  output_directory = "."

  output_path = os.path.join(output_directory, output_filename)
  download_from_google_drive(file_id, output_path)
