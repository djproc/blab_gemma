import uuid
import re

class BroadstoreURI:
    """
    Handles the generation and parsing of 'bs://' provenance URIs to track 
    the scientific method: Project -> Obs -> Hypoth -> Test -> Result -> Interpretation.
    """
    def __init__(self, project_id, obs_id=None, hypoth_id=None, test_id=None, result_id=None, interp_id=None):
        self.project_id = self._sanitize(project_id)
        self.obs_id = self._sanitize(obs_id) if obs_id else None
        self.hypoth_id = self._sanitize(hypoth_id) if hypoth_id else None
        self.test_id = self._sanitize(test_id) if test_id else None
        self.result_id = self._sanitize(result_id) if result_id else None
        self.interp_id = self._sanitize(interp_id) if interp_id else None

    @staticmethod
    def _sanitize(value):
        """Sanitizes names to be URL-safe (no spaces or special chars)."""
        if not value: return None
        return re.sub(r'[^a-zA-Z0-9-]', '-', str(value).lower())

    @staticmethod
    def generate_short_uuid():
        """Generates an 8-character UUID for clean URIs."""
        return str(uuid.uuid4())[:8]

    def build(self):
        """Builds the full bs:// URI string based on current state."""
        uri = f"bs://{self.project_id}"
        if self.obs_id:
            uri += f".obs({self.obs_id})"
        if self.hypoth_id:
            uri += f".hypoth({self.hypoth_id})"
        if self.test_id:
            uri += f".test({self.test_id})"
        if self.result_id:
            uri += f".result({self.result_id})"
        if self.interp_id:
            uri += f".interp({self.interp_id})"
        return uri

    def format_markdown_block(self, obs_text="", hypoth_text="", test_text="", result_text="", interp_text=""):
        """Generates the standardized Broadstore markdown output block."""
        return f"""
**[{self.build()}]**
*   **Observation:** {obs_text or "(The empirical trigger)"}
*   **Hypothesis:** {hypoth_text or "(The logical proposition)"}
*   **Test:** {test_text or "(The execution details)"}
*   **Result:** {result_text or "(Raw metrics/findings)"}
*   **Interpretation:** {interp_text or "(Scientific/Operational meaning)"}
"""

def generate_new_node(project, parent_uri=None, node_type="obs", nickname="node"):
    """
    Helper to quickly generate a new downstream node in the bs:// hierarchy.
    Example: generate_new_node("midas", parent_uri="bs://midas.obs(xyz)", node_type="hypoth", nickname="kras-dependency")
    """
    short_id = f"{nickname}--{BroadstoreURI.generate_short_uuid()}"
    
    # In a full deployment, this would ping the FastAPI semantic gateway (broadstore_api).
    # Locally, it generates valid schema paths.
    
    # Basic routing based on parent_uri
    uri = BroadstoreURI(project)
    if parent_uri:
        if ".obs" in parent_uri: uri.obs_id = re.search(r'\.obs\((.*?)\)', parent_uri).group(1)
        if ".hypoth" in parent_uri: uri.hypoth_id = re.search(r'\.hypoth\((.*?)\)', parent_uri).group(1)
        if ".test" in parent_uri: uri.test_id = re.search(r'\.test\((.*?)\)', parent_uri).group(1)
        if ".result" in parent_uri: uri.result_id = re.search(r'\.result\((.*?)\)', parent_uri).group(1)

    # Attach the new node
    setattr(uri, f"{node_type}_id", short_id)
    return uri
