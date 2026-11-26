const PHOTOS = {
  'macro-calculator': '/pics/tools/macro-calculator.webp',
  'tdee-calculator': '/pics/tools/tdee-calculator.webp',
  'protein-calculator': '/pics/tools/protein-calculator.webp',
  'bmi-calculator': '/pics/tools/bmi-calculator.webp',
  'body-fat-calculator': '/pics/tools/body-fat-calculator.webp',
  'water-intake-calculator': '/pics/tools/water-intake-calculator.webp',
  'one-rep-max-calculator': '/pics/tools/one-rep-max-calculator.webp',
  'running-pace-calculator': '/pics/tools/running-pace-calculator.webp',
  'calorie-burn-calculator': '/pics/optimized/training-7856.webp',
  'outdoor-workout-generator': '/pics/optimized/training-7860.webp',
  'workout-plan-generator': '/pics/optimized/training-7858.webp',
  tools: '/pics/optimized/training-7933.webp',
};

export const getToolPhoto = (id) => PHOTOS[id] || PHOTOS.tools;
