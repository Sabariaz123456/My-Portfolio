import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1,user-scalable=no" />
  <title>Saba Muhammad Riaz - Software Engineer Portfolio</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
    /* Reset and base */
    *, *::before, *::after {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background: #f9fbff;
      color: #2c3e50;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 20px 10px 40px;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    .container {
      background: #ffffff;
      max-width: 350px;
      width: 100%;
      border-radius: 24px;
      box-shadow:
        0 12px 36px rgba(46, 61, 73, 0.15);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      max-height: 600px;
      scroll-behavior: smooth;
    }
    header {
      background: linear-gradient(135deg, #667eea, #764ba2);
      padding: 40px 20px 35px;
      text-align: center;
      box-shadow:
        0 6px 16px rgba(118, 75, 162, 0.5);
      border-bottom-left-radius: 24px;
      border-bottom-right-radius: 24px;
      user-select: none;
      color: #ffffff;
      transition: background 0.4s ease;
    }
    header h1 {
      margin: 0;
      font-size: 2.5rem;
      font-weight: 700;
      letter-spacing: 3px;
      text-shadow: 0 0 10px rgba(255 255 255 / 0.7);
      line-height: 1.2;
      user-select: text;
    }
    header p {
      margin: 14px 0 0;
      font-weight: 500;
      font-size: 1.15rem;
      letter-spacing: 1.1px;
      text-shadow: 0 0 5px rgba(0 0 0 / 0.2);
      user-select: text;
    }
    main {
      padding: 28px 32px;
      overflow-y: auto;
      flex-grow: 1;
      scroll-behavior: smooth;
      color: #34495e;
    }
    /* Section Stylings */
    section {
      margin-bottom: 36px;
    }
    h2 {
      font-size: 1.55rem;
      color: #5a4a96;
      border-bottom: 4px solid #8a6be4;
      padding-bottom: 10px;
      margin-bottom: 22px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      filter: drop-shadow(0 0 6px #967ccf66);
      transition: color 0.4s ease, border-color 0.4s ease;
      user-select: none;
    }
    /* Summary */
    #summary p {
      font-size: 1.05rem;
      line-height: 1.65;
      font-weight: 400;
      letter-spacing: 0.03em;
      margin: 0;
      user-select: text;
    }
    /* Skills */
    #skills ul {
      list-style: none;
      padding: 0;
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
    }
    #skills ul li {
      background: linear-gradient(135deg, #8567f5, #a68fff);
      color: #fff;
      padding: 12px 22px;
      border-radius: 28px;
      font-size: 1rem;
      font-weight: 700;
      user-select: none;
      box-shadow:
        0 10px 22px rgba(134, 103, 245, 0.8);
      cursor: pointer;
      transition:
        transform 0.4s cubic-bezier(0.25,0.46,0.45,0.94),
        box-shadow 0.4s ease,
        background 0.4s ease;
      outline-offset: 4px;
      outline-color: transparent;
    }
    #skills ul li:hover,
    #skills ul li:focus,
    #skills ul li.active {
      transform: scale(1.12);
      box-shadow:
        0 12px 28px rgba(134, 103, 245, 1),
        0 0 15px 3px rgba(166, 143, 255, 0.7);
      background: linear-gradient(135deg, #5847ca, #806ef8);
      outline-color: #5847ca;
      outline-style: solid;
      outline-width: 2px;
      z-index: 10;
      position: relative;
    }
    /* Projects */
    #projects {
      position: relative;
    }
    #projects .filter-controls {
      margin-bottom: 20px;
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      justify-content: center;
      user-select: none;
    }
    #projects .filter-controls button {
      background: #8a6be4;
      color: #fff;
      border: none;
      border-radius: 22px;
      cursor: pointer;
      padding: 10px 22px;
      font-weight: 700;
      font-size: 1rem;
      box-shadow: 0 8px 24px rgba(138, 107, 228, 0.75);
      transition: background 0.4s ease, box-shadow 0.4s ease;
      outline-offset: 3px;
      outline-color: transparent;
    }
    #projects .filter-controls button:hover,
    #projects .filter-controls button:focus,
    #projects .filter-controls button.active {
      background: #654bbb;
      box-shadow: 0 10px 30px rgba(101, 75, 187, 0.95);
      outline-color: #654bbb;
      outline-style: solid;
      outline-width: 3px;
      z-index: 10;
      position: relative;
    }
    #projects .project {
      background: #f3f5ff;
      border-radius: 20px;
      padding: 24px 28px;
      margin-bottom: 24px;
      cursor: default;
      box-shadow:
        0 10px 30px rgba(120, 120, 230, 0.25);
      transition:
        transform 0.4s cubic-bezier(0.25,0.46,0.45,0.94),
        box-shadow 0.4s ease,
        color 0.4s ease;
      user-select: text;
      color: #2a2f4a;
      line-height: 1.5;
      font-weight: 400;
      letter-spacing: 0.02em;
    }
    #projects .project.hide {
      display: none;
      opacity: 0;
    }
    #projects .project:hover,
    #projects .project:focus {
      transform: translateY(-8px);
      box-shadow:
        0 20px 50px rgba(101, 75, 187, 0.7);
      outline: none;
      color: #462ea7;
      font-weight: 600;
      letter-spacing: 0.03em;
    }
    #projects .project h3 {
      margin: 0 0 10px 0;
      font-size: 1.4rem;
      font-weight: 700;
      color: #8079ff;
      text-shadow: 0 0 5px #785fdaaa;
      text-transform: capitalize;
      line-height: 1.15;
    }
    #projects .project p {
      margin: 0 0 16px 0;
      font-size: 1rem;
      font-weight: 400;
      color: #50567e;
      line-height: 1.6;
      user-select: text;
    }
    #projects .project a {
      font-size: 1.05rem;
      font-weight: 700;
      color: #7f87ff;
      text-decoration: none;
      border-bottom: 3px solid transparent;
      transition: border-color 0.35s ease;
      user-select: text;
      letter-spacing: 0.03em;
    }
    #projects .project a:hover,
    #projects .project a:focus {
      border-color: #6557bb;
      outline: none;
    }
    /* Contact */
    #contact p {
      font-size: 1.1rem;
      margin: 14px 0;
      font-weight: 400;
      color: #606b9e;
      user-select: text;
    }
    #contact a {
      color: #7f87ff;
      font-weight: 700;
      text-decoration: none;
      border-bottom: 3px solid transparent;
      transition: border-color 0.35s ease;
      user-select: text;
      letter-spacing: 0.02em;
    }
    #contact a:hover,
    #contact a:focus {
      border-color: #4a3edb;
      outline: none;
    }
    /* Scrollbar styling for main content */
    main::-webkit-scrollbar {
      width: 8px;
      border-radius: 12px;
    }
    main::-webkit-scrollbar-track {
      background: #fff;
      border-radius: 12px;
    }
    main::-webkit-scrollbar-thumb {
      background-color: #7f87ff;
      border-radius: 12px;
      box-shadow: inset 0 0 6px rgba(127,135,255,0.4);
    }
    /* Responsive */
    @media (max-width: 350px) {
      .container {
        max-width: 350px;
      }
      main {
        max-height: 570px;
        padding: 28px 24px;
      }
      header h1 {
        font-size: 2.2rem;
      }
      h2 {
        font-size: 1.35rem;
        border-width: 3px;
      }
      #skills ul li {
        font-size: 1rem;
        padding: 10px 18px;
      }
      #projects .project {
        padding: 20px 22px;
        font-size: 0.95rem;
      }
      #projects .project h3 {
        font-size: 1.3rem;
      }
      #projects .filter-controls button {
        padding: 8px 15px;
        font-size: 0.9rem;
      }
    }
  </style>
</head>
<body>
  <div class="container" role="main" aria-label="Software Engineer Portfolio for Saba Muhammad Riaz">
    <header>
      <h1 tabindex="0">Saba Muhammad Riaz</h1>
      <p tabindex="0">Software Engineer & Full-Stack Developer</p>
    </header>
    <main tabindex="0">
      <section id="summary" aria-label="Summary">
        <h2> Summary</h2>
        <p>
          Energetic Software Engineer skilled in Python and modern web technologies including Next.js, JavaScript, and CSS. Committed to building sleek, high-performance applications focused on excellent user experience and clean code. Continuously learning, collaborating, and solving complex challenges.
        </p>
      </section>

      <section id="skills" aria-label="Technical Skills">
        <h2>Skills</h2>
        <ul>
          <li tabindex="0" data-skill="python">Python</li>
          <li tabindex="0" data-skill="javascript">JavaScript (ES6+)</li>
          <li tabindex="0" data-skill="nextjs">Next.js</li>
          <li tabindex="0" data-skill="react">React</li>
          <li tabindex="0" data-skill="nodejs">Node.js & Express</li>
          <li tabindex="0" data-skill="restapi">RESTful APIs</li>
          <li tabindex="0" data-skill="git">Git & GitHub</li>
        </ul>
      </section>

      <section id="projects" aria-label="Projects">
        <h2>Projects</h2>
        <div class="filter-controls" role="tablist" aria-label="Filter projects by technology">
          <button type="button" class="active" data-filter="all" role="tab" aria-selected="true">All</button>
          <button type="button" data-filter="python" role="tab">Python</button>
          <button type="button" data-filter="nextjs" role="tab">Next.js</button>
          <button type="button" data-filter="css" role="tab">CSS</button>
          <button type="button" data-filter="javascript" role="tab">JavaScript</button>
        </div>
        <div class="project" tabindex="0" aria-describedby="proj1desc" data-tech="nextjs javascript react">
          <h3>Password-Generator-project</h3>
          <p id="proj1desc">
Password Generator Project is a tool that automatically creates strong, random passwords to enhance security for user accounts.          </p>
          <a href="https://github.com/Sabariaz123456/Password-Generator-project-3.git" target="_blank" rel="noopener noreferrer" aria-label="View NextPortfolio on GitHub">View on GitHub</a>
        </div>
        <div class="project" tabindex="0" aria-describedby="proj2desc" data-tech="python restapi">
          <h3>Personal-library_Manager</h3>
          <p id="proj2desc">
Personal Library Manager is a digital tool or software that helps individuals organize, track, and manage their personal book collections.          </p>
          <a href="https://github.com/Sabariaz123456/Personal-library_Manager.git" target="_blank" rel="noopener noreferrer" aria-label="View Python API Server on GitHub">View on GitHub</a>
        </div>
        <div class="project" tabindex="0" aria-describedby="proj3desc" data-tech="css javascript">
          <h3>Multi-Language-Online-Code-Editor</h3>
          <p id="proj3desc">
Multi-Language Online Code Editor is a web-based platform that allows users to write and execute code in multiple programming languages like C, C++, Python, Java, and more.
It is convenient for both beginners and professionals as it requires no installation and works directly from the browser.          </p>
          <a href="https://github.com/Sabariaz123456/Multi-Language-Online-Code-Editor.git" target="_blank" rel="noopener noreferrer" aria-label="View CSS3 UI Kit on GitHub">View on GitHub</a>
        </div>
      </section>

      <section id="contact" aria-label="Contact Information">
        <h2>Contact</h2>
        <p>Email: <a href="mailto:sabaranicool94@gmail.com">sabaranicool94@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/saba-muhammad-riaz-2333512b5/" target="_blank" rel="noopener noreferrer">linkedin.com/in/sabamriaz</a></p>
        <p>GitHub: <a href="https://github.com/Sabariaz123456" target="_blank" rel="noopener noreferrer">github.com/sabamriaz</a></p>
      </section>
    </main>
  </div>
  <script>
    // Skill badges clickable highlight with smooth toggle
    const skillItems = document.querySelectorAll('#skills ul li');
    skillItems.forEach(skill => {
      skill.addEventListener('click', () => {
        skill.classList.toggle('active');
      });
      skill.addEventListener('keyup', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          skill.classList.toggle('active');
          e.preventDefault();
        }
      });
    });

    // Project filter with smooth show hide
    const filterButtons = document.querySelectorAll('#projects .filter-controls button');
    const projects = document.querySelectorAll('#projects .project');
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        filterButtons.forEach(btn => {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        });
        button.classList.add('active');
        button.setAttribute('aria-selected', 'true');
        const filter = button.getAttribute('data-filter');
        projects.forEach(project => {
          if (filter === 'all') {
            project.classList.remove('hide');
            project.style.pointerEvents = 'auto';
            project.style.opacity = '1';
            project.style.transition = 'opacity 0.35s ease';
          } else {
            const tech = project.getAttribute('data-tech');
            if (tech && tech.includes(filter)) {
              project.classList.remove('hide');
              project.style.pointerEvents = 'auto';
              project.style.opacity = '1';
              project.style.transition = 'opacity 0.35s ease';
            } else {
              project.style.opacity = '0';
              project.style.pointerEvents = 'none';
              setTimeout(() => {
                project.classList.add('hide');
              }, 360);
            }
          }
        });
      });
    });
  </script>
</body>
</html>
"""

components.html(html_code, height=660, scrolling=True)
