const toggle = document.getElementById('theme-toggle');
const themeColor = document.querySelector('meta[name="theme-color"]');
function syncThemeButton() {
  const dark = document.documentElement.dataset.theme !== 'light';
  const label = `Switch to ${dark ? 'light' : 'dark'} theme`;
  toggle.setAttribute('aria-label', label);
  toggle.title = label;
  themeColor.setAttribute('content', dark ? '#19181a' : '#ffffff');
}
syncThemeButton();
toggle.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
  document.documentElement.dataset.theme = theme;
  try { localStorage.setItem('theme', theme); } catch (_) {}
  syncThemeButton();
});
document.getElementById('year').textContent = new Date().getFullYear();
