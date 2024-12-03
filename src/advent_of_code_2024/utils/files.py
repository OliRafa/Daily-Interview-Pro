from pathlib import Path


def read_inputs(inputs_file_path: Path) -> list[str]:
    with inputs_file_path.open("r") as buffer:
        return buffer.readlines()
