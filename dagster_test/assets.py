from dagster import asset, Output, MetadataValue
import pandas as pd
import numpy as np

@asset
def raw_data():
    """A basic raw data asset."""
    data = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=100, freq="D"),
        "value": np.random.randn(100).cumsum()
    })
    return Output(
        data,
        metadata={
            "row_count": len(data),
            "preview": MetadataValue.md(data.head().to_markdown())
        }
    )
