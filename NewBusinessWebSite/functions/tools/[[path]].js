// SPA fallback for /tools/* — serves /tools/index.html for all sub-routes.
// Passes through requests for static files (assets, images, etc.) unchanged.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  // Let static assets pass through unchanged
  if (/\.[a-z0-9]+$/i.test(url.pathname)) {
    return context.env.ASSETS.fetch(context.request);
  }
  url.pathname = "/tools/index.html";
  return context.env.ASSETS.fetch(url.toString());
}
