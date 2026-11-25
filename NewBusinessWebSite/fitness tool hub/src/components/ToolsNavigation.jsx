import { useEffect, useRef } from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function ToolsNavigation() {
  const { pathname } = useLocation();
  const menu = useRef(null);
  useEffect(() => { if (menu.current) menu.current.open = false; }, [pathname]);
  const links = <>
    <a href="/">Personal training</a><a href="/pricing">Pricing</a><a href="/testimonials">Results</a><a href="/about">About Dean</a>
    <Link to="/tools" aria-current={pathname === '/tools' ? 'page' : undefined}>Fitness tools</Link>
    <a href="/contact" className="tools-nav-book">Book free consultation call</a>
  </>;
  return <header className="tools-site-nav"><div className="tools-site-nav-inner">
    <a href="/" className="tools-site-brand" aria-label="DB's Workouts home"><img src={import.meta.env.BASE_URL + 'logo-3d-matte.webp'} alt="" width="72" height="72" /><span>DB’s Workouts</span></a>
    <nav className="tools-desktop-links" aria-label="Main navigation">{links}</nav>
    <details className="tools-mobile-menu" ref={menu} onKeyDown={event => { if (event.key === 'Escape') { event.currentTarget.open = false; event.currentTarget.querySelector('summary').focus(); } }}>
      <summary>Menu</summary><nav aria-label="Mobile navigation">{links}</nav>
    </details>
  </div></header>;
}
