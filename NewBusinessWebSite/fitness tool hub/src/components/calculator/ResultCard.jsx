import React from "react";

export default function ResultCard({ icon: Icon, label, value, helper }) {
  const isNumber = /^[\d.,:]+(?:g|kg|L|%)?$/.test(String(value));
  return (
    <article className="tool-metric">
      <div className="tool-metric-label">
        <p>{label}</p>
        {Icon && <Icon className="h-4 w-4" aria-hidden="true" />}
      </div>
      <p className={`tool-metric-value ${isNumber ? 'is-number' : ''}`}>{value}</p>
      {helper && <p className="tool-metric-helper">{helper}</p>}
    </article>
  );
}
