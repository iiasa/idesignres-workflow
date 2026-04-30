from pathlib import Path
import pyam
from nomenclature import DataStructureDefinition, RegionProcessor, process


here = Path(__file__).absolute().parent


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Use subannual timeseries for validation if relevant for timeseries data
    if "subannual" in df.dimensions:
        dimensions = ["region", "variable", "subannual"]
    else:
        dimensions = ["region", "variable"]

    # Run the validation and region-processing
    dsd = DataStructureDefinition(here / "definitions", dimensions=dimensions)
    processor = RegionProcessor.from_directory(path=here / "mappings", dsd=dsd)
    return process(df, dsd, processor=processor)
