# PAL.AI - Advanced OSINT Intelligence Platform

🔍 **PAL.AI** is a comprehensive Open Source Intelligence (OSINT) platform that consolidates data from multiple free sources to provide unified intelligence gathering, analysis, and location-based insights.

## Features

### 🌐 Social Media OSINT
- Twitter profile search and analysis
- LinkedIn profile gathering
- Instagram account intelligence
- TikTok user research
- Username verification across platforms

### 🌍 Domain & IP Intelligence
- Whois lookup and domain history
- DNS records analysis
- IP geolocation tracking
- ISP information
- Reverse IP lookup

### 📧 Email & Phone Research
- Email address finder
- Phone number lookup and verification
- Email validation
- Phone carrier information
- Contact consolidation

### 📍 Location Intelligence
- Geocoding (address to coordinates)
- Reverse geocoding (coordinates to address)
- Interactive map visualization
- Location history tracking
- Geofencing capabilities

### 💰 Funding & Company Intelligence
- Company profile research
- Funding round information
- Key people identification
- Business registration data
- Growth metrics and analytics

## Tech Stack

### Backend
- **Python 3.9+** - Core intelligence modules
- **Flask/FastAPI** - RESTful API
- **Requests** - HTTP client for API calls
- **Beautiful Soup** - Web scraping
- **SQLite** - Local database

### Frontend
- **React.js** - User interface
- **Axios** - API communication
- **Leaflet.js** - Map visualization
- **Chart.js** - Data visualization
- **Tailwind CSS** - Styling

### Free APIs Used
- Twitter API v2
- LinkedIn (public data)
- Hunter.io (free tier)
- NumVerify
- OpenCage Geocoding
- IP Stack / GeoIP
- Crunchbase (public data)
- Google Custom Search

## Project Structure

```
pal-ai/
├── backend/
│   ├── app.py                    # Flask/FastAPI main
│   ├── requirements.txt          # Python dependencies
│   ├── config/
│   │   └── api_keys.py          # API configuration
│   ├── modules/
│   │   ├── social_media.py      # Twitter, LinkedIn, Instagram, TikTok
│   │   ├── domain_ip.py         # Domain & IP intelligence
│   │   ├── email_phone.py       # Email & Phone research
│   │   ├── location.py          # Geolocation & mapping
│   │   ├── funding.py           # Company & Funding data
│   │   └── consolidator.py      # Unified data aggregation
│   └── routes/
│       ├── social.py            # Social media endpoints
│       ├── domain.py            # Domain/IP endpoints
│       ├── contact.py           # Email/Phone endpoints
│       ├── location.py          # Location endpoints
│       ├── funding.py           # Company/Funding endpoints
│       └── search.py            # Unified search endpoint
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.js     # Search interface
│   │   │   ├── Dashboard.js     # Main dashboard
│   │   │   ├── SocialResults.js # Social media results
│   │   │   ├── LocationMap.js   # Map visualization
│   │   │   ├── ProfileCard.js   # Unified profile display
│   │   │   └── ResultsTable.js  # Data table
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Search.js
│   │   │   ├── Results.js
│   │   │   └── About.js
│   │   ├── services/
│   │   │   └── api.js           # API communication
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── SETUP_GUIDE.md
│   ├── MODULE_DETAILS.md
│   └── EXAMPLES.md
│
├── .env.example                  # Environment variables template
├── docker-compose.yml            # Docker setup
└── LICENSE                       # MIT License
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 14+
- Git

### Installation

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your free API keys to .env
python app.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## API Endpoints

### Search (Unified)
- `POST /api/search` - Comprehensive search across all modules

### Social Media
- `GET /api/social/twitter/:username`
- `GET /api/social/linkedin/:profile`
- `GET /api/social/instagram/:username`
- `GET /api/social/tiktok/:username`

### Domain & IP
- `GET /api/domain/:domain`
- `GET /api/ip/:ipaddress`
- `GET /api/dns/:domain`

### Email & Phone
- `GET /api/email/:email`
- `GET /api/phone/:phonenumber`
- `POST /api/email-finder` - Find emails for domain

### Location
- `GET /api/location/geocode/:address`
- `GET /api/location/reverse/:lat/:lng`
- `GET /api/location/ip/:ipaddress`

### Funding & Company
- `GET /api/company/:name`
- `GET /api/funding/:company`
- `GET /api/people/:name`

## Free APIs Configuration

All APIs used are free tier. See `.env.example` for setup instructions.

## Usage Examples

See `docs/EXAMPLES.md` for detailed examples.

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for guidelines.

## Legal & Ethical Disclaimer

⚠️ **PAL.AI** is designed for lawful intelligence gathering only. Users are responsible for:
- Following local laws and regulations
- Respecting privacy and data protection laws
- Using data ethically and legally
- Compliance with each API's terms of service

## License

MIT License - See LICENSE file for details

## Support

- 📖 Documentation: See `/docs` directory
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

---

**Built with ❤️ for Open Source Intelligence**
