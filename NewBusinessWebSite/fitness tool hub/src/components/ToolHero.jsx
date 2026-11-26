import { getToolPhoto } from '@/lib/tool-visuals';

/** @param {{ title: string, description: string, tool: string, children?: import("react").ReactNode }} props */
export default function ToolHero({ title, description, tool, children }) {
  return (
    <header className="tool-hero">
      <div className="tool-hero-copy">
        <h1>{title}</h1>
        <p>{description}</p>
        {children}
      </div>
      <img className="tool-hero-photo" src={getToolPhoto(tool)} alt="" width="960" height="640" decoding="async" />
    </header>
  );
}
