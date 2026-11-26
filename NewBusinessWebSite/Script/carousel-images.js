// Prime the complete loop, including off-screen photos, before it starts moving.
document.querySelectorAll('.gallery-strip,.about-marquee,.training-scroll-inner').forEach(strip => {
  const images = [...strip.querySelectorAll('img')];
  if (!images.length) return;
  strip.setAttribute('data-carousel-loading', '');
  Promise.all(images.map(img => {
    if (typeof img.decode === 'function') return img.decode().catch(() => {});
    if (img.complete) return Promise.resolve();
    return new Promise(resolve => {
      img.addEventListener('load', resolve, { once: true });
      img.addEventListener('error', resolve, { once: true });
    });
  })).then(() => strip.removeAttribute('data-carousel-loading'));
});
