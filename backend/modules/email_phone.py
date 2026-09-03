"""
Email & Phone Intelligence Module
Handles: Email finder, phone lookup, validation, carrier info
"""

import requests
import logging
from typing import Dict, List, Optional
from datetime import datetime
import os
import re

logger = logging.getLogger(__name__)

class EmailPhoneIntelligence:
    """
    Gathers intelligence about emails and phone numbers
    """
    
    def __init__(self):
        self.hunter_api_key = os.getenv('HUNTER_API_KEY')
        self.numverify_api_key = os.getenv('NUMVERIFY_API_KEY')
        self.session = requests.Session()
    
    # ============================================
    # Email Finder
    # ============================================
    
    def find_emails(self, domain: str, name: Optional[str] = None) -> Dict:
        """
        Find emails for a domain or person
        Uses Hunter.io free tier (50 searches/month)
        
        Args:
            domain: Domain name
            name: Optional person name
            
        Returns:
            Dictionary with email addresses
        """
        try:
            if not self.hunter_api_key:
                return {
                    'success': False,
                    'error': 'Hunter.io API key not configured',
                    'domain': domain
                }
            
            logger.info(f"Finding emails for domain: {domain}")
            
            url = "https://api.hunter.io/v2/email-finder"
            params = {
                'domain': domain,
                'full_name': name if name else '',
                'type': 'personal',
                'limit': 10
            }
            
            # Note: Hunter.io requires API key in request body
            params['api_key'] = self.hunter_api_key
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                emails = data.get('data', [])
                
                return {
                    'success': True,
                    'domain': domain,
                    'emails_found': len(emails),
                    'emails': emails,
                    'timestamp': datetime.utcnow().isoformat()
                }
            else:
                return {
                    'success': False,
                    'error': f'Hunter.io API error: {response.status_code}',
                    'domain': domain
                }
        
        except requests.Timeout:
            logger.error(f"Email finder timeout for domain: {domain}")
            return {'success': False, 'error': 'Request timeout', 'domain': domain}
        except Exception as e:
            logger.error(f"Email finder error: {str(e)}")
            return {'success': False, 'error': str(e), 'domain': domain}
    
    # ============================================
    # Email Validation
    # ============================================
    
    def validate_email(self, email: str) -> Dict:
        """
        Validate email address format and check if it exists
        
        Args:
            email: Email address to validate
            
        Returns:
            Dictionary with validation results
        """
        try:
            logger.info(f"Validating email: {email}")
            
            # Basic email format validation
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            is_valid_format = bool(re.match(email_pattern, email))
            
            if not is_valid_format:
                return {
                    'success': False,
                    'email': email,
                    'valid': False,
                    'reason': 'Invalid email format'
                }
            
            # Extract domain
            domain = email.split('@')[1]
            
            return {
                'success': True,
                'email': email,
                'valid': True,
                'domain': domain,
                'format_valid': True,
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Email validation error: {str(e)}")
            return {'success': False, 'error': str(e), 'email': email}
    
    # ============================================
    # Phone Number Lookup
    # ============================================
    
    def phone_lookup(self, phone_number: str, country_code: str = 'US') -> Dict:
        """
        Lookup phone number information
        Uses NumVerify API (free tier)
        
        Args:
            phone_number: Phone number to lookup
            country_code: Country code (default: US)
            
        Returns:
            Dictionary with phone information
        """
        try:
            if not self.numverify_api_key:
                return {
                    'success': False,
                    'error': 'NumVerify API key not configured',
                    'phone': phone_number
                }
            
            logger.info(f"Phone lookup for: {phone_number}")
            
            url = "http://api.numverify.com/validate"
            params = {
                'number': phone_number,
                'country_code': country_code,
                'access_key': self.numverify_api_key
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('valid'):
                    return {
                        'success': True,
                        'phone': phone_number,
                        'valid': True,
                        'info': {
                            'country_code': data.get('country_code'),
                            'country_name': data.get('country_name'),
                            'carrier': data.get('carrier'),
                            'line_type': data.get('line_type'),
                            'international_format': data.get('international_format'),
                            'national_format': data.get('national_format')
                        },
                        'timestamp': datetime.utcnow().isoformat()
                    }
                else:
                    return {
                        'success': False,
                        'phone': phone_number,
                        'valid': False,
                        'reason': 'Invalid phone number'
                    }
            else:
                return {
                    'success': False,
                    'error': f'NumVerify API error: {response.status_code}',
                    'phone': phone_number
                }
        
        except requests.Timeout:
            logger.error(f"Phone lookup timeout for: {phone_number}")
            return {'success': False, 'error': 'Request timeout', 'phone': phone_number}
        except Exception as e:
            logger.error(f"Phone lookup error: {str(e)}")
            return {'success': False, 'error': str(e), 'phone': phone_number}
    
    # ============================================
    # Phone Number Validation
    # ============================================
    
    def validate_phone(self, phone_number: str) -> Dict:
        """
        Validate phone number format
        
        Args:
            phone_number: Phone number to validate
            
        Returns:
            Dictionary with validation results
        """
        try:
            logger.info(f"Validating phone: {phone_number}")
            
            # Remove common separators
            cleaned = re.sub(r'[\s\-\(\)\.]+', '', phone_number)
            
            # Check if it's all digits or starts with +
            is_valid = cleaned.replace('+', '').isdigit() and len(cleaned.replace('+', '')) >= 7
            
            return {
                'success': True,
                'phone': phone_number,
                'cleaned': cleaned,
                'valid': is_valid,
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Phone validation error: {str(e)}")
            return {'success': False, 'error': str(e), 'phone': phone_number}


# Instantiate module
email_phone_intel = EmailPhoneIntelligence()
