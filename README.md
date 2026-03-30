# Leijie Tao — Personal Portfolio

A full-page slide portfolio website showcasing my background in software engineering and investment analysis.

**Live site:** [leijie-tao.github.io/My-Profile-Web](https://leijie-tao.github.io/My-Profile-Web/)

## Sections

1. **Home** — Hero with photo, CTA buttons, social links
2. **About** — Background summary, floating tech icons, stats cards
3. **Skills** — Backend, Frontend, Data & AI, Tools, Business & Strategy, AI-assisted dev
4. **Journey** — Experience & Education timeline with tab switcher
5. **Projects** — MarketLens, Employee Management System, SV Housing Market Analysis
6. **Contact** — Email CTA, LinkedIn/GitHub/Resume links, availability status

## Tech Stack

- HTML / CSS / JavaScript (vanilla, no framework)
- Bootstrap 5 for responsive grid
- Font Awesome icons
- Playfair Display + Inter fonts
- GitHub Pages for deployment
- GitHub Actions for CI/CD

## Features

- Full-page slide navigation (click-only, no scroll hijacking)
- Right-side navigation dots with tooltips
- Previous/next section buttons
- Keyboard navigation (Arrow keys)
- Entrance animations via Intersection Observer
- Internal scrolling for content-heavy sections (Skills, Journey)
- Animated gradient background orbs
- Responsive design

## Local Development

```bash
cd frontend
python -m http.server 8001
# Open http://localhost:8001
```

## Deployment

Deployed automatically via GitHub Actions to GitHub Pages. Push to `main` triggers deployment of the `frontend/` directory.

## License

MIT
