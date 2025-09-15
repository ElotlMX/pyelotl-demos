import csv
from pathlib import Path


def write_feedback(file_path: Path, row: list[str], header: list[str]) -> None:
    """Append a feedback row to a CSV file, creating it with a header if it doesn't exist
    
    Parameters
    ----------
    file_path : Path
        Path to the CSV file
    row : list[str]
        List of strings representing the row to append
    header : list[str]
        List of strings representing the header row
    
    Returns
    -------
    None
    """
    if not file_path.exists():
        file_path.touch()
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        has_header = next(reader, None) is not None
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not has_header:
            writer.writerow(header)
        writer.writerow(row)