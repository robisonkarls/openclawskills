# Practical Examples - Gemini Image with Subject Consistency

Real-world examples demonstrating logo integration and subject consistency features.

## Example 1: Coffee Shop Branding Suite

**Scenario:** Local coffee shop "The Daily Grind" needs branded marketing materials.

### Setup

```bash
# Prepare logo
cp ~/Downloads/daily-grind-logo.png ./brand-assets/logos/coffee-logo.png
```

### Generate Mug Photo

```bash
scripts/generate_image.py \
  "A rustic ceramic coffee mug in cream color on a weathered wooden table. Morning sunlight streaming through a window creates warm highlights. The provided logo is printed on the mug as a matte brown design, centered and sized to wrap around 40% of the mug circumference. Steam rises from fresh coffee inside. Cozy cafe aesthetic, shallow depth of field, professional food photography." \
  --ref ./brand-assets/logos/coffee-logo.png \
  --ar 4:5 \
  --output ./coffee-shop/mug-photo.png
```

### Generate Instagram Post

```bash
scripts/generate_image.py \
  "Instagram post design for a coffee shop. Warm brown gradient background from espresso to cream tones. The provided logo in the top-right corner, white version, 150px wide. Text space reserved in center (blank area for overlay text). Coffee bean pattern subtly visible in background. Inviting, warm, artisanal aesthetic." \
  --ref ./brand-assets/logos/coffee-logo.png \
  --ar 1:1 \
  --output ./coffee-shop/instagram-template.png
```

### Generate Loyalty Card

```bash
scripts/generate_image.py \
  "Loyalty card design, business card size. The provided logo at top center, 1 inch wide in brown. Cream-colored background with subtle coffee stain texture. Grid of 10 coffee cup icons below for stamps (simple line art). Minimalist, tactile design that feels premium yet approachable." \
  --ref ./brand-assets/logos/coffee-logo.png \
  --ar 3:2 \
  --temperature 0.4 \
  --output ./coffee-shop/loyalty-card.png
```

## Example 2: Tech Startup Product Launch

**Scenario:** "CloudSync" launching a new SaaS product, needs marketing assets.

### Setup

```bash
# Prepare assets
cp ~/Downloads/cloudsync-logo.png ./brand-assets/logos/cloudsync.png
cp ~/Downloads/brand-colors.png ./brand-assets/colors/cloudsync-palette.png
```

### Generate LinkedIn Banner

```bash
scripts/generate_image.py \
  "LinkedIn company banner for a cloud storage startup. Abstract background with floating geometric shapes and subtle cloud motifs in gradient blue tones matching the provided color palette. The provided logo positioned in left third, white version, sized appropriately for LinkedIn specs. Modern, professional, tech-forward aesthetic with sense of connectivity and innovation." \
  --ref ./brand-assets/logos/cloudsync.png \
  --ref ./brand-assets/colors/cloudsync-palette.png \
  --ar 21:9 \
  --output ./cloudsync-launch/linkedin-banner.png
```

### Generate Product Screenshot Mockup

```bash
scripts/generate_image.py \
  "MacBook Pro on a clean white desk with soft shadows. The screen shows a blurred interface (generic dashboard with charts and graphs). The provided logo is visible in the top-left corner of the interface as it would appear in the actual app navigation bar. Professional product photography, soft studio lighting, slight angle to show depth. The laptop should feel premium and the interface modern." \
  --ref ./brand-assets/logos/cloudsync.png \
  --ar 16:9 \
  --output ./cloudsync-launch/laptop-mockup.png
```

### Generate App Icon

```bash
scripts/generate_image.py \
  "iOS app icon design, 1024x1024px. Based on the provided logo, create a simplified icon version optimized for small sizes. Bold, recognizable shape with the key logo element. Use brand colors. Ensure it's distinct and readable at 60x60px. Modern, clean, follows Apple design guidelines. Slight gradient for depth but maintains clarity." \
  --ref ./brand-assets/logos/cloudsync.png \
  --ref ./brand-assets/colors/cloudsync-palette.png \
  --ar 1:1 \
  --temperature 0.5 \
  --output ./cloudsync-launch/app-icon.png
```

### Generate Email Header

```bash
scripts/generate_image.py \
  "Email newsletter header, 600px wide. Clean, professional design with gradient background using brand colors from palette. The provided logo centered, 200px wide. Subtle abstract shapes in background suggesting cloud connectivity. Email-optimized: light file size aesthetic, clear focal point, doesn't overwhelm content below." \
  --ref ./brand-assets/logos/cloudsync.png \
  --ref ./brand-assets/colors/cloudsync-palette.png \
  --ar 8:1 \
  --output ./cloudsync-launch/email-header.png
```

## Example 3: E-commerce Product Line

**Scenario:** "EcoWave" selling sustainable water bottles, needs product photos with consistent branding.

### Setup

```bash
cp ~/Downloads/ecowave-logo.png ./brand-assets/logos/ecowave.png
```

### Generate Bottle Product Photo

```bash
scripts/generate_image.py \
  "Premium stainless steel water bottle in sage green color on a natural wooden surface. The provided logo is laser-etched into the metal on the front of the bottle, centered vertically, approximately 2 inches wide. The etching should look subtle and high-quality with a matte finish. Background: blurred nature scene (leaves, sunlight) to emphasize eco-friendly theme. Professional product photography, soft natural lighting, shallow depth of field." \
  --ref ./brand-assets/logos/ecowave.png \
  --ar 4:5 \
  --temperature 0.4 \
  --output ./ecowave-products/bottle-sage.png
```

### Generate Packaging Box

```bash
scripts/generate_image.py \
  "Product packaging box for a water bottle. Recyclable kraft cardboard box with natural texture. The provided logo printed on the box lid in forest green ink, centered, 3 inches wide. Minimalist design with small eco-certification icons in corner. The box is photographed at a slight angle showing the lid with logo prominently. Natural lighting, earth-toned aesthetic, sustainable premium feel." \
  --ref ./brand-assets/logos/ecowave.png \
  --ar 1:1 \
  --output ./ecowave-products/packaging.png
```

### Generate Lifestyle Photo

```bash
scripts/generate_image.py \
  "Lifestyle product photography. A hiker's hand holding the water bottle (stainless steel, sage green) with a mountain trail in the blurred background. Golden hour lighting. The provided logo is visible on the bottle, laser-etched, catching the light. Conveys adventure, sustainability, and active lifestyle. Natural colors, authentic moment feel, aspirational but relatable." \
  --ref ./brand-assets/logos/ecowave.png \
  --ar 3:2 \
  --output ./ecowave-products/lifestyle-hiking.png
```

## Example 4: Event Branding

**Scenario:** "DevCon 2026" conference needs consistent branding across materials.

### Setup

```bash
cp ~/Downloads/devcon-logo.png ./brand-assets/logos/devcon.png
```

### Generate Conference Badge

```bash
scripts/generate_image.py \
  "Conference badge design, lanyard size (4x6 inches vertical). White background with bold header section in conference brand colors. The provided logo at top center, 2 inches wide. Space for attendee name, company, and QR code below (blank areas for template). Modern tech conference aesthetic, clean typography area, professional but friendly design." \
  --ref ./brand-assets/logos/devcon.png \
  --ar 2:3 \
  --temperature 0.3 \
  --output ./devcon-2026/badge-template.png
```

### Generate Stage Backdrop

```bash
scripts/generate_image.py \
  "Conference stage backdrop design, ultra-wide format. Dynamic abstract tech-themed background with geometric patterns and gradient colors (blues and purples). The provided conference logo prominently centered, large scale (approximately 6 feet wide at actual print size). Modern, energetic, professional event aesthetic. Design should work well in photos/videos from audience perspective." \
  --ref ./brand-assets/logos/devcon.png \
  --ar 21:9 \
  --output ./devcon-2026/stage-backdrop.png
```

### Generate Social Media Frame

```bash
scripts/generate_image.py \
  "Social media profile picture frame template for conference attendees. Circular border design with conference branding. The provided logo incorporated into the bottom arc of the circle. Bold colors from conference theme. When overlaid on a profile photo, the logo should be clearly visible and the design should frame the face nicely. Modern, shareable, community-building design." \
  --ref ./brand-assets/logos/devcon.png \
  --ar 1:1 \
  --output ./devcon-2026/profile-frame.png
```

## Example 5: Iterative Refinement Workflow

**Scenario:** Getting a t-shirt design exactly right through iterations.

### First Attempt

```bash
scripts/generate_image.py \
  "A black t-shirt flat lay with the provided logo screen-printed on the chest" \
  --ref ./brand-assets/logos/mylogo.png \
  --ar 1:1 \
  --output ./iterations/tshirt-v1.png
```

**Review:** Logo is too small and positioned too high.

### Second Attempt - Size & Position

```bash
scripts/generate_image.py \
  "Take the provided t-shirt image. Make the logo 40% larger and move it down 2 inches so it's better centered on the chest area. Keep the black t-shirt and flat lay style exactly the same." \
  --ref ./iterations/tshirt-v1.png \
  --ref ./brand-assets/logos/mylogo.png \
  --ar 1:1 \
  --temperature 0.3 \
  --output ./iterations/tshirt-v2.png
```

**Review:** Better, but the print looks too glossy. Want vintage effect.

### Third Attempt - Print Finish

```bash
scripts/generate_image.py \
  "Adjust the provided image: change the logo print to have a vintage, slightly faded appearance with a soft matte finish instead of glossy. Make it look like a well-loved screen print that's been washed a few times. Keep size and position exactly as is." \
  --ref ./iterations/tshirt-v2.png \
  --ref ./brand-assets/logos/mylogo.png \
  --ar 1:1 \
  --temperature 0.2 \
  --output ./iterations/tshirt-v3.png
```

**Review:** Perfect! This is the final version.

### Key Takeaways

- **Lower temperature** for refinements (0.2-0.4) to minimize changes
- **Reference the previous iteration** to maintain what's working
- **Still include original logo reference** to maintain consistency
- **Be specific** about what to change and what to keep

## Example 6: Multi-Product Consistency

**Scenario:** Need multiple product mockups with the same logo treatment.

### Create a Logo Style Reference First

```bash
# Generate one perfect example
scripts/generate_image.py \
  "A white ceramic mug on white background. The provided logo is printed on the mug centered with a premium matte finish, exact colors preserved from reference." \
  --ref ./brand-assets/logos/logo.png \
  --ar 1:1 \
  --temperature 0.3 \
  --output ./style-reference/logo-on-mug.png
```

### Use as Reference for Other Products

```bash
# Now apply same style to other products
scripts/generate_image.py \
  "A black t-shirt flat lay. Apply the logo with the same print style and color treatment as shown on the mug in the reference image. Size the logo appropriately for a chest print." \
  --ref ./style-reference/logo-on-mug.png \
  --ref ./brand-assets/logos/logo.png \
  --ar 1:1 \
  --temperature 0.4 \
  --output ./products/tshirt-consistent.png

scripts/generate_image.py \
  "A notebook cover. Apply the logo with the same style as shown on the mug reference - same colors, same finish quality." \
  --ref ./style-reference/logo-on-mug.png \
  --ref ./brand-assets/logos/logo.png \
  --ar 3:4 \
  --temperature 0.4 \
  --output ./products/notebook-consistent.png
```

## Example 7: Seasonal Variations

**Scenario:** Holiday-themed social media posts while maintaining brand identity.

```bash
# Summer theme
scripts/generate_image.py \
  "Instagram post for summer sale. Beach-themed background with soft sand and ocean waves. The provided logo in top-right corner, white version, with subtle sun flare effect. Bright, energetic, vacation vibes while maintaining brand professionalism." \
  --ref ./brand-assets/logos/logo-white.png \
  --ar 1:1 \
  --output ./seasonal/summer-post.png

# Winter holidays
scripts/generate_image.py \
  "Instagram post for holiday season. Elegant winter background with subtle snowflakes and deep blue tones. The provided logo in white with a soft glow effect. Text space in center. Festive but sophisticated, not overly Christmas-y to remain inclusive." \
  --ref ./brand-assets/logos/logo-white.png \
  --ar 1:1 \
  --output ./seasonal/winter-post.png

# Black Friday
scripts/generate_image.py \
  "Instagram post for Black Friday sale. High-energy design with bold geometric shapes. The provided logo prominently displayed. Black, white, and one accent color from brand palette. Modern, urgent, attention-grabbing without being tacky." \
  --ref ./brand-assets/logos/logo-white.png \
  --ref ./brand-assets/colors/palette.png \
  --ar 1:1 \
  --output ./seasonal/black-friday.png
```

## Tips for Maximum Consistency

### 1. Use the Same Reference Image

Don't switch between different versions of your logo file. Pick one high-quality version and use it consistently.

### 2. Create Style Templates

Generate a few "perfect" examples early, then use those as references for new work.

### 3. Document Your Settings

When you get a perfect result, save the exact command:

```bash
# Save successful commands to a reference file
echo "Perfect mug mockup: scripts/generate_image.py '...' --ref logo.png --ar 4:5 --temp 0.4" >> ./successful-prompts.txt
```

### 4. Maintain a Generation Log

```bash
# Log all generations with timestamps
scripts/generate_image.py "$PROMPT" --ref "$LOGO" | tee -a generation-log.json
```

### 5. Batch with Consistent Parameters

```bash
# Define standard settings
LOGO="./brand-assets/logos/logo.png"
TEMP=0.4
STYLE="Professional product photography, soft studio lighting, white background"

# Use them consistently
scripts/generate_image.py "Mug. $STYLE" --ref "$LOGO" --ar 4:5 --temperature "$TEMP"
scripts/generate_image.py "Tshirt. $STYLE" --ref "$LOGO" --ar 1:1 --temperature "$TEMP"
```

## Common Patterns

### Pattern: White Background Product Photos

```bash
scripts/generate_image.py \
  "<product> on pure white background. The provided logo <placement and style>. Professional e-commerce product photography, even lighting, no shadows, crisp focus." \
  --ref ./logo.png \
  --ar <appropriate>
```

### Pattern: Lifestyle Context

```bash
scripts/generate_image.py \
  "<product in real-world setting>. The provided logo visible on product as <treatment>. Natural lighting, authentic moment, lifestyle photography aesthetic." \
  --ref ./logo.png \
  --ar <appropriate>
```

### Pattern: Social Media Post Template

```bash
scripts/generate_image.py \
  "<background description>. The provided logo in <corner> corner, <size>. Text space reserved in <area>. <aesthetic description>." \
  --ref ./logo.png \
  --ar <1:1 or 9:16>
```

### Pattern: Marketing Material

```bash
scripts/generate_image.py \
  "<material type> design. The provided logo <placement>. <brand colors/style>. <target audience feel>. Professional, polished, print-ready aesthetic." \
  --ref ./logo.png \
  --ref ./palette.png (optional) \
  --ar <appropriate>
```

Use these patterns as starting points and customize for your specific needs.
