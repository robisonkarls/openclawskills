---
name: gemini-image
description: Generate images from text prompts using Google Gemini 3.1 Flash Image Preview. Use when a user asks to create, generate, or make an image, picture, photo, illustration, or visual from a description. Also use for requests like "draw me...", "show me...", "create a picture of...", or any image creation task.
---

# Gemini Image Generation

Generate images from text descriptions using Google's Gemini 3.1 Flash Image Preview model.

## Prerequisites

Gemini API key must be configured in one of:
- `~/.gemini/settings.json` (preferred)
- `GEMINI_API_KEY` environment variable

To check if configured:
```bash
cat ~/.gemini/settings.json
```

## Quick Start

Generate an image from a prompt:

```bash
scripts/generate_image.py "A cute robot assistant working at a desk"
```

Images are automatically saved to `gemini-images/<timestamp>.png` in the current working directory (typically the agent's workspace).

The script returns JSON with image details:
```json
{
  "success": true,
  "path": "/Users/autobot/.openclaw/workspace/gemini-images/image_20260311_183000.png",
  "dimensions": "1408 x 768",
  "size_bytes": 1782340,
  "model": "gemini-3.1-flash-image-preview"
}
```

## Usage

```bash
scripts/generate_image.py <prompt> [output_path] [model]
```

**Arguments:**
- `prompt` (required): Text description of image to generate
- `output_path` (optional): Where to save image (default: `gemini-images/image_<timestamp>.png` in current directory)
- `model` (optional): Gemini model to use (default: `gemini-3.1-flash-image-preview`)

**Examples:**

```bash
# Basic usage (saves to gemini-images/image_<timestamp>.png)
scripts/generate_image.py "A serene mountain landscape at sunset"

# Specify custom output path
scripts/generate_image.py "A minimalist tech logo" ./custom-folder/logo.png

# Custom model
scripts/generate_image.py "Portrait of a cat" ./cat.png gemini-3.1-flash-image-preview
```

## Output Directory

By default, images are saved to `gemini-images/` in the agent's current working directory (typically their workspace). The directory is created automatically if it doesn't exist.

Files are named with timestamps: `image_YYYYMMDD_HHMMSS.png`

## Prompting Tips

Write descriptive, specific prompts:

✅ **Good:**
- "A futuristic cityscape at night with neon lights reflecting on wet streets"
- "Minimalist logo design for a coffee shop, warm brown tones, simple line art"
- "Photo-realistic close-up of fresh strawberries with water droplets"

❌ **Avoid:**
- "A nice picture" (too vague)
- "A complex scene with 20 different objects" (too complex)

## Advanced Features

For detailed API specifications, model options, and troubleshooting:

```bash
cat references/api-reference.md
```

## Error Handling

The script returns JSON with `success: false` on errors:

```json
{
  "success": false,
  "error": "No Gemini API key found. Set GEMINI_API_KEY or configure ~/.gemini/settings.json"
}
```

Common errors:
- Missing API key
- Invalid prompt (content policy violation)
- Network connectivity issues
- Rate limiting

## Integration Example

Use from Python code:

```python
import subprocess
import json

result = subprocess.run([
    'scripts/generate_image.py',
    'A beautiful sunset over mountains',
    './output.png'
], capture_output=True, text=True)

response = json.loads(result.stdout)
if response['success']:
    print(f"Image saved to: {response['path']}")
else:
    print(f"Error: {response['error']}")
```

## Notes

- Generated images are typically 1408×768 PNG files (~1-3 MB)
- Generation takes 5-15 seconds depending on prompt complexity
- Images consume ~2520 tokens per generation
- Supported aspect ratios: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
