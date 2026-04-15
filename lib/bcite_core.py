import requests
import fitz  # PyMuPDF
import uuid
import tempfile
from pathlib import Path

def get_paper_uuid(doi):
    """Generates a deterministic UUID v5 for a paper based on its DOI."""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, doi))

def resolve_doi_to_url(doi, email="djproc_bcite_dev@gmail.com"):
    """
    Uses the Unpaywall API to find a free full-text URL for a given DOI.
    """
    url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            best_oa_location = data.get("best_oa_location", {})
            if best_oa_location:
                return {
                    "pdf_url": best_oa_location.get("url_for_pdf"),
                    "html_url": best_oa_location.get("url_for_landing_page") or best_oa_location.get("url"),
                    "title": data.get("title"),
                    "journal": data.get("journal_name"),
                    "published_date": data.get("published_date"),
                    "is_oa": data.get("is_oa"),
                    "uuid": get_paper_uuid(doi)
                }
    except Exception as e:
        print(f"Error connecting to Unpaywall: {e}")
    return None

def fetch_metadata_crossref(doi):
    """
    Fetches detailed publication metadata from Crossref.
    """
    url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get("message", {})
        
        title = data.get("title", ["Unknown Title"])[0]
        authors = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in data.get("author", [])]
        journal = data.get("container-title", ["Preprint / Unknown"])[0]
        year = data.get("issued", {}).get("date-parts", [[None]])[0][0]
        
        return {
            "title": title,
            "authors": authors,
            "journal": journal,
            "year": year,
            "abstract": data.get("abstract", "")
        }
    except Exception as e:
        print(f"Failed to fetch Crossref metadata for {doi}: {e}")
    return None

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF, organized by page.
    """
    doc = fitz.open(pdf_path)
    content = []
    for i, page in enumerate(doc):
        text = page.get_text("text").strip()
        if text:
            content.append({
                "page": i + 1,
                "text": text
            })
    return content

def download_pdf(url):
    """
    Downloads a PDF to a temporary file.
    """
    try:
        response = requests.get(url, stream=True, timeout=20)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            for chunk in response.iter_content(chunk_size=8192):
                tmp.write(chunk)
            return Path(tmp.name)
    except Exception as e:
        print(f"Failed to download PDF: {e}")
    return None
