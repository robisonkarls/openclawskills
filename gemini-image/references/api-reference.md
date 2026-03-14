# Gemini 3.1 Flash Image API Reference

## Model Information

**Model ID:** `gemini-3.1-flash-image-preview`  
**Code Name:** Nano Banana 2  
**Release:** Early 2026  
**Capabilities:** Native multimodal image generation and editing

## Key Features

1. **Subject Consistency** - Maintain specific objects (logos, characters) across different contexts
2. **Advanced Text Rendering** - High-quality, legible text in images
3. **Multi-Modal Input** - Accept both text prompts and reference images
4. **Precise Control** - Aspect ratios, temperature, style specifications

## API Endpoint

```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent
```

**Authentication:** API key via query parameter `?key=YOUR_API_KEY`

## Request Format

### Basic Text-to-Image

```json
{
  "contents": [{
    "parts": [{
      "text": "A serene mountain landscape at sunset"
    }]
  }],
  "generationConfig": {
    "temperature": 1.0,
    "topP": 0.95
  }
}
```

### With Reference Images (Subject Consistency)

```json
{
  "contents": [{
    "parts": [
      {
        "inlineData": {
          "mimeType": "image/png",
          "data": "base64_encoded_image_data"
        }
      },
      {
        "text": "Place this logo on a coffee mug, centered, with a matte finish"
      }
    ]
  }],
  "generationConfig": {
    "temperature": 1.0,
    "topP": 0.95,
    "aspectRatio": "1:1"
  }
}
```

### Multiple Reference Images

```json
{
  "contents": [{
    "parts": [
      {
        "inlineData": {
          "mimeType": "image/png",
          "data": "base64_logo_data"
        }
      },
      {
        "inlineData": {
          "mimeType": "image/jpeg",
          "data": "base64_style_reference_data"
        }
      },
      {
        "text": "Create a product photo using the first image as the logo and matching the color palette from the second image"
      }
    ]
  }],
  "generationConfig": {
    "temperature": 1.0,
    "topP": 0.95,
    "aspectRatio": "16:9"
  }
}
```

## Generation Config Parameters

| Parameter | Type | Default | Range/Options | Description |
|-----------|------|---------|---------------|-------------|
| `temperature` | float | 1.0 | 0.0 - 2.0 | Controls randomness. Lower = more deterministic |
| `topP` | float | 0.95 | 0.0 - 1.0 | Nucleus sampling threshold |
| `aspectRatio` | string | - | See below | Output image aspect ratio |

### Supported Aspect Ratios

| Ratio | Orientation | Use Case |
|-------|-------------|----------|
| `1:1` | Square | Social media posts, profile pictures |
| `16:9` | Landscape | Presentations, YouTube thumbnails, banners |
| `9:16` | Portrait | Mobile screens, Instagram Stories |
| `4:3` | Landscape | Standard photo, classic displays |
| `3:4` | Portrait | Portrait photography, posters |
| `21:9` | Ultra-wide | Cinematic, LinkedIn banners |
| `3:2` | Landscape | Standard photography |
| `2:3` | Portrait | Book covers, magazine pages |
| `4:5` | Portrait | Instagram feed (optimized) |
| `5:4` | Portrait | Close to square, product shots |
| `8:1` | Ultra-wide banner | Website headers, panoramic |

## Response Format

### Success Response

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "base64_encoded_image_data"
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "safetyRatings": [...]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 2520,
    "candidatesTokenCount": 0,
    "totalTokenCount": 2520
  }
}
```

### Error Response

```json
{
  "error": {
    "code": 400,
    "message": "Invalid argument: content violates content policy",
    "status": "INVALID_ARGUMENT"
  }
}
```

## Common Error Codes

| Code | Status | Common Causes |
|------|--------|---------------|
| 400 | `INVALID_ARGUMENT` | Content policy violation, invalid parameters |
| 401 | `UNAUTHENTICATED` | Invalid or missing API key |
| 403 | `PERMISSION_DENIED` | API key doesn't have access to model |
| 429 | `RESOURCE_EXHAUSTED` | Rate limit exceeded, quota exhausted |
| 500 | `INTERNAL` | Temporary server error |
| 503 | `UNAVAILABLE` | Service temporarily unavailable |

## Rate Limits & Quotas

**Note:** Actual limits vary by Google Cloud project tier. Check your quota at:
https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas

Typical free tier limits:
- **Requests per minute:** 60
- **Requests per day:** 1,500
- **Tokens per minute:** 1,000,000

## Best Practices

### Reference Image Guidelines

**For best subject consistency:**

1. **High resolution** - At least 512x512px for logos
2. **Clean background** - Solid color or transparent PNG
3. **High contrast** - Logo should be clearly distinguishable
4. **Centered subject** - Main object in center of frame
5. **Proper format** - PNG for transparency, JPEG/WebP also supported

### Prompt Engineering for Logo Integration

**Structure your prompt with clear sections:**

1. **Scene description** - Set the context
2. **Subject details** - Main elements in the image
3. **Logo integration** - Specific instructions for reference image
4. **Style & quality** - Artistic direction, resolution, lighting
5. **Constraints** - Text legibility, size requirements

**Example:**

```
Scene: A modern tech conference booth with minimalist design
Subject: A large display screen showing product features
Logo Integration: Place the provided company logo in the top-right corner of the display screen. The logo should appear as a backlit LED sign with subtle glow.
Style: Professional photography, soft studio lighting, shallow depth of field
Constraints: Ensure the logo maintains exact colors and all text is sharp and legible
```

### Temperature Guidelines

| Temperature | Effect | Best For |
|-------------|--------|----------|
| 0.0 - 0.3 | Very deterministic | Consistent branding, exact reproductions |
| 0.4 - 0.7 | Balanced | General use, product mockups |
| 0.8 - 1.2 | Creative (default) | Artistic images, varied outputs |
| 1.3 - 2.0 | Highly varied | Experimental, abstract art |

**For consistent logo placement:** Use temperature 0.3-0.5

## Subject Consistency Deep Dive

### How It Works

The model analyzes reference images to understand:
- **Shape and geometry** - Logo outline, proportions
- **Colors** - Exact color values, gradients
- **Text elements** - Font characteristics, letterforms
- **Style** - Flat vs 3D, line weight, shadows

It then applies this learned representation to the new context specified in your prompt.

### Multi-Reference Strategy

When providing multiple reference images:

1. **First image** - Primary subject (usually your logo)
2. **Second image** - Style reference (color palette, texture)
3. **Third image** - Context reference (scene composition)

**Order matters** - Images earlier in the `parts` array have higher influence.

### Common Pitfalls

❌ **Vague instructions**
```
"Put my logo somewhere on this"
```

✅ **Specific instructions**
```
"Place the provided logo centered on the product label, sized to 40% of the label width, with 10px padding"
```

❌ **Low-quality reference**
```
Using a 100x100px pixelated logo
```

✅ **High-quality reference**
```
Using a 1024x1024px vector-exported PNG
```

## Access Methods

### 1. Google AI Studio (Web Interface)

**URL:** https://aistudio.google.com/

1. Select `gemini-3.1-flash-image-preview` from model dropdown
2. Enter text prompt
3. Upload reference images (optional)
4. Adjust generation settings
5. Click "Run"

**Pros:** Easy visual interface, no coding required  
**Cons:** Manual workflow, no automation

### 2. Vertex AI (Google Cloud)

**Console:** https://console.cloud.google.com/vertex-ai/studio

Enterprise features:
- Higher quotas and rate limits
- VPC-SC support for data privacy
- Audit logging and compliance
- Custom quotas and SLAs

**Pros:** Enterprise-grade, integrated with GCP  
**Cons:** Requires Google Cloud project, billing

### 3. Gemini API (SDK/CLI)

**Python SDK:**
```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=["Your prompt here"]
)
```

**REST API (curl):**
```bash
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

**Pros:** Programmatic control, automation, CI/CD integration  
**Cons:** Requires API key management, error handling

## Security & Privacy

### API Key Management

**Never commit API keys to version control**

Recommended approaches:
1. Environment variables: `export GEMINI_API_KEY="your-key"`
2. Config files with restricted permissions: `~/.gemini/settings.json` (chmod 600)
3. Secret management: Google Secret Manager, HashiCorp Vault

### Content Policy

The model will reject prompts that:
- Contain violence, gore, or disturbing imagery
- Depict illegal activities
- Include sexually explicit content
- Generate misleading or harmful information
- Infringe on copyrights or trademarks

**For brand logos:** Ensure you have rights to use the logo/trademark in generated content.

### Data Privacy

- **Input data** (prompts & images) may be used to improve Google services unless you opt out
- **Generated images** are not stored by Google after delivery
- **Vertex AI** offers additional privacy controls and data residency options

## Troubleshooting

### Logo Not Appearing

**Possible causes:**
1. Reference image not properly encoded as base64
2. Prompt doesn't mention the reference image
3. Conflicting instructions in prompt

**Solution:**
```bash
# Verify image encoding
base64 -i your-logo.png | head -c 100

# Use explicit instructions
"Incorporate the provided logo image..."
```

### Logo Distorted or Wrong Colors

**Possible causes:**
1. Low-resolution reference image
2. High temperature causing variation
3. Complex background in reference image

**Solution:**
- Use high-res PNG with transparent background
- Lower temperature to 0.3-0.5
- Specify exact colors in prompt: "The logo should maintain exact RGB colors from reference"

### Text in Logo Not Legible

**Possible causes:**
1. Logo too small in final composition
2. Model hallucinating text details
3. Low contrast placement

**Solution:**
- Specify size: "The logo should be at least 200px wide"
- Add constraint: "Ensure all text in the logo is perfectly legible and matches the reference exactly"
- Specify high contrast placement: "Place on solid white background"

### Rate Limit Errors

**Error:** `429 RESOURCE_EXHAUSTED`

**Solutions:**
1. Implement exponential backoff retry logic
2. Cache results when possible
3. Batch operations during off-peak hours
4. Upgrade to higher quota tier

**Exponential backoff example:**
```python
import time

def retry_with_backoff(func, max_retries=5):
    for i in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if i == max_retries - 1:
                raise
            wait = 2 ** i
            time.sleep(wait)
```

## Cost & Token Consumption

**Image generation typically costs:**
- ~2,520 tokens per image (base cost)
- Additional tokens for reference images based on resolution
- Text prompt tokens (minor compared to image generation)

**Example calculation:**
- Base image: 2,520 tokens
- 1024x1024 logo reference: ~400 tokens
- Text prompt (50 words): ~75 tokens
- **Total:** ~2,995 tokens

**Pricing** (as of March 2026, subject to change):
- Check current pricing: https://ai.google.dev/pricing

## Related Resources

- **Official Docs:** https://ai.google.dev/gemini-api/docs
- **AI Studio:** https://aistudio.google.com/
- **Vertex AI:** https://cloud.google.com/vertex-ai
- **Python SDK:** https://github.com/google/generative-ai-python
- **Community:** https://discord.gg/google-ai
