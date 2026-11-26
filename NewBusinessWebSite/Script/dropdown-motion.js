/** Animate a native details menu without changing its links or keyboard behaviour. */
export function installDropdownMotion(details, panelSelector) {
  const summary = details.querySelector('summary');
  const panel = details.querySelector(panelSelector);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let animation = null;
  let closing = false;
  let previousOverflow = '';

  function cancel() {
    if (animation) {
      animation.onfinish = null;
      animation.cancel();
      animation = null;
      panel.style.overflow = previousOverflow;
    }
  }

  function setOpen(open) {
    if (open === details.open && !closing && !animation) return;
    const current = details.open ? getComputedStyle(panel) : null;
    const visible = current ? {
      opacity: current.opacity, transform: current.transform,
      height: `${panel.getBoundingClientRect().height}px`,
      paddingTop: current.paddingTop, paddingBottom: current.paddingBottom,
      marginTop: current.marginTop, marginBottom: current.marginBottom,
    } : null;
    cancel();
    closing = !open;
    panel.inert = !open;
    if (reduced.matches || typeof panel.animate !== 'function') {
      details.open = open;
      closing = false;
      return;
    }
    if (open) details.open = true;
    const styles = getComputedStyle(panel);
    const collapse = styles.position === 'static';
    const expanded = {
      opacity: '1', transform: 'translateY(0) scale(1)',
      ...(collapse ? {} : { clipPath: 'inset(0 0 0% 0 round 8px)' }),
      ...(collapse ? {
        height: `${panel.getBoundingClientRect().height}px`,
        paddingTop: styles.paddingTop, paddingBottom: styles.paddingBottom,
        marginTop: styles.marginTop, marginBottom: styles.marginBottom,
      } : {}),
    };
    const hidden = {
      opacity: '0', transform: collapse ? 'translateY(-6px)' : 'translateY(-14px) scale(.94)',
      ...(collapse ? {} : { clipPath: 'inset(0 0 100% 0 round 8px)' }),
      ...(collapse ? { height: '0px', paddingTop: '0px', paddingBottom: '0px', marginTop: '0px', marginBottom: '0px' } : {}),
    };
    const start = visible ? (collapse ? visible : { opacity: visible.opacity, transform: visible.transform, clipPath: 'inset(0 0 0% 0 round 8px)' }) : hidden;
    previousOverflow = panel.style.overflow;
    panel.style.overflow = 'hidden';
    animation = panel.animate([start, open ? expanded : hidden], {
      duration: open ? 750 : 350, easing: 'cubic-bezier(.22,.8,.2,1)', fill: 'both',
    });
    if (open) {
      panel.querySelectorAll('a').forEach((a, i) => a.animate(
        [{ opacity: 0, transform: 'translateY(-8px)' }, { opacity: 1, transform: 'translateY(0)' }],
        { duration: 500, delay: 150 + i * 70, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' }));
    }
    animation.onfinish = () => {
      if (!open) details.open = false;
      closing = false;
      cancel();
    };
  }

  function onClick(event) {
    event.preventDefault();
    setOpen(!details.open || closing);
  }
  function onToggle() {
    if (!details.open) { cancel(); closing = false; panel.inert = true; }
  }
  function onReducedChange() {
    if (animation) { const open = !closing; cancel(); closing = false; details.open = open; panel.inert = !open; }
  }
  panel.inert = !details.open;
  summary.addEventListener('click', onClick);
  details.addEventListener('toggle', onToggle);
  reduced.addEventListener('change', onReducedChange);
  return {
    setOpen,
    destroy() {
      cancel();
      summary.removeEventListener('click', onClick);
      details.removeEventListener('toggle', onToggle);
      reduced.removeEventListener('change', onReducedChange);
    },
  };
}
