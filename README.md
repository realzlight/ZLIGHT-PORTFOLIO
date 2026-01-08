
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZLIGHT | Portfolio</title>
    <style>
        :root {
            --bg: #0a0a0a;
            --text: #ffffff;
            --accent: #00f2fe;
            --secondary: #4facfe;
            --card-bg: #1a1a1a;
            --nav-bg: rgba(10, 10, 10, 0.8);
            --gradient: linear-gradient(45deg, #00f2fe, #4facfe, #7367f0);
            --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }

        [data-theme="light"] {
            --bg: #f5f7fa;
            --text: #1a1a1a;
            --accent: #4facfe;
            --secondary: #00f2fe;
            --card-bg: #ffffff;
            --nav-bg: rgba(245, 247, 250, 0.8);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            transition: background-color 0.5s ease;
            overflow-x: hidden;
        }

        /* --- Navigation --- */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 1.5rem 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--nav-bg);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid rgba(128, 128, 128, 0.1);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            letter-spacing: 2px;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            z-index: 1100;
        }

        .desktop-nav { display: flex; gap: 2rem; align-items: center; }
        .desktop-nav a { text-decoration: none; color: inherit; font-weight: 500; opacity: 0.8; transition: var(--transition); }
        .desktop-nav a:hover { opacity: 1; color: var(--accent); }

        /* --- Mobile Navigation Elements --- */
        .menu-btn {
            display: none;
            cursor: pointer;
            z-index: 1100;
            flex-direction: column;
            gap: 6px;
        }

        .menu-btn span {
            display: block;
            width: 25px;
            height: 2px;
            background: var(--text);
            transition: var(--transition);
        }

        .sidebar {
            position: fixed;
            top: 0;
            right: -100%;
            width: 280px;
            height: 100vh;
            background: var(--card-bg);
            z-index: 1050;
            padding: 120px 40px;
            display: flex;
            flex-direction: column;
            gap: 2rem;
            transition: 0.5s cubic-bezier(0.77,0.2,0.05,1.0);
            box-shadow: -10px 0 30px rgba(0,0,0,0.3);
        }

        .sidebar.active { right: 0; }

        .sidebar a {
            text-decoration: none;
            color: var(--text);
            font-size: 1.5rem;
            font-weight: 600;
        }

        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(4px);
            z-index: 1040;
            display: none;
        }

        .overlay.active { display: block; }

        /* Mobile specific icon animations */
        .menu-btn.open span:nth-child(1) { transform: translateY(8px) rotate(45deg); }
        .menu-btn.open span:nth-child(2) { opacity: 0; }
        .menu-btn.open span:nth-child(3) { transform: translateY(-8px) rotate(-45deg); }

        /* Responsive Breakpoint */
        @media (max-width: 768px) {
            .desktop-nav { display: none; }
            .menu-btn { display: flex; }
        }

        /* --- Stacking Cards Logic --- */
        .stack-container {
            padding: 0 10%;
            display: flex;
            flex-direction: column;
            gap: 4rem;
            padding-bottom: 10vh;
        }

        .stack-section {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .stack-section h2 {
            position: sticky;
            top: 100px;
            margin-bottom: 2rem;
            z-index: 10;
        }

        .card {
            position: sticky;
            top: 160px;
            height: 350px;
            width: 100%;
            max-width: 800px;
            margin: 0 auto 50px auto;
            background: var(--card-bg);
            border-radius: 24px;
            padding: 3rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }

        .card::after {
            content: '';
            position: absolute;
            inset: -2px;
            background: var(--gradient);
            border-radius: 24px;
            z-index: -1;
            opacity: 0.3;
            animation: borderRotate 4s infinite linear;
        }

        .card h3 { font-size: 2rem; margin-bottom: 1rem; color: var(--accent); }
        .card p { font-size: 1.1rem; opacity: 0.8; line-height: 1.6; }

        /* --- Theme Toggle --- */
        .theme-toggle {
            width: 45px;
            height: 24px;
            background: #333;
            border-radius: 20px;
            position: relative;
            cursor: pointer;
        }
        .toggle-ball {
            position: absolute;
            top: 2px;
            left: 2px;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            transition: var(--transition);
        }
        [data-theme="light"] .theme-toggle { background: #ddd; }
        [data-theme="light"] .toggle-ball { left: 23px; background: #4facfe; }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        .contact-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(128,128,128,0.2);
            transition: var(--transition);
        }
        .contact-card:hover { transform: translateY(-10px); border-color: var(--accent); }
        .contact-card a { color: var(--accent); text-decoration: none; font-weight: bold; }

        @keyframes borderRotate {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }

        section { min-height: 100vh; padding: 120px 10% 60px; }
        .hero-title { font-size: clamp(3rem, 10vw, 6rem); font-weight: 900; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

    </style>
</head>
<body>

<div class="overlay" id="overlay"></div>

<nav>
    <div class="logo">ZLIGHT</div>
    
    <div class="desktop-nav">
        <a href="#home">Home</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
        <div class="theme-toggle" id="themeToggle"><div class="toggle-ball"></div></div>
    </div>

    <div class="menu-btn" id="menuBtn">
        <span></span>
        <span></span>
        <span></span>
    </div>
</nav>

<div class="sidebar" id="sidebar">
    <a href="#home">Home</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
    <div style="margin-top: 20px; display: flex; align-items: center; gap: 15px;">
        <span>Theme</span>
        <div class="theme-toggle" id="themeToggleMobile"><div class="toggle-ball"></div></div>
    </div>
</div>

<section id="home">
    <h1 class="hero-title">It's Me ZLIGHT!</h1>
    <p style="font-size: 1.5rem; opacity: 0.7; margin-top: 1rem;">Full Stack Developer & Python, Java Expert! Along With Data!</p>
</section>

<div class="stack-container">
    <div class="stack-section" id="skills">
        <h2>Expertise</h2>
        <div class="card">
            <h3>Frontend Mastery</h3>
            <p>HTML5, CSS3, JavaScript (ES6+), and React. Building responsive, high-performance web applications with a focus on UX.</p>
        </div>
        <div class="card">
            <h3>Python & Logic</h3>
            <p>Data processing, automation. Leveraging Python for clean, scalable solutions.</p>
        </div>
        <div class="card">
            <h3>System Languages</h3>
            <p>Java and C. Deep understanding of memory management, OOP principles, and low-level optimization.</p>
        </div>
        <div class="card">
            <h3>Creative Arts</h3>
            <p>Professional Video Editing and Strategic Thinking through high-level Chess. Combining technical precision with creative flair.</p>
        </div>
    </div>

    <div class="stack-section" id="projects">
        <h2>Selected Works</h2>
        <div class="card">
            <h3>MULTI AI TOOLS WEBSITE</h3>
            <p>A Multi AI Tool SaaS Website That Include AI Job Recommender Advanced, AI Mentor Advanced, AI Chess Teacher, AI Resume Builder</p>
        </div>
        <div class="card">
            <h3>AI-PEDIA</h3>
            <p>An AI Powered Wikipedia Replacement With Modern UI And Features, Generates Information When Someone Search About It, Unlimited Content! </p>
        </div>
        <div class="card">
            <h3>Social Media WebSite</h3>
            <p>A New Featured Social Media Website With AI Chats And AI Features Simply Instagram And YouTube Fusion!</p>
        </div>
    </div>
</div>

<section id="contact">
    <h2 class="logo">Get In Touch</h2>
    <p style="font-size: 1.2rem; opacity: 0.8;">Available for collaborations and creative projects.</p>
    
    <div class="contact-grid">
        <div class="contact-card">
            <h4>Email</h4>
            <p><a href="mailto:legitzlight@gmail.com">legitzlight@gmail.com</a></p>
        </div>
        <div class="contact-card">
            <h4>Instagram</h4>
            <p><a href="#">@real_zlight</a></p>
        </div>
        <div class="contact-card">
            <h4>Location</h4>
            <p>India</p>
        </div>
         <div class="contact-card">
            <h4>GitHub</h4>
            <p>github.com/realzlight</p>
        </div>
    </div>
    <footer style="margin-top: 5rem; opacity: 0.4; text-align: center;">
        © 2026 ZLIGHT Portfolio • Built with Precision
    </footer>
</section>

<script>
    // Theme Toggle Logic
    const toggleTheme = () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', newTheme);
    };

    document.getElementById('themeToggle').onclick = toggleTheme;
    document.getElementById('themeToggleMobile').onclick = toggleTheme;

    // Mobile Menu Logic
    const menuBtn = document.getElementById('menuBtn');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    const sidebarLinks = document.querySelectorAll('.sidebar a');

    const toggleMenu = () => {
        menuBtn.classList.toggle('open');
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.style.overflow = sidebar.classList.contains('active') ? 'hidden' : 'auto';
    };

    menuBtn.onclick = toggleMenu;
    overlay.onclick = toggleMenu;
    sidebarLinks.forEach(link => link.onclick = toggleMenu);

    // Stacking Effect Shadow Adjustment on Scroll
    window.addEventListener('scroll', () => {
        const cards = document.querySelectorAll('.card');
        const scrollPos = window.scrollY;

        cards.forEach((card, index) => {
            const rect = card.getBoundingClientRect();
            // Using a dynamic offset based on card index to match your CSS 'top' values
            const stickyPoint = 160 + (index * 20);
            
            if (rect.top <= stickyPoint + 5) {
                card.style.transform = `scale(${1 - (index * 0.02)})`;
                card.style.filter = `brightness(${1 - (index * 0.1)})`;
            } else {
                card.style.transform = `scale(1)`;
                card.style.filter = `brightness(1)`;
            }
        });
    });
</script>

</body>
</html>
