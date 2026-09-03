"""
PAL.AI - Advanced OSINT Intelligence Platform
Main Flask Application
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Enable CORS
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(','),
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# ============================================
# Error Handlers
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found',
        'status': 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal Server Error: {str(error)}")
    return jsonify({
        'success': False,
        'error': 'Internal server error',
        'status': 500
    }), 500

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors"""
    return jsonify({
        'success': False,
        'error': 'Bad request',
        'status': 400
    }), 400

# ============================================
# Health Check & Status Endpoints
# ============================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }), 200

@app.route('/api/status', methods=['GET'])
def status():
    """API status endpoint"""
    return jsonify({
        'success': True,
        'status': 'online',
        'service': 'PAL.AI - OSINT Platform',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat(),
        'modules': {
            'social_media': 'active',
            'domain_ip': 'active',
            'email_phone': 'active',
            'location': 'active',
            'funding': 'active'
        }
    }), 200

# ============================================
# Info Endpoints
# ============================================

@app.route('/api/info', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'success': True,
        'name': 'PAL.AI',
        'description': 'Advanced OSINT Intelligence Platform',
        'version': '1.0.0',
        'author': 'PAL.AI Team',
        'github': 'https://github.com/bbbajay035-dev/pal-ai',
        'documentation': '/api/docs',
        'endpoints': {
            'health': '/api/health',
            'status': '/api/status',
            'search': '/api/search',
            'social': '/api/social/*',
            'domain': '/api/domain/*',
            'email': '/api/email/*',
            'phone': '/api/phone/*',
            'location': '/api/location/*',
            'company': '/api/company/*'
        }
    }), 200

# ============================================
# Search Endpoints (Unified)
# ============================================

@app.route('/api/search', methods=['POST'])
def unified_search():
    """
    Unified search across all modules
    POST body: {
        'query': 'search_term',
        'type': 'all|social|domain|email|phone|location|company',
        'modules': ['social', 'domain', 'location']  # Optional: specific modules
    }
    """
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        search_type = data.get('type', 'all')
        modules = data.get('modules', [])

        if not query:
            return jsonify({
                'success': False,
                'error': 'Search query is required'
            }), 400

        logger.info(f"Unified search initiated for: {query}")

        # TODO: Implement unified search logic
        # This will call individual modules based on query type

        return jsonify({
            'success': True,
            'query': query,
            'type': search_type,
            'results': {
                'social_media': None,
                'domain_ip': None,
                'email_phone': None,
                'location': None,
                'funding': None
            },
            'timestamp': datetime.utcnow().isoformat(),
            'message': 'Unified search endpoint - modules in development'
        }), 200

    except Exception as e:
        logger.error(f"Search error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ============================================
# Social Media Routes (Placeholder)
# ============================================

@app.route('/api/social/twitter/<username>', methods=['GET'])
def twitter_search(username):
    """Search Twitter profile"""
    try:
        logger.info(f"Twitter search for: {username}")
        return jsonify({
            'success': True,
            'query': username,
            'platform': 'twitter',
            'data': None,
            'message': 'Twitter module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/social/linkedin/<profile>', methods=['GET'])
def linkedin_search(profile):
    """Search LinkedIn profile"""
    try:
        logger.info(f"LinkedIn search for: {profile}")
        return jsonify({
            'success': True,
            'query': profile,
            'platform': 'linkedin',
            'data': None,
            'message': 'LinkedIn module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Domain & IP Routes (Placeholder)
# ============================================

@app.route('/api/domain/<domain>', methods=['GET'])
def domain_lookup(domain):
    """Lookup domain information"""
    try:
        logger.info(f"Domain lookup for: {domain}")
        return jsonify({
            'success': True,
            'query': domain,
            'data': None,
            'message': 'Domain module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/ip/<ipaddress>', methods=['GET'])
def ip_lookup(ipaddress):
    """Lookup IP address information"""
    try:
        logger.info(f"IP lookup for: {ipaddress}")
        return jsonify({
            'success': True,
            'query': ipaddress,
            'data': None,
            'message': 'IP module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Email & Phone Routes (Placeholder)
# ============================================

@app.route('/api/email/<email>', methods=['GET'])
def email_lookup(email):
    """Lookup email information"""
    try:
        logger.info(f"Email lookup for: {email}")
        return jsonify({
            'success': True,
            'query': email,
            'data': None,
            'message': 'Email module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/phone/<phonenumber>', methods=['GET'])
def phone_lookup(phonenumber):
    """Lookup phone number information"""
    try:
        logger.info(f"Phone lookup for: {phonenumber}")
        return jsonify({
            'success': True,
            'query': phonenumber,
            'data': None,
            'message': 'Phone module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Location Routes (Placeholder)
# ============================================

@app.route('/api/location/geocode/<address>', methods=['GET'])
def geocode(address):
    """Geocode address to coordinates"""
    try:
        logger.info(f"Geocoding address: {address}")
        return jsonify({
            'success': True,
            'query': address,
            'data': None,
            'message': 'Location module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/location/reverse/<lat>/<lng>', methods=['GET'])
def reverse_geocode(lat, lng):
    """Reverse geocode coordinates to address"""
    try:
        logger.info(f"Reverse geocoding: {lat}, {lng}")
        return jsonify({
            'success': True,
            'coordinates': {'lat': lat, 'lng': lng},
            'data': None,
            'message': 'Location module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Company & Funding Routes (Placeholder)
# ============================================

@app.route('/api/company/<company_name>', methods=['GET'])
def company_lookup(company_name):
    """Lookup company information"""
    try:
        logger.info(f"Company lookup for: {company_name}")
        return jsonify({
            'success': True,
            'query': company_name,
            'data': None,
            'message': 'Company module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/funding/<company>', methods=['GET'])
def funding_lookup(company):
    """Lookup company funding information"""
    try:
        logger.info(f"Funding lookup for: {company}")
        return jsonify({
            'success': True,
            'query': company,
            'data': None,
            'message': 'Funding module in development'
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Main Entry Point
# ============================================

if __name__ == '__main__':
    port = int(os.getenv('API_PORT', 5000))
    host = os.getenv('API_HOST', '0.0.0.0')
    debug = os.getenv('FLASK_DEBUG', True)
    
    logger.info(f"Starting PAL.AI OSINT Platform on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
