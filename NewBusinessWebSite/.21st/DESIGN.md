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

Do not show Home / page-name breadcrumb trails on any public page. The logo links home. The design decorator removes visible breadcrumb markup after regeneration; retain structured data for search engines.

Areas Covered uses IMG_7861 3.jpg, showing the outdoor gym at Stratford Park, following the latest user correction. Do not substitute homepage training photos or court photographs. Park Guide uses victoria-park-london.jpg to keep these two main headers distinct; see pics/image-credits.json for its CC0 source.

WhatsApp sizing: shared floating action 72×72px with a 36px icon and 24px edge spacing. Mobile contact-bar actions are 52px high with 76px bottom space plus the safe-area inset. Preserve the existing WhatsApp destinations, responsive visibility and button effects. Latest shared/home styles use version 23.


## Initial page positioning

Keep foreground headings, labels, images and actions clear of the 88px fixed navigation. About has no negative portrait margin: its colour photo starts below the header, scales with viewport height and keeps its complete frame. On short laptops reduce spacing and stat padding, with enough text-column width to keep the booking actions together. On phones add explicit top clearance. Show final About statistics immediately instead of counting up from zero.

Programs shows its title before page-number navigation. The workout generator uses the shared tool-header spacing, without a duplicate logo/back-link block; its hero and first form appear immediately. The macro hero also starts in its final position. Keep the user’s mobile Results reference, full-background homepage video and existing carousel layouts.

Validated all 237 public routes at 9 viewport sizes (2133 opening layouts), followed by 168 changed-route/tool layouts and focused short-laptop checks. Tool lint/typecheck/build and 12 prerenders passed. Evidence is in the external opening-layouts folder. Latest shared static stylesheet version is 24; homepage version remains 23.

Currency icons must use pounds sterling (£), including the homepage No Gym Fees icon.

Homepage benefit icons: tree and sun for Outdoor Training; apple and leaf for Nutrition Support. Keep the same line weight, clear internal spacing and decorative aria-hidden treatment.

Homepage benefit icons: coach/client figures for Personalised Coaching, and a checked progress clipboard for Real Accountability.


## Know Your Numbers imagery

User explicitly requested realistic generated photos instead of icons for all eight tools. Use the eight photo assets in pics/tools and their generation-briefs.json; built-in image_gen was used. These are fictional editorial still-life illustrations, not client photographs. Keep the original labels and calculator links, matching 3:2 image frames, four columns above 859px and two below, compact phone photos, visible keyboard focus and reduced-motion support. Optimized WebP files are 960×640. The homepage stylesheet is version 25.


Header logo: 72×72px across shared website/tool navigation, while retaining the existing 88px navigation height. Use 160px/320px responsive WebP sources on static pages for sharp high-density rendering; tool navigation retains its high-resolution original. Keep menus within 320px screens.

The homepage trust strip must keep all three full labels on one mobile line, with compact decorative icons beside their text. Do not wrap or clip the labels. Latest homepage stylesheet version is 27; shared static stylesheet version is 26.


## 3D logo

The user requested a 3D version of the existing shield logo. Use the transparent red enamel/black-metal version with silver bevelled D, raised B, muscular dumbbell arm, DB’s text and red star. The original logo.png remains intact. The full PNG and built-in image-generation prompt are in pics/branding; static pages use responsive logo-3d-160/320 WebP sources, and tools use public/logo-3d.webp. Headers remain 72px for the mark and 88px for the navigation. Visible footer/brand images also use the new artwork. Do not replace it with the old flat assets during regeneration.

Latest logo refinement: use logo-3d-clean.png and logo-3d-clean-160/320.webp (tool public/logo-3d-clean.webp). The user rejected the fine perimeter lines around the earlier 3D badge; use the smooth single dark-metal rim while keeping the raised emblem details. Original and earlier 3D versions remain saved.

Latest logo uses logo-3d-matte assets with no perimeter glare. Header logo hover gently lifts and tilts, with press/focus feedback and reduced-motion support. Do not add glow or shine.

Header wordmark: bold italic uppercase Barlow Condensed 800, 24px and 22px below 360px. Keep all words on one line beside the matte 3D shield.

Buttons use subtle raised faces: inset top edge, 3px dark base, soft shadow, 1px hover lift and 2px press-down. Keep current readable colour pairs, focus rings and reduced-motion support.

Tool pages must not display promotional/directory badges or badge carousels. Remove server injection as well as source markup; calculator data labels and progress controls remain functional. All 12 routes checked; lint/typecheck/build and prerenders pass.

## Premium tool pages

All 12 routes share the existing charcoal/red/ivory sports identity through ToolHero and tool-visuals.js. Use the approved compressed still-life and training photography, with compact side images on phones. Forms have deliberate spacing, 50px inputs and visible selection/focus states. Ivory results panels use large figures, units and useful explanations, without arbitrary decorative progress bars. Long calculator forms no longer stretch empty results panels. The tool hub has consistent photo cards; keep search and category filters. Keep promotional/directory badges removed, use plain exercise-type metadata, retain genuine data charts and wizard progress. Preserve calculator formulae, validation, metadata, booking and download functionality.

Validation evidence: external tools-premium audit/review/calculations files, sample calculations for all nine standalone tools plus the macro wizard and workout/nutrition generator; directory search/filter and invalid-input checks; lint, typecheck, production build and 12 prerenders. 21st catalogue was unavailable without sign-in, so reuse the approved project primitives and imagery.

Final tool QA (2026-11-26): 60 layouts across 12 routes at 320/390/768/1024/1440px, with no page overflow, clipped form controls, heading/header collisions, missing hero photos or directory badges. Populated TDEE metric text minimum contrast is 5.90:1; input keyboard focus has a solid 2px outline. Rechecked the outdoor generator after fixing its result-summary state reference. Final deterministic review: zero errors and warnings.

Navigation dropdowns: shared Script/dropdown-motion.js animates native details (220ms open, 160ms close, fade/6px slide and mobile inline height). Static nav controller is an ES module, version 2. Keep reduced-motion instant changes, inert closing panels, Escape focus return, rapid-toggle handling and route-change closure. Verified desktop and mobile main menus and tools menu; lint/typecheck/build, 12 prerenders and deterministic review pass.

Mobile menu spacing correction (IMG_2341 2.JPG): mobile rows must override inherited desktop gap to 0, and direct menu children must not flex-shrink when dropdowns expand. Use 15px links and 50px minimum rows, preserving existing motion and Safari bottom room. Shared stylesheet version 7. Validated 36 menu states across home/About and six viewport sizes (320–1024px), including short phone screens; no overlap/overflow and booking is reachable.

Navigation now has a restrained recessed treatment: dark desktop link tray and soft inset shadows on the header/mobile panel/toggle, with unchanged header clearance and compact menu rows. Shared nav CSS version 8. Checked main, inner and tools navigation at 320/390/1100/1440px; no overlap/overflow, header remains 89px including border.

User rejected the subtle recessed nav as looking unchanged. Current version 9 uses a visibly lighter charcoal surround, deep black desktop tray and individually recessed mobile links with 6px separation. Keep 50px rows and reachable booking action; main/tools layouts checked at 320/390/1100/1440px, build and deterministic review pass.

The DB’s Workouts header text has silver/charcoal 3D extrusion and a soft cast shadow, preserving the approved italic Barlow Condensed and accessible live text. Applied to static/tool navigation; CSS version 10. Checked at 320/390/1100/1440px with no clipping or overflow.

Latest wordmark correction: user requested indented lettering instead of raised text. Static/tool CSS now uses a readable silver-grey face (#bdbdb5), dark upper cut and light lower bevel, without diagonal extrusion/cast shadow. Static CSS cache version 11; 224 references verified, diff check passed, face/header contrast 7.90:1. External volume is accessible again; tools rebuild and all 12 prerenders passed. Verified engraved text on main/tool pages at 320/390/1440px, with no clipping or overflow.

Deep wordmark engraving: user rejected outside text shadows as too subtle. The current db-wordmark-cut filter clips the cut shadow and lower bevel into the live lettering using SourceAlpha, offsets and composites. Keep one non-rendering absolute SVG definition per page (never display:none), preserve live accessible text. React uses WordmarkInsetFilter; Python navigation includes WORDMARK_INSET and removes stale copies before regeneration. Static CSS version 12. Eight main/tools layouts, 224 filter instances and generation idempotence checked; lint/typecheck/build and 12 prerenders pass. Reference: https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Filters

Mobile menu bottom inset is now 20px plus the device safe area, replacing the excessive 120px toolbar allowance. Keep the booking action reachable within the scrolling panel. CSS version 13; 24 states verified across home/About and four screen sizes, measured 21px including border, no overflow.

Photo carousel loading: all three strips (Home/About/Results) use responsive 320/480px WebP sources plus optimized master fallbacks. Load strip photos eagerly at low priority, including off-screen clones, and pause the animation until decode completes. Keep image order, visual sizes, existing pace and full-resolution lightbox actions. Shared helper lib/carousel_images.py preserves these rules during regeneration. Home mobile gallery payload is 31% smaller; About/Results about 82% smaller than their JPEG strips. Verified all photos ready before scrolling; local Fast 4G emulation on a 390px/DPR2 viewport completed nine Home image requests by 1057ms. Detailed report is on the external drive.

Google Maps: Home/Contact use eager loading and verified direct www.google.com/maps/embed URLs, plus preconnects to Google and Maps static resources. Preserve the original locations, zooms, dimensions and Google links. prepare_map_loading keeps this idempotent. Hero video initializes at DOM readiness and navigation closes on persisted pageshow only, so an external map cannot hold up the video or unexpectedly close an open menu on initial load. Nav module version 7. Verified both frames return HTTP 200 directly and start loading at the top of the page.
