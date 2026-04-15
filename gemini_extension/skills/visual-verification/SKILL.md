<activated_skill>
<instructions>
You are an expert multimodal QA agent. When you activate this skill, you are required to perform a physical inspection of generated visual artifacts.

1. **Trigger:** You generated a `.png`, `.jpg`, `.pdf`, or `.svg` file.
2. **Action:** Use the `read_file` tool to ingest the generated image into your context.
3. **Inspection Checklist:**
   - [ ] Are there any empty subplots?
   - [ ] Is there any overlapping or truncated text (axis labels, titles, tick marks)?
   - [ ] Does the legend obscure the data?
   - [ ] Is the Broadstore `bs://` provenance URI or DEV-ID clearly visible?
4. **Resolution:** If the image fails ANY of these checks, you must rewrite the plotting code (e.g., adjusting `figsize`, `bbox_inches='tight'`, or legend placement) and regenerate the plot.
5. **Finality:** Do not consider the plotting task complete until you have successfully "looked" at a flawless image.
</instructions>
</activated_skill>
