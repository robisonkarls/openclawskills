# Logo Branding Workflow Guide

Practical workflows for maintaining brand consistency across generated images using Gemini 3.1 Flash Image.

## Setup: Prepare Your Brand Assets

### 1. Logo Files

Create a `brand-assets/` directory in your workspace:

```bash
mkdir -p brand-assets/logos
```

**Recommended formats:**

- **Primary Logo** (full color): `logo-color.png` (1024x1024px, transparent background)
- **White Version**: `logo-white.png` (for dark backgrounds)
- **Black Version**: `logo-black.png` (for light backgrounds)
- **Icon Only**: `logo-icon.png` (if your logo has icon + text, save icon separately)

**Quality requirements:**
- PNG format with transparency
- At least 512x512px (1024x1024px ideal)
- Clean edges, no compression artifacts
- Exported from vector source (Illustrator, Figma, etc.)

### 2. Brand Colors Reference

Create a visual color palette reference:

```bash
# Save your brand colors as a reference image
brand-assets/colors/palette.png
```

This can be a simple image with color swatches labeled with hex codes.

### 3. Style Guide Reference

Optional but helpful for consistent aesthetic:

```bash
brand-assets/style/
├── photography-style.jpg    # Reference for photo style
├── texture-reference.jpg    # Materials/textures you use
└── layout-examples.png      # Composition preferences
```

## Workflow 1: Product Mockups

### Goal: Generate product photos with your logo consistently placed

**Example: Coffee Mug**

```bash
scripts/generate_image.py \
  "A white ceramic coffee mug on a wooden breakfast table with morning sunlight. The provided logo is printed on the mug surface, centered, as a full-color glossy print approximately 3 inches wide. Steam rising from hot coffee inside. Warm, inviting lifestyle photography with shallow depth of field." \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 4:5 \
  --output ./product-mockups/mug-001.png
```

**Variations:**

```bash
# T-shirt mockup
scripts/generate_image.py \
  "A premium heather gray t-shirt flat lay on rustic wood planks. The provided logo is screen-printed on the chest, centered, approximately 4 inches wide with a soft vintage texture. Natural daylight, top-down photography." \
  --ref ./brand-assets/logos/logo-black.png \
  --ar 1:1 \
  --output ./product-mockups/tshirt-gray.png

# Laptop sticker
scripts/generate_image.py \
  "Close-up of a MacBook Pro lid. The provided logo is a die-cut vinyl sticker, placed in the top-right corner, 3x3 inches, matte finish. Clean minimal aesthetic, soft studio lighting." \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 16:9 \
  --output ./product-mockups/laptop-sticker.png
```

## Workflow 2: Social Media Graphics

### Goal: Create on-brand social media content

**Instagram Post (1:1)**

```bash
scripts/generate_image.py \
  "Modern Instagram post design. Abstract gradient background transitioning from deep purple to coral pink. The provided logo in white positioned in the top-right corner, 150px wide. Text space reserved in center (blank area). Minimalist, trendy aesthetic with subtle grain texture." \
  --ref ./brand-assets/logos/logo-white.png \
  --ar 1:1 \
  --temperature 0.5 \
  --output ./social-media/instagram-template-001.png
```

**Instagram Story (9:16)**

```bash
scripts/generate_image.py \
  "Instagram Story frame. Vertical layout with blurred lifestyle background (soft focus cafe interior). The provided logo watermarked at top center, small (100px wide), 40% opacity. Clean space in middle third for overlay text. Modern, professional aesthetic." \
  --ref ./brand-assets/logos/logo-white.png \
  --ar 9:16 \
  --output ./social-media/story-template-001.png
```

**LinkedIn Banner (21:9)**

```bash
scripts/generate_image.py \
  "Professional LinkedIn banner for a tech company. Abstract background with subtle circuit board pattern in navy blue and silver tones. The provided logo positioned in the left third of the banner, properly sized for visibility. Clean, corporate, slightly futuristic aesthetic. Ensure logo text is sharp and legible." \
  --ref ./brand-assets/logos/logo-white.png \
  --ar 21:9 \
  --output ./social-media/linkedin-banner.png
```

**YouTube Thumbnail (16:9)**

```bash
scripts/generate_image.py \
  "YouTube thumbnail design. High-contrast background with bold geometric shapes in brand colors. The provided logo in bottom-right corner, sized at 200px wide. Large text space reserved in center and left side. Eye-catching, click-worthy aesthetic with slight 3D depth." \
  --ref ./brand-assets/logos/logo-color.png \
  --ref ./brand-assets/colors/palette.png \
  --ar 16:9 \
  --temperature 0.6 \
  --output ./social-media/youtube-thumb-template.png
```

## Workflow 3: Marketing Materials

### Goal: Professional marketing assets with consistent branding

**Business Card**

```bash
scripts/generate_image.py \
  "Professional business card design, front side. The provided logo positioned in top-left corner, 0.75 inches wide. Clean white background. Contact details area reserved (blank) in bottom-right. Minimalist, modern corporate design. Include subtle embossed texture effect." \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 3:2 \
  --temperature 0.3 \
  --output ./marketing/business-card-front.png
```

**Presentation Slide Background**

```bash
scripts/generate_image.py \
  "PowerPoint presentation slide background. Subtle gradient from light gray to white, left to right. The provided logo watermarked in bottom-right corner, 120px wide, 15% opacity. Clean, professional, minimal distraction. Content area (center) kept clear." \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 16:9 \
  --output ./marketing/slide-background.png
```

**Email Header**

```bash
scripts/generate_image.py \
  "Email newsletter header design. Width 600px. Gradient background using brand colors from the provided palette. The provided logo centered, 250px wide, with subtle drop shadow. Professional, modern, email-optimized design." \
  --ref ./brand-assets/logos/logo-white.png \
  --ref ./brand-assets/colors/palette.png \
  --ar 8:1 \
  --output ./marketing/email-header.png
```

**Trade Show Banner**

```bash
scripts/generate_image.py \
  "Vertical trade show banner design, 2ft x 6ft proportions. Bold background with dynamic abstract shapes in brand colors. The provided logo prominently displayed in top third, large and centered. Space for key messaging in middle section (blank area). Professional, attention-grabbing conference aesthetic." \
  --ref ./brand-assets/logos/logo-white.png \
  --ref ./brand-assets/colors/palette.png \
  --ar 2:3 \
  --temperature 0.5 \
  --output ./marketing/tradeshow-banner.png
```

## Workflow 4: Packaging Design

### Goal: Product packaging with brand elements

**Box Design**

```bash
scripts/generate_image.py \
  "Product box design mockup. Premium white cardboard box, 6x6x4 inches. The provided logo on the top face, centered, as a matte black print with spot UV coating for subtle shine. Minimalist, luxury aesthetic. Soft studio lighting showing box depth and texture." \
  --ref ./brand-assets/logos/logo-black.png \
  --ar 1:1 \
  --output ./packaging/box-top.png
```

**Label Design**

```bash
scripts/generate_image.py \
  "Circular product label, 3 inch diameter. The provided logo at top of circle, 1 inch wide. Cream background with subtle texture. Space for product name and details in center (blank). Vintage-modern aesthetic with clean typography." \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 1:1 \
  --temperature 0.4 \
  --output ./packaging/label-round.png
```

## Workflow 5: Iterative Refinement

### Goal: Refine generated images that are almost perfect

**Step 1: Generate initial version**

```bash
scripts/generate_image.py \
  "A modern office interior with the provided company logo on the wall behind the reception desk" \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 16:9 \
  --output ./iterations/office-v1.png
```

**Step 2: Review and identify issues**
- Logo too small?
- Logo placement off?
- Wrong color/finish?

**Step 3: Refine with specific instructions**

```bash
scripts/generate_image.py \
  "Take the provided office image. Make the logo on the wall 50% larger and move it 10 inches to the left so it's more centered above the desk. Change the logo to have a brushed metal finish instead of painted. Keep all other elements exactly the same." \
  --ref ./iterations/office-v1.png \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 16:9 \
  --temperature 0.3 \
  --output ./iterations/office-v2.png
```

**Step 4: Fine-tune details**

```bash
scripts/generate_image.py \
  "Adjust the provided image: add subtle LED backlighting to the logo on the wall with a soft white glow. Everything else stays the same." \
  --ref ./iterations/office-v2.png \
  --ref ./brand-assets/logos/logo-color.png \
  --ar 16:9 \
  --temperature 0.2 \
  --output ./iterations/office-v3.png
```

**Pro tip:** Lower temperature (0.2-0.4) for refinement to minimize unwanted changes.

## Workflow 6: Batch Generation

### Goal: Create multiple variations efficiently

**Create a batch script:**

```bash
#!/bin/bash
# batch-generate-mockups.sh

LOGO="./brand-assets/logos/logo-color.png"
OUTPUT_DIR="./batch-mockups"
mkdir -p "$OUTPUT_DIR"

# Array of products and prompts
declare -a products=(
  "mug|A white ceramic mug with the logo centered|4:5"
  "tshirt|A black t-shirt with the logo on chest|1:1"
  "tote|A canvas tote bag with large logo print|4:5"
  "cap|A baseball cap with embroidered logo|3:2"
  "notebook|A hardcover notebook with foil logo|3:4"
)

# Generate each
for item in "${products[@]}"; do
  IFS='|' read -r name prompt ratio <<< "$item"
  
  echo "Generating $name..."
  
  scripts/generate_image.py \
    "$prompt. Professional product photography, clean white background, soft studio lighting." \
    --ref "$LOGO" \
    --ar "$ratio" \
    --output "$OUTPUT_DIR/${name}.png"
  
  # Small delay to respect rate limits
  sleep 2
done

echo "Batch generation complete!"
```

**Run it:**

```bash
chmod +x batch-generate-mockups.sh
./batch-generate-mockups.sh
```

## Advanced Tips

### Multi-Logo Scenarios

Some brands use different logo variations for different contexts. Handle this with clear naming:

```bash
brand-assets/logos/
├── primary-color.png          # Main full-color logo
├── primary-white.png          # White version
├── primary-black.png          # Black version
├── icon-only-color.png        # Just the icon
├── wordmark-color.png         # Just the text
└── secondary-badge.png        # Alternative badge version
```

**When to use which:**

- **primary-color**: Most product mockups, light backgrounds
- **primary-white**: Dark backgrounds, overlays, watermarks
- **primary-black**: Minimal designs, monochrome contexts
- **icon-only**: Small spaces (favicons, app icons, profile pics)
- **wordmark**: Horizontal spaces, headers, footers

### Color Palette Matching

To ensure generated backgrounds match your brand colors:

```bash
# Create a palette reference image first
scripts/generate_image.py \
  "Create a color swatch palette showing these exact colors: deep navy blue #1a2b4a, coral pink #ff6b6b, cream white #f4f1ea, and sage green #8fa888. Display as 4 large horizontal bars with hex codes labeled." \
  --ar 16:9 \
  --output ./brand-assets/colors/palette.png

# Then use it in future generations
scripts/generate_image.py \
  "Abstract background for Instagram post using the exact colors from the provided palette reference. Modern gradient design." \
  --ref ./brand-assets/colors/palette.png \
  --ar 1:1 \
  --output ./social-media/bg-branded.png
```

### Maintaining Consistency Across Sessions

Create a `brand-context.txt` file with your standard instructions:

```bash
cat > brand-assets/brand-context.txt << 'EOF'
Brand: [Your Company Name]
Logo file: brand-assets/logos/logo-color.png
Color palette: Deep navy #1a2b4a, Coral pink #ff6b6b, Cream #f4f1ea
Photography style: Clean, minimal, soft natural lighting
Typography: Modern sans-serif, clean and readable
Overall vibe: Professional yet approachable, modern, trustworthy
EOF
```

Then reference this context in prompts:

```bash
BRAND_CONTEXT=$(cat brand-assets/brand-context.txt)

scripts/generate_image.py \
  "$BRAND_CONTEXT. Generate a LinkedIn post image featuring the logo and matching brand colors." \
  --ref ./brand-assets/logos/logo-color.png \
  --ref ./brand-assets/colors/palette.png \
  --ar 1:1
```

## Quality Checklist

Before considering a generated image complete:

- [ ] Logo is legible and sharp
- [ ] Logo colors match brand guidelines
- [ ] Logo size is appropriate for context
- [ ] Logo placement follows brand standards
- [ ] No distortion or stretching of logo
- [ ] Text in logo is perfectly readable
- [ ] Background doesn't compete with logo
- [ ] Overall composition is balanced
- [ ] Image resolution is sufficient for use case
- [ ] Matches brand aesthetic and tone

## Troubleshooting Common Issues

### Issue: Logo colors look washed out

**Solution:**
```bash
# Add color specification to prompt
scripts/generate_image.py \
  "... The logo must maintain exact RGB colors from reference: no color shifts, washes, or tints. Preserve original logo colors perfectly." \
  --ref ./logo.png \
  --temperature 0.3
```

### Issue: Logo gets creative interpretation

**Solution:**
```bash
# Emphasize exact reproduction
scripts/generate_image.py \
  "... Use the provided logo exactly as shown in the reference image. Do not modify, stylize, or reinterpret the logo design. It should be a pixel-perfect reproduction." \
  --ref ./logo.png \
  --temperature 0.2
```

### Issue: Logo text is blurry

**Solution:**
```bash
# Request higher sharpness and larger size
scripts/generate_image.py \
  "... The logo should be rendered at high resolution with crisp, sharp text. All letterforms must be perfectly legible at 100% zoom. Minimum logo width: 400px." \
  --ref ./logo.png
```

### Issue: Background too busy, logo gets lost

**Solution:**
```bash
# Simplify background and add contrast
scripts/generate_image.py \
  "... Use a simple, clean background that doesn't compete with the logo. Ensure high contrast between logo and background. The logo should be the focal point." \
  --ref ./logo.png
```

## Organizing Your Output

Recommended directory structure:

```
workspace/
├── brand-assets/
│   ├── logos/
│   ├── colors/
│   └── style/
├── gemini-images/          # Default output (timestamped)
├── product-mockups/        # Organized by category
├── social-media/
│   ├── instagram/
│   ├── linkedin/
│   └── youtube/
├── marketing/
│   ├── print/
│   └── digital/
├── packaging/
└── iterations/             # Refinement versions
```

This keeps everything organized and easy to find later.
