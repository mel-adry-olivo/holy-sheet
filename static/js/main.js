const sidebarTools = document.querySelectorAll('.sidebar-tool');
const sidebarSecondary = document.querySelector('.sidebar-secondary');

const initSidebar = () => {
  sidebarTools.forEach((tool) =>
    tool.addEventListener('click', () => {
      toggleSidebar(tool);
    }),
  );
};

const toggleSidebar = (tool) => {
  sidebarSecondary.classList.toggle('active');

  sidebarTools.forEach((tool) => {
    tool.classList.remove('active');
  });
  tool.classList.add('active');
};

initSidebar();
