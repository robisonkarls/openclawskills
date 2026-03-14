# Gemini Image Generation Skill

Professional image generation using Google Gemini 3.1 Flash Image Preview with advanced **subject consistency** and **logo integration** capabilities.

## What's New

This skill now supports:

✨ **Subject Consistency** - Maintain logos, icons, and brand elements consistently across different images  
🎨 **Multi-Reference Input** - Use logo + color palette + style references together  
📐 **Aspect Ratio Control** - 11 supported ratios for different use cases  
🔧 **Iterative Refinement** - Improve generated images through conversational editing  
🎯 **Temperature Control** - Balance creativity vs consistency for branding  

## Quick Start

### Basic Usage

```bash
# Simple image generation
scripts/generate_image.py "A serene mountain landscape at sunset"
```

### With Logo Integration

```bash
# Product mockup with your logo
scripts/generate_image.py \
  "A white coffee mug on a wooden table. The provided logo is centered on the mug as a matte print." \
  --ref ./my-logo.png \
  --ar 4:5
```

### Advanced Branding

```bash
# Instagram post with brand consistency
scripts/generate_image.py \
  "Instagram post design with gradient background matching the provided color palette. The logo in top-right corner, 150px wide. Modern, clean aesthetic." \
  --ref ./logo.png \
  --ref ./brand-colors.png \
  --ar 1:1 \
  --temperature 0.5
```

## Documentation

| Document | Description |
|----------|-------------|
| **[SKILL.md](SKILL.md)** | Complete skill documentation with all features |
| **[Quick Reference](references/quick-reference.md)** | Fast command lookup and common patterns |
| **[API Reference](references/api-reference.md)** | Technical details, parameters, troubleshooting |
| **[Branding Workflows](references/branding-workflows.md)** | Step-by-step guides for brand consistency |
| **[Examples](references/examples.md)** | Real-world practical examples |

**New to this skill?** Start with [SKILL.md](SKILL.md)  
**Need a quick command?** Check [Quick Reference](references/quick-reference.md)  
**Working on branding?** See [Branding Workflows](references/branding-workflows.md)

## Key Features

### Subject Consistency (The Game-Changer)

The model can "learn" objects from reference images and place them consistently in new contexts:

```bash
# Your logo appears correctly on any product
scripts/generate_image.py "T-shirt with logo on chest" --ref ./logo.png
scripts/generate_image.py "Coffee mug with logo centered" --ref ./logo.png
scripts/generate_image.py "Business card with logo in corner" --ref ./logo.png
```

Same logo, consistently rendered, different contexts. No manual editing required.

### Multi-Reference Input

Combine multiple reference images for complex requirements:

```bash
scripts/generate_image.py \
  "Product photo matching brand aesthetic" \
  --ref ./logo.png \
  --ref ./color-palette.png \
  --ref ./style-reference.jpg
```

The model considers all references when generating.

### Supported Aspect Ratios

- **1:1** - Instagram posts, profile pictures
- **16:9** - YouTube thumbnails, presentations
- **9:16** - Instagram Stories, mobile
- **4:5** - Instagram feed (optimized)
- **21:9** - LinkedIn banners, ultra-wide
- Plus: 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 8:1

### Temperature Control

Control the creativity/consistency balance:

- **0.2-0.4** - Very consistent (best for branding)
- **0.5-0.7** - Balanced (general use)
- **0.8-1.2** - Creative (default, artistic work)
- **1.3-2.0** - Highly varied (experimental)

## Common Use Cases

### Product Mockups
Generate realistic product photos with your logo:
- T-shirts, mugs, notebooks, packaging
- Consistent logo treatment across all products
- Professional e-commerce imagery

### Social Media Graphics
Create on-brand social content:
- Instagram posts/stories with logo watermarks
- YouTube thumbnails with brand elements
- LinkedIn banners with company branding

### Marketing Materials
Professional marketing assets:
- Business cards, brochures, flyers
- Email headers with logo
- Presentation backgrounds
- Trade show banners

### Brand Consistency
Maintain visual identity across:
- Multiple product lines
- Seasonal campaigns
- Various marketing channels
- Different aspect ratios

## Prerequisites

You need a Gemini API key configured at:
- `~/.gemini/settings.json` (recommended), or
- `GEMINI_API_KEY` environment variable

Get your API key: https://aistudio.google.com/app/apikey

## Installation

This skill is pre-installed in OpenClaw. The script is ready to use at:
```
~/.openclaw/workspace/skills/gemini-image/scripts/generate_image.py
```

## File Organization

Recommended workspace structure:

```
workspace/
├── brand-assets/           # Your logos, colors, style guides
│   ├── logos/
│   │   ├── logo-color.png
│   │   ├── logo-white.png
│   │   └── logo-black.png
│   ├── colors/
│   │   └── palette.png
│   └── style/
│       └── reference.jpg
├── gemini-images/          # Default output directory
├── product-mockups/        # Organized outputs
├── social-media/
│   ├── instagram/
│   ├── linkedin/
│   └── youtube/
└── marketing/
```

## Examples

### Coffee Shop Branding

```bash
# Mug photo
scripts/generate_image.py \
  "Rustic ceramic coffee mug on wooden table with morning light. The provided logo printed on mug, matte brown finish, centered. Cozy cafe aesthetic." \
  --ref ./coffee-logo.png --ar 4:5 --output ./cafe-mug.png

# Instagram post
scripts/generate_image.py \
  "Instagram post with warm brown gradient. Logo in top-right, white, 150px. Text space in center. Inviting coffee shop vibe." \
  --ref ./coffee-logo.png --ar 1:1 --output ./insta-template.png
```

### Tech Startup Assets

```bash
# LinkedIn banner
scripts/generate_image.py \
  "Professional LinkedIn banner with abstract tech shapes in brand colors. Logo in left third, white version. Modern, innovative aesthetic." \
  --ref ./startup-logo.png --ref ./brand-colors.png --ar 21:9

# App icon
scripts/generate_image.py \
  "iOS app icon, simplified version of provided logo optimized for small sizes. Bold, recognizable. Apple design guidelines." \
  --ref ./startup-logo.png --ar 1:1 --temp 0.5
```

### E-commerce Product Line

```bash
# Water bottle
scripts/generate_image.py \
  "Stainless steel water bottle, sage green. Logo laser-etched on front, centered, 2 inches wide. Natural background blur. Professional product photo." \
  --ref ./eco-logo.png --ar 4:5

# Packaging
scripts/generate_image.py \
  "Kraft cardboard box with logo printed on lid in green ink, centered, 3 inches wide. Eco-friendly, minimal design." \
  --ref ./eco-logo.png --ar 1:1
```

## Tips for Best Results

1. **High-res logos** - Use at least 512x512px PNG with transparency
2. **Be specific** - Describe exactly where/how logo should appear
3. **Mention materials** - "matte print", "laser-etched", "embossed gold"
4. **Specify size** - "2 inches wide", "150px", "40% of mug surface"
5. **Lower temperature** - Use 0.3-0.5 for brand consistency
6. **Iterate** - Refine imperfect results with follow-up generations
7. **Reference successes** - Use good outputs as style guides for new work

## Troubleshooting

**Logo not appearing?**
- Make sure you mention it in prompt: "The provided logo..."
- Verify `--ref` path is correct

**Colors look wrong?**
- Add: "Maintain exact RGB colors from reference"
- Lower temperature to 0.3-0.4

**Logo is blurry?**
- Specify larger size: "at least 400px wide"
- Add: "sharp, legible text" to prompt

**Inconsistent results?**
- Use same reference file every time
- Lower temperature (0.3-0.5)
- Be more specific in prompt

See [API Reference](references/api-reference.md) for comprehensive troubleshooting.

## Command Reference

```bash
scripts/generate_image.py "<prompt>" [OPTIONS]

Options:
  --output PATH, -o PATH          Save location
  --ref IMAGE, -r IMAGE           Reference image (repeatable)
  --aspect-ratio RATIO, --ar      Aspect ratio (e.g., 16:9)
  --temperature TEMP, -t TEMP     Creativity (0.0-2.0)
  --model MODEL, -m MODEL         Gemini model to use
```

For complete options and examples, see [SKILL.md](SKILL.md).

## Learn More

- **[Full Documentation](SKILL.md)** - Everything you need to know
- **[Quick Reference](references/quick-reference.md)** - Fast command lookup
- **[Branding Guide](references/branding-workflows.md)** - Professional branding workflows
- **[API Details](references/api-reference.md)** - Technical deep dive
- **[Examples](references/examples.md)** - Real-world use cases

## About the Model

**Gemini 3.1 Flash Image Preview** (Nano Banana 2)
- Released: Early 2026
- Native multimodal image generation
- Advanced text rendering in images
- Subject consistency for branding
- Precise control over composition

## Support

Questions or issues?
- Check the documentation files above
- Review [examples.md](references/examples.md) for patterns
- Consult [api-reference.md](references/api-reference.md) for errors

---

**Ready to generate?** Start with a simple command and build from there. The skill grows with you.
