# ENGINEER_CORE - Professional Portfolio

A modern, minimalist portfolio website for showcasing your engineering projects and skills. Built with Django backend and vanilla HTML/CSS/JavaScript frontend.

## 🎨 Design Features

- **Modern Minimalist Design**: Purple-blue gradient backgrounds with clean white cards
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations**: Interactive animations and transitions throughout
- **Fast Performance**: Optimized for quick load times and smooth interactions
- **Professional Typography**: Mix of serif (Playfair Display) and sans-serif (Inter) fonts

## 📋 Sections

1. **Hero Section** - Bold introduction with call-to-action buttons
2. **About** - Personal introduction with statistics
3. **Skills** - Categorized technical skills with proficiency indicators
4. **Projects** - Featured project portfolio with images and links
5. **Contact** - Contact form with backend integration
6. **Footer** - Social links and copyright information

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js (optional, for local serving)
- Git

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser account:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

The Django API will be available at `http://localhost:8000/api`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Start a local server (using Python):
```bash
python -m http.server 8001
```

Or using Node.js (if installed):
```bash
npx http-server
```

3. Open your browser and navigate to `http://localhost:8001`

## 📝 Configuration

### Environment Variables

Edit `.env` file to configure:
- `SECRET_KEY` - Django secret key for production
- `DEBUG` - Debug mode (set to False in production)
- `ALLOWED_HOSTS` - Allowed host domains
- `CORS_ALLOWED_ORIGINS` - Frontend URLs for CORS
- `CONTACT_EMAIL` - Email to receive contact form submissions
- `DEFAULT_FROM_EMAIL` - Email from address

### Customizing Content

#### Update Personal Information

1. **Frontend HTML** (`frontend/index.html`):
   - Update name, title, and description in the hero section
   - Update social media links in the social-links section
   - Modify profile image URL

2. **Backend Data** (via Django Admin):
   - Navigate to `http://localhost:8000/admin`
   - Add your projects, skills, and other portfolio data
   - The frontend will automatically fetch and display this data

## 🛠️ API Endpoints

### Contact Messages
- `POST /api/contacts/` - Submit a contact form message

### Projects
- `GET /api/projects/` - List all projects
- `GET /api/projects/featured/` - List featured projects only

### Skills
- `GET /api/skills/` - List all skills
- `GET /api/skills/by_category/` - List skills grouped by category

## 🎯 Customization Guide

### Colors

Edit CSS variables in `frontend/styles.css`:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --accent-color: #667eea;
    --accent-dark: #764ba2;
}
```

### Fonts

Change font imports in `frontend/index.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT:wght@400;700&display=swap" rel="stylesheet">
```

### Sections

Each section can be hidden by commenting out or removing the corresponding HTML section in `frontend/index.html`.

## 📧 Contact Form Integration

To enable email sending:

1. Update `.env` with your email configuration:
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

2. Set `CONTACT_EMAIL` to receive submissions

## 🚢 Deployment

### Frontend (Vercel)

1. Push your frontend code to GitHub
2. Connect repository to Vercel
3. Set build command: `npm install`
4. Deploy

### Backend (Heroku/Railway/Render)

1. Create a `Procfile`:
```
web: gunicorn config.wsgi
```

2. Update `requirements.txt` with production dependencies
3. Deploy to your chosen platform
4. Update frontend API endpoint in `script.js`

## 🧪 Testing

Run Django tests:
```bash
python manage.py test
```

## 📄 License

MIT License - feel free to use this template for your portfolio

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Happy coding! 🚀**
