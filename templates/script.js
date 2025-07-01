function toggleTheme() {
  const body = document.body;
  const html = document.documentElement;
  const icon = document.querySelector(".theme-toggle");

  if (body.classList.contains("dark-mode")) {
    body.classList.remove("dark-mode");
    body.classList.add("bg-light");
    html.setAttribute("data-theme", "light");
    icon.innerText = "dark_mode";
  } else {
    body.classList.add("dark-mode");
    body.classList.remove("bg-light");
    html.setAttribute("data-theme", "dark");
    icon.innerText = "light_mode";
  }
}
