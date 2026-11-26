import ToolHero from '@/components/ToolHero';

export default function Hero({ onStart }) {
  return (
    <ToolHero title="Free Macro & Training Goal Calculator" description="Calculate your calories, macros and personalised training recommendations in less than 60 seconds." tool="macro-calculator">
      <button type="button" onClick={onStart} className="tool-start-button">Start Calculator</button>
    </ToolHero>
  );
}
