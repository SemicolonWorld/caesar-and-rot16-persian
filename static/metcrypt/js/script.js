const githubIcon = document.querySelector(".fa-github");
const githubDevelopers = document.querySelectorAll(".git-hub__developer");

githubIcon.onclick = () => {
  githubDevelopers.forEach((item) => {
    item.classList.toggle("active");
  });
};
