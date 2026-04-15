# SOP-VIZ-01: Automated Visual QC & Formatting

**Objective:** Guarantee that all generated scientific figures are presentation-ready, self-documenting, and free of visual artifacts.

## 1. Zero-Overlap Policy
- Legends, titles, text annotations, and data points MUST NOT overlap. 
- If necessary, place legends outside the plot area (`bbox_to_anchor`).

## 2. Standardized Layouts
- **Slide Graphics:** Optimize aspect ratios for a 4x Canvas (e.g., 2880 x 1620 points for 16:9).
- **Composite Panels:** Use grid layouts (e.g., 2x3 or 4-row) to separate plots from their respective legends, guaranteeing no occlusion.

## 3. Data Provenance Watermarks
- All generated artifacts MUST include a text sidebar, footer, or explicit legend block outlining the `bs://` (Broadstore) URI to ensure it is self-documenting.
- Include the Dev-ID and Generation Timestamp in the figure header.

## 4. Automated & Multimodal QC
- **Multimodal Agents:** Agents MUST use `read_file` to physically view the generated image and check for clipping or unreadable text.
- **Algorithmic QC:** Use bounding-box / IoU checkers if available in the pipeline (e.g., `validate_layout`) before saving the final figure.
