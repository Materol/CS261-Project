// function to calculate ring colour based on percentage
export function percentToColor(percent) {
  const x = percent / 100;
  const r = Math.min(2 - 2 * x, 1) * 255;
  const g = Math.min(2 * x, 1) * 255;
  return `rgba(${r}, ${g}, 100, 0.6)`;
}

export function getSuccessSplit(metrics) {
  const danger = 2.5;
  const warning = 3.5;
  let e = 0;
  let r = 0;
  let y = 0;
  let g = 0;
  metrics.forEach((metric) => {
    if (metric.value == 0) {
      e++;
    } else if (metric.value < danger) {
      r++;
    } else if (metric.value < warning) {
      y++;
    } else {
      g++;
    }
  });
  const total = e + r + y + g;
  r = (r / total) * 100;
  y = (y / total) * 100;
  g = (g / total) * 100;
  return [r, y, g];
}
