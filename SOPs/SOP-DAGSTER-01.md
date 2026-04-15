# SOP-DAGSTER-01: Asset-Based Orchestration

**Objective:** Ensure all data pipelines are reproducible, testable, and declarative using Dagster's Software-Defined Asset (SDA) framework.

## 1. Asset Definition Mandates
- **Focus on State, Not Process:** Define the data artifact being created (`@asset`), rather than the action being performed.
- **Granularity:** Break monolithic scripts into atomic assets. If an intermediate DataFrame is useful for debugging, it should be its own asset.

## 2. IO Management
- **No Hardcoded Paths:** Assets must NOT contain `df.to_csv('/hardcoded/path.csv')`.
- **Use IO Managers:** Return the Python object (e.g., Pandas DataFrame, NumPy Array) and let the configured `IOManager` handle serialization to the appropriate storage tier (Local disk, GCS, S3).

## 3. Metadata & Observability
- **Always Attach Metadata:** Every asset must yield an `Output` object containing metadata.
- **Required Metadata Fields:**
  - `row_count` (int): Number of rows or elements.
  - `preview` (Markdown): A `head().to_markdown()` preview of tabular data.
  - `provenance` (string): The source URI or pipeline stage identifier.

## 4. Execution & Testing
- **Local Dev:** Use `dagster dev` to spin up the local UI.
- **Materialization Check:** Do not report a pipeline step as "done" unless you have explicitly verified its materialization status via Dagster.
