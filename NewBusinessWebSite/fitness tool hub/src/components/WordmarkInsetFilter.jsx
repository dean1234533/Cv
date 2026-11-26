export default function WordmarkInsetFilter() {
  return (
    <svg className="wordmark-inset-defs" xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true" focusable="false">
      <defs>
        <filter id="db-wordmark-cut" x="-10%" y="-25%" width="120%" height="160%" colorInterpolationFilters="sRGB">
          <feOffset in="SourceAlpha" dx="0.6" dy="1.6" result="cut-offset" />
          <feGaussianBlur in="cut-offset" stdDeviation="0.35" result="cut-blur" />
          <feComposite in="SourceAlpha" in2="cut-blur" operator="out" result="cut-edge" />
          <feFlood floodColor="#000000" floodOpacity="0.95" />
          <feComposite in2="cut-edge" operator="in" result="cut-shadow" />
          <feComposite in="cut-shadow" in2="SourceGraphic" operator="over" result="cut-face" />
          <feOffset in="SourceAlpha" dx="-0.4" dy="-0.9" result="bevel-offset" />
          <feComposite in="SourceAlpha" in2="bevel-offset" operator="out" result="bevel-edge" />
          <feFlood floodColor="#ffffff" floodOpacity="0.8" />
          <feComposite in2="bevel-edge" operator="in" result="bevel-light" />
          <feComposite in="bevel-light" in2="cut-face" operator="over" />
        </filter>
      </defs>
    </svg>
  );
}
