# Adobe Hackathon Round 1A – Intelligent PDF Outline Extractor

## Problem Statement
Extract a hierarchical outline (Title, H1-H3 headings with page numbers) from any PDF (≤ 50 pages) and generate a structured JSON.

## Approach
We used **PyMuPDF** to:
- Parse PDF structure
- Analyze text blocks
- Infer heading levels via **font size heuristics**

## JSON Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Docker Instructions

### Build
```bash
docker build --platform linux/amd64 -t adobe-solution:mytag .
```

### Run
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none adobe-solution:mytag
```

## Constraints Satisfied
- Runtime < 10 seconds
- Model size = 0 MB (no external model used)
- No internet calls
- CPU-only, offline compatible

## Dependencies
- PyMuPDF
