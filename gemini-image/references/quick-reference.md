# Gemini Image Skill - Quick Reference

## Command Structure

```bash
scripts/generate_image.py "<prompt>" [OPTIONS]
```

## Essential Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--output PATH` | `-o` | Save location | `-o ./my-image.png` |
| `--ref IMAGE` | `-r` | Reference image (logo) | `--ref ./logo.png` |
| `--aspect-ratio RATIO` | `--ar` | Image dimensions | `--ar 16:9` |
| `--temperature TEMP` | `-t` | Creativity (0.0-2.0) | `-t 0.5` |
| `--model MODEL` | `-m` | Gemini model | `-m gemini-3.1-flash-image-preview` |

## Aspect Ratios

| Ratio | Type | Use Case |
|-------|------|----------|
| `1:1` | Square | Instagram, profile pics |
| `16:9` | Landscape | YouTube, presentations |
| `9:16` | Portrait | Stories, mobile |
| `4:5` | Portrait | Instagram feed |
| `21:9` | Ultra-wide | Banners, headers |

## Temperature Guide

| Range | Effect | Use For |
|-------|--------|---------|
| 0.2-0.4 | Very consistent | Logo refinement, brand consistency |
| 0.5-0.7 | Balanced | General use, product mockups |
| 0.8-1.2 | Creative (default) | Artistic, varied outputs |
| 1.3-2.0 | Highly varied | Experimental, abstract |

## Quick Commands

### Basic Image
```bash
scripts/generate_image.py "A serene mountain landscape at sunset"
```

### With Logo (Subject Consistency)
```bash
scripts/generate_image.py \
  "A coffee mug with the provided logo centered" \
  --ref ./my-logo.png \
  --ar 4:5
```

### Full Control
```bash
scripts/generate_image.py \
  "Professional product photo with logo placement" \
  --ref ./logo.png \
  --ar 16:9 \
  --temperature 0.4 \
  --output ./products/final.png
```

### Multiple References (Logo + Color Palette)
```bash
scripts/generate_image.py \
  "Instagram post using brand colors" \
  --ref ./logo.png \
  --ref ./palette.png \
  --ar 1:1
```

## Prompt Structure (Best Results)

```
[Scene/Context]: <detailed scene description>
[Subject]: <main elements>
[Logo Integration]: <how/where reference image appears>
[Style]: <aesthetic, lighting, quality>
[Constraints]: <specific requirements>
```

**Example:**
```bash
scripts/generate_image.py \
  "Scene: Modern tech office with natural lighting. Subject: Reception desk with computer. Logo Integration: Company logo on wall behind desk, brushed metal finish, 4ft wide, centered. Style: Professional architecture photography, 8k. Constraints: Logo text must be sharp and legible." \
  --ref ./company-logo.png \
  --ar 16:9
```

## Logo Integration Checklist

- ✅ Include `--ref` with high-res logo (1024x1024px PNG recommended)
- ✅ Mention logo explicitly in prompt ("the provided logo...")
- ✅ Specify placement ("centered", "top-right corner", "on the label")
- ✅ Describe style ("matte print", "embossed", "laser-etched")
- ✅ Mention size/scale if critical
- ✅ Add constraint for text legibility if logo contains text
- ✅ Use lower temperature (0.3-0.5) for consistent branding

## Common Patterns

### Product Mockup
```bash
scripts/generate_image.py \
  "<product> on white background. The provided logo <where/how>. Professional product photography, soft lighting." \
  --ref ./logo.png \
  --ar 4:5
```

### Social Media Post
```bash
scripts/generate_image.py \
  "<background>. The provided logo in <corner>, <size>. Text space in center. <vibe>." \
  --ref ./logo.png \
  --ar 1:1
```

### Marketing Material
```bash
scripts/generate_image.py \
  "<material type>. The provided logo <placement>. <brand colors/style>. Professional, print-ready." \
  --ref ./logo.png \
  --ref ./palette.png \
  --ar <appropriate>
```

## Iterative Refinement

**First attempt:**
```bash
scripts/generate_image.py \
  "Initial description" \
  --ref ./logo.png \
  --output ./v1.png
```

**Refine:**
```bash
scripts/generate_image.py \
  "Adjust the provided image: make logo 30% larger and move it left. Keep everything else the same." \
  --ref ./v1.png \
  --ref ./logo.png \
  --temperature 0.3 \
  --output ./v2.png
```

**Key:** Lower temperature + reference previous version + be specific about changes.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Logo not appearing | Mention it explicitly in prompt: "Incorporate the provided logo..." |
| Logo colors wrong | Add: "Maintain exact RGB colors from reference" + lower temperature |
| Logo blurry/illegible | Specify size: "at least 400px wide" + add "sharp, legible text" |
| Background too busy | "Simple clean background, high contrast with logo" |
| Inconsistent across images | Use same reference image + lower temperature (0.3-0.5) |

## File Organization

```
workspace/
├── brand-assets/
│   ├── logos/
│   │   ├── logo-color.png      # Main logo
│   │   ├── logo-white.png      # Dark backgrounds
│   │   └── logo-black.png      # Light backgrounds
│   └── colors/
│       └── palette.png         # Color reference
├── gemini-images/              # Default output
├── product-mockups/
├── social-media/
└── marketing/
```

## Documentation

- **SKILL.md** - Full skill documentation with all features
- **references/api-reference.md** - Technical API details
- **references/branding-workflows.md** - Step-by-step branding workflows
- **references/examples.md** - Real-world practical examples
- **references/quick-reference.md** - This file (quick lookup)

## Getting Help

```bash
# Show this quick reference
cat references/quick-reference.md

# Full documentation
cat SKILL.md

# API details
cat references/api-reference.md

# Practical examples
cat references/examples.md

# Branding workflows
cat references/branding-workflows.md
```

## Tips

1. **Prepare assets first** - Have high-res logos ready before generating
2. **Start simple** - Get basic composition right, then refine
3. **Document successes** - Save commands that work well
4. **Batch similar tasks** - Generate multiple variations efficiently
5. **Use references** - Previous successful outputs make great style guides
6. **Lower temp for brands** - Consistency matters more than creativity
7. **Iterate** - Don't expect perfection on first try
