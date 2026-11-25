import { Link } from 'react-router-dom';
export default function PageNotFound() {
  return <main className="tools-not-found"><p className="tools-eyebrow">404 / PAGE NOT FOUND</p><h1>Let’s get you<br />back on track.</h1><p>This tool may have moved. Browse the fitness tools to find what you need.</p><Link to="/tools" className="tools-nav-book">Browse fitness tools</Link></main>;
}
