# SOP-PROVENANCE-01: Broadstore Data Provenance

**Objective:** Constantly articulate the scientific method in all agentic development and analysis. Ensure that every script, visualization, and insight is strictly traceable via a `bs://` (Broadstore) Semantic URI.

## 1. The 6-Step Hierarchy
All analytical workflows must adhere to the formal `bs://` URI schema to ensure perfect reproducibility. The pipeline progresses strictly as:

1. **`bs://project.obs(uuid)`** [Observation] - The empirical trigger.
2. **`bs://project.hypoth(uuid)`** [Hypothesis] - The logical proposition derived from the observation.
3. **`bs://project.hypoth.test(uuid)`** [Test] - The specific analytical test or script execution.
4. **`bs://project.hypoth.test.result(uuid)`** [Result] - Raw metrics, datasets, or outputs.
5. **`bs://project.hypoth.test.result.interp(uuid)`** [Interpretation] - Scientific or operational meaning.

## 2. The Output Template Mandate
Whenever you perform a task involving data analysis, script creation, or result interpretation, you MUST prefix your response with the following metadata block:

```markdown
**[bs://project(nickname--uuid).obs(nickname--uuid).hypoth(...)]**
*   **Observation:** (The empirical trigger)
*   **Hypothesis:** (The logical proposition)
*   **Test:** (The execution details)
*   **Result:** (Raw metrics/findings)
*   **Interpretation:** (Scientific/Operational meaning)
```

## 3. Loop-Back Protocol
If an Interpretation reveals a new biological phenomenon, you MUST 'loop back' by creating a new Observation (`.obs`) node linked to that interpretation's URI.

## 4. Figure Integration
As dictated by `SOP-VIZ-01`, any visual artifact generated MUST embed its full `bs://` URI as a watermark or legend to ensure the figure is fully self-documenting outside of the project context.
