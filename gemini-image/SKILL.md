---
name: gemini-image
description: Generate images from text prompts using Google Gemini 3.1 Flash Image Preview. Use when a user asks to create, generate, or make an image, picture, photo, illustration, or visual from a description. Also use for requests like "draw me...", "show me...", "create a picture of...", or any image creation task.
---

# Gemini Image Generation

Generate images from text descriptions using Google's **Gemini 3.1 Flash Image Preview** model (codenamed Nano Banana 2), released in early 2026.

This model is **natively multimodal**, meaning it doesn't just "see" images—it is built to generate and edit them with high precision, including advanced text rendering and **subject consistency**.

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
scripts/generate_image.py <prompt> [OPTIONS]
```

**Required:**
- `prompt`: Text description of image to generate

**Options:**
- `--output PATH` or `-o PATH`: Where to save image (default: `gemini-images/image_<timestamp>.png`)
- `--model MODEL` or `-m MODEL`: Gemini model to use (default: `gemini-3.1-flash-image-preview`)
- `--ref IMAGE` or `-r IMAGE`: Reference image path (can be used multiple times for subject consistency/logos)
- `--aspect-ratio RATIO` or `--ar RATIO`: Aspect ratio (e.g., `16:9`, `1:1`, `9:16`)
- `--temperature TEMP` or `-t TEMP`: Generation temperature (0.0-2.0, default: 1.0)

**Supported Aspect Ratios:**
`1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`

## Subject Consistency & Logo Integration

The **Subject Consistency** feature allows the model to "learn" a specific object (like your logo) and place it in different contexts.

### The "Reference Image" Strategy

To make Gemini use a specific logo across different images:

1. **Upload the Logo**: Include your logo as a reference image using `--ref`
2. **Define it clearly**: Give the logo a name in your prompt (e.g., "The [BrandName] Logo")
3. **Specify Placement**: Be exact about where it should go

**Example:**

```bash
scripts/generate_image.py \
  "A photorealistic high-end interior of a modern coffee shop. A barista pouring latte art into a ceramic cup. Incorporate the provided logo onto the side of the ceramic cup as a matte black print. The logo should maintain perfect proportions and the text must be legible. Cinematic lighting, 8k resolution." \
  --ref ./my-logo.png \
  --ar 16:9 \
  --output ./coffee-shop-branded.png
```

### Logo Placement Examples

```bash
# Logo on product label
scripts/generate_image.py \
  "A sleek aluminum water bottle on a wooden desk with natural lighting. The [BrandName] logo is centered on the bottle label with a brushed metal finish." \
  --ref ./logo.png \
  --ar 4:3

# Logo watermarked in corner
scripts/generate_image.py \
  "A professional marketing photo of a modern tech office. Watermark the provided logo in the bottom-right corner with 30% opacity." \
  --ref ./logo.png \
  --ar 16:9

# Logo etched into metal
scripts/generate_image.py \
  "Close-up macro shot of a titanium smartphone case. The [BrandName] logo is laser-etched into the metal with precise detail." \
  --ref ./logo.png \
  --ar 1:1
```

## How to Structure Prompts (Creative Brief Method)

Instead of simple sentences, use a **Creative Brief** structure for best results:

### Poor Prompt
"Make an image of a coffee shop with my logo."

### Better Prompt (Flash Image 3.1 Guideline)

```
[Context/Scene]: A photorealistic, high-end interior of a modern industrial coffee shop with warm lighting and large windows.

[Subject]: A barista pouring latte art into a ceramic cup on a wooden counter.

[Logo Integration]: Incorporate the provided logo image onto the side of the ceramic cup. The logo should look like a matte black print.

[Style]: Cinematic lighting, 8k resolution, shot on a 35mm lens.

[Constraint]: Ensure the text "The Daily Grind" from the logo is perfectly legible.
```

**When calling the script**, combine this into a single prompt string:

```bash
scripts/generate_image.py \
  "A photorealistic, high-end interior of a modern industrial coffee shop with warm lighting and large windows. A barista pouring latte art into a ceramic cup on a wooden counter. Incorporate the provided logo onto the side of the ceramic cup as a matte black print. Cinematic lighting, 8k resolution, shot on a 35mm lens. Ensure the text 'The Daily Grind' from the logo is perfectly legible." \
  --ref ./logo.png \
  --ar 16:9
```

## Prompting Tips

### Be Descriptive and Specific

✅ **Good Prompts:**
- "A futuristic cityscape at night with neon lights reflecting on wet streets, cyberpunk aesthetic"
- "Minimalist logo design for a coffee shop, warm brown tones, simple line art, modern typography"
- "Photo-realistic close-up of fresh strawberries with water droplets, macro photography, shallow depth of field"
- "Professional billboard for a tech company. Place the uploaded logo in the top right corner with a gradient blue background."

❌ **Avoid:**
- "A nice picture" (too vague)
- "A complex scene with 20 different objects" (too complex)
- Not mentioning how/where reference images should be used

### Mention Textures and Details

The model excels at rendering specific materials and finishes:

- **Textures**: etched, printed, neon, brushed metal, matte, glossy, embossed
- **Materials**: wood, metal, fabric, glass, ceramic
- **Lighting**: cinematic, natural, studio, golden hour, backlit
- **Camera**: 35mm lens, macro, wide-angle, portrait mode, 8k resolution

**Example:**

```bash
scripts/generate_image.py \
  "A luxury brand shopping bag made of premium textured paper. The provided logo is embossed in gold foil on the front. Soft studio lighting with subtle shadows. Product photography style." \
  --ref ./brand-logo.png \
  --ar 3:4
```

## Conversational Editing (Iterative Refinement)

If the generated image isn't quite right, you can refine it by:

1. Describing what to change in a new prompt
2. Referencing the previous output as a reference image
3. Being specific about adjustments

**Example workflow:**

```bash
# First generation
scripts/generate_image.py \
  "A modern tech startup office with the provided logo on the wall" \
  --ref ./logo.png \
  --output ./v1.png

# Refine it (if logo placement is off)
scripts/generate_image.py \
  "Take the provided office image. Move the logo 20% to the left and make it 30% larger. Keep everything else the same." \
  --ref ./v1.png \
  --ref ./logo.png \
  --output ./v2.png
```

## Advanced Examples

### Multi-Reference Branding

```bash
# Use both logo and color palette reference
scripts/generate_image.py \
  "Design a professional business card. Use the provided logo in the top-left corner. Match the color scheme from the provided brand palette image. Include contact details placeholder. Modern, clean layout." \
  --ref ./logo.png \
  --ref ./brand-colors.png \
  --ar 3:2
```

### Product Mockup with Consistent Branding

```bash
# T-shirt mockup
scripts/generate_image.py \
  "A white cotton t-shirt flat lay on a wooden background. The provided logo is screen-printed on the chest area, centered, approximately 4 inches wide. The print should look slightly vintage with a soft texture. Natural daylight photography." \
  --ref ./tshirt-logo.png \
  --ar 4:5

# Coffee mug mockup
scripts/generate_image.py \
  "A white ceramic coffee mug on a breakfast table with morning light. The provided logo wraps around the mug as a full-color print. Steam rising from hot coffee inside. Cozy, lifestyle photography aesthetic." \
  --ref ./mug-logo.png \
  --ar 1:1
```

### Social Media Graphics

```bash
# Instagram post with brand consistency
scripts/generate_image.py \
  "Create an Instagram post design. Abstract geometric background in teal and coral gradients. The provided logo in the top-right corner (white version). Text space reserved in center. Modern, minimal, on-brand aesthetic." \
  --ref ./logo-white.png \
  --ar 1:1

# LinkedIn banner
scripts/generate_image.py \
  "Professional LinkedIn banner for a tech company. Subtle abstract circuit board pattern in dark blue and silver. The provided logo positioned in the left third of the image. Clean, corporate, futuristic vibe." \
  --ref ./company-logo.png \
  --ar 21:9
```

## Summary Checklist for Success

When generating images with logos/branding:

- ✅ **Be Descriptive**: Mention textures (etched, printed, neon)
- ✅ **Use Reference Images**: Don't just describe the logo; show it with `--ref`
- ✅ **Specify Aspect Ratio**: Use `--ar` for proper dimensions
- ✅ **Specify Placement**: "centered on label", "top-right corner", "chest area"
- ✅ **Specify Style**: "matte black print", "embossed gold", "laser-etched"
- ✅ **Iterate**: If slightly off, use conversational editing with previous output as reference

## Output Directory

By default, images are saved to `gemini-images/` in the agent's current working directory (typically their workspace). The directory is created automatically if it doesn't exist.

Files are named with timestamps: `image_YYYYMMDD_HHMMSS.png`

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
- Reference image not found
- Unsupported aspect ratio
- Network connectivity issues
- Rate limiting

## Integration Example

Use from Python code:

```python
import subprocess
import json

result = subprocess.run([
    'scripts/generate_image.py',
    'A beautiful sunset over mountains with the company logo watermarked in the corner',
    '--ref', './logo.png',
    '--ar', '16:9',
    '--output', './branded-sunset.png'
], capture_output=True, text=True)

response = json.loads(result.stdout)
if response['success']:
    print(f"Image saved to: {response['path']}")
else:
    print(f"Error: {response['error']}")
```

## Notes

- Generated images are typically 1408×768 PNG files (~1-3 MB) depending on aspect ratio
- Generation takes 5-15 seconds depending on prompt complexity
- Images consume ~2520 tokens per generation
- Reference images add additional token cost based on resolution
- The model excels at precise text rendering—perfect for logos with text
- Subject consistency works best with clean, high-contrast reference images
