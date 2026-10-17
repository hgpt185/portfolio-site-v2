const toggle = document.getElementById('theme-toggle');
function syncThemeButton() {
  const dark = document.documentElement.dataset.theme !== 'light';
  toggle.textContent = dark ? '☼' : '☾';
  toggle.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
}
syncThemeButton();
toggle.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
  document.documentElement.dataset.theme = theme;
  try { localStorage.setItem('theme', theme); } catch (_) {}
  syncThemeButton();
});
document.getElementById('year').textContent = new Date().getFullYear();
