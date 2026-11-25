# DB’s Workouts design context

Updated 25 November 2026. Canonical tokens and decisions are in design.json.

## Selected homepage direction

The user selected a high-end sports brand: bold, sharp and energetic. The hero uses a full-bleed background training video with the headline, copy and buttons layered on top. This replaces the earlier split-photo layout.

- Black #101010, off-white #f4f4ef and existing brand red #b30018.
- Barlow Condensed 700 uppercase headings; Inter body and controls.
- Flat surfaces, squared controls, strong alignment and real training photography.
- Responsive autoplay video sources, poster fallback and reduced motion. The user requested no visible pause button.
- Photo-led service links, visible pricing, coach introduction and manual client reviews.

## Implementation

Static HTML and vanilla JavaScript. Styles/homepage-sport.css scopes the approved homepage to .home-sport. Styles/sport-system.css extends the same identity to .sport-site on all public inner HTML pages, and the React tools use .sport-tools. Reuse existing navigation, enquiry forms, pricing data, before-and-after sliders and FAQ controls. Preserve real business information, metadata and structured data. Do not invent credentials or testimonials.

## Image layout preference

Keep the original continuous horizontal photo carousel on all screen sizes. The user dislikes stacked images. Photo-led training options scroll horizontally on mobile.

## Button interactions

All homepage buttons use hover lift and explicit colour changes, press feedback and visible keyboard focus. Respect disabled states and reduced motion. Do not add decorative arrows.

Button colours must use explicit foreground/background pairs in normal, hover and active states. Avoid brightness filters on the entire control.
Do not crossfade text and background colours between inverse button states: switch the pair immediately, while animating only movement, borders and shadows.

## Bottom contact section

The solid red banner and the plain dark replacement were rejected. The current section uses full-width original training photography, dark shading, a bold white Let’s get you moving headline and booking/WhatsApp buttons overlaid on the image. Red remains an accent and primary button colour. Preserve button contrast, the existing scrolling gallery and the video hero.

## Site-wide rollout

224 public inner HTML pages now use sport-system.css. The approved homepage remains in homepage-sport.css. The 12 fitness-tool routes share the same typography, colours, navigation, sharp controls and photographic contact section. Preserve app calculations and enquiry/checkout integrations.

Run `python3 apply_sport_design.py` after regenerating pages; build.sh also runs it. The decorator is idempotent and preserves metadata, canonical links and form destinations. Internal helper pages and the excluded workout/nutrition app source copies are not deployed by this site's build.

Validation evidence and screenshots are stored on the external drive at `/Volumes/Untitled/Codex/dbworkouts-site-redesign/`. The complete local preview is `http://127.0.0.1:8944/`, including clean HTML routes and the built fitness tools. No deployment was performed.

## Mobile photography

Mobile content photographs should preserve their full frame, with natural dimensions and no fixed-height cover crop. Service-hero captions belong below the image on mobile. Coach photos must not be hidden at smaller widths. Jasmin now has one full-width photo instead of a carousel containing different portrait proportions. Photo carousels must use matching landscape proportions. The background-video hero and continuous landscape photo carousel retain their approved treatments.

`lib/image-dimensions.json` records actual local image dimensions. `apply_sport_design.py` fixes mismatched image width/height ratios after page generation without requiring an image-processing dependency in the build environment.

## Pricing and mobile layout rules

Pricing cards must fill the available content width on phones; they are not photo carousels. Use one column below 768px and two columns from 768px to 1199px. Keep booking buttons full width inside cards and feature text legible. Review-carousel controls sit below the card on phones so they do not squeeze its text. Long headings and links must fit 320px screens. Avoid adding padding to both a hero and its inner wrapper.

The mobile contact bar labels are Call Dean (immediate telephone), WhatsApp and Book a call (consultation enquiry). The inner-page decorator preserves this distinction when pages are regenerated.

The comprehensive mobile review checks full-document content and card geometry, including text clipping inside containers, not just the page scroll width. Evidence: mobile-full-review on the external drive. Latest checks cover all 225 HTML pages and 12 tool routes at 320, 390 and 768px.

## Page-specific hero imagery

Results uses a dedicated client before-and-after photo pair, separate from the Pricing training photograph. Keep both client photos equally sized and uncropped across desktop and mobile.

## Mobile carousel scale

Photo carousels must stay compact on phones: height clamp(112px,32vw,144px), consistent 16:9 frames across Home, About and Results. At 390px, images are approximately 222 × 125px, rather than the old 533 × 300px Results images. Keep desktop sizing unchanged.


## Main-page header ownership

Header photographs must not repeat across main pages. The user explicitly chose to retain the existing location-page photos. Treat original and optimized copies as the same photo. Contact uses its own park-court image; Pricing retains dumbbell training; About retains the colour portrait; Results retains its matched client pair. AI plans, online training, pair sessions, beginner training, mobile training, the areas directory and journal pages have separate photographs. Keep these assignments when regenerating pages via apply_sport_design.py.

## Mobile benefits and comparisons

Pricing benefits use the full content width, aligned small icons and open rows with quiet separators. Avoid nested padding that squeezes the text. Apply the same benefit treatment to the free-workout page, and readable mobile descriptions to shared session steps. Comparison rows on phones show the feature above two equally sized, explicitly labelled choices; no sideways scrolling is required. Keep the semantic table and normal desktop layout. Mobile comparison labels come from the actual table headings through the design decorator.

Pricing hero on phones: focus the background photograph at 75% horizontally, with vertical shading that reveals the foreground client’s head and darkens behind the text. Preserve the desktop crop and unique photo assignment.

Results mobile opening follows the user’s IMG_2337.PNG reference: no breadcrumb or eyebrow, heading 32px below the nav, original introduction, two full-width buttons and the matched client photos 32px below. Keep desktop layout unchanged. At 390px the photo pair begins around 481px and the hero ends around 749px, excluding phone/browser chrome.

Results review navigation: matching 48px-high Previous/Next buttons below the card, with a live current/total count between. No overlapping side controls or autoplay. Keep keyboard activation, intentional horizontal swipe, resize persistence and inert inactive slides. Preserve button effects and focus styling.

SEO coach introductions on phones: for the shared Dean portrait section, put a compact, uncropped colour portrait beside the kicker/heading, then show biography and link across the full width, followed by a separated client quotation. Avoid a tall portrait centred in the middle of the text. Apply this to all 131 matching sections; retain other trainer images and desktop/tablet layouts.


## White-section responsive rules

All 154 white sections across 152 static pages were checked at phone, tablet and desktop widths. Text/photo panels for Jasmin and Jay must use two actual columns on larger screens, never inherit the three-column testimonial layout. On phones use one column and preserve the full source frame; cap image height without distorting width. Coach panels on tablets use copy/photo columns with the quotation across the full width below. Online coach biographies now use Dean’s existing portrait and the same compact phone introduction as location pages.

The homepage’s white training-service photographs use consistent 16:9 frames at every width; retain horizontal service-card scrolling on phones. Root horizontal clipping prevents oversized fixed navigation from enlarging phone viewports, without changing scrolling inside photo strips.

Audit evidence is in the external white-sections folder: 225 pages inventoried, 1520 white-section layouts plus 75 breakpoint layouts, 36 tool layouts and 40 viewport checks. Both stylesheets pass deterministic review with no errors/warnings. Source, copy, forms and business pricing remain in the existing repository.
