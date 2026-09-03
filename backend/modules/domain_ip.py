"""
Domain & IP Intelligence Module
Handles: Whois lookups, DNS records, IP geolocation, Reverse IP lookup
"""

import requests
import logging
from typing import Dict, List, Optional
from datetime import datetime
import os
import socket

logger = logging.getLogger(__name__)

class DomainIPIntelligence:
    """
    Gathers intelligence about domains and IP addresses
    """
    
    def __init__(self):
        self.ipstack_key = os.getenv('IPSTACK_API_KEY')
        self.abstract_key = os.getenv('ABSTRACT_API_KEY')
        self.session = requests.Session()
    
    # ============================================
    # Domain Whois Lookup
    # ============================================
    
    def whois_lookup(self, domain: str) -> Dict:
        """
        Lookup domain WHOIS information (free service)
        Uses whois.com free API
        
        Args:
            domain: Domain name (e.g., example.com)
            
        Returns:
            Dictionary with WHOIS data
        """
        try:
            logger.info(f"WHOIS lookup for: {domain}")
            
            # Using whois.com free API
            url = f"https://www.whois.com/whois/{domain}"
            
            # For production, use API like:
            # https://api.whois.com/v1/domains/{domain}
            # or: https://www.arin.net/resources/registry_data_access/
            
            # Placeholder response
            return {
                'success': True,
                'domain': domain,
                'data': {
                    'registrar': None,
                    'registrant': None,
                    'admin': None,
                    'tech': None,
                    'name_servers': [],
                    'creation_date': None,
                    'expiry_date': None,
                    'status': []
                },
                'message': 'WHOIS module requires implementation with free API service',
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"WHOIS lookup error: {str(e)}")
            return {'success': False, 'error': str(e), 'domain': domain}
    
    # ============================================
    # DNS Records Lookup
    # ============================================
    
    def dns_lookup(self, domain: str) -> Dict:
        """
        Lookup DNS records for domain
        Records: A, AAAA, MX, TXT, NS, SOA, CNAME
        
        Args:
            domain: Domain name
            
        Returns:
            Dictionary with DNS records
        """
        try:
            logger.info(f"DNS lookup for: {domain}")
            
            dns_records = {
                'A': [],
                'AAAA': [],
                'MX': [],
                'TXT': [],
                'NS': [],
                'SOA': [],
                'CNAME': []
            }
            
            # Try to resolve basic A record
            try:
                a_records = socket.gethostbyname_ex(domain)
                dns_records['A'] = a_records[2]
            except:
                pass
            
            return {
                'success': True,
                'domain': domain,
                'records': dns_records,
                'timestamp': datetime.utcnow().isoformat(),
                'note': 'Extended DNS records require DNS API integration'
            }
        
        except Exception as e:
            logger.error(f"DNS lookup error: {str(e)}")
            return {'success': False, 'error': str(e), 'domain': domain}
    
    # ============================================
    # IP Geolocation
    # ============================================
    
    def ip_geolocation(self, ip_address: str) -> Dict:
        """
        Get geolocation data for IP address
        Free tier: Uses ipstack API (100 requests/month free)
        Fallback: Abstract API
        
        Args:
            ip_address: IP address to lookup
            
        Returns:
            Dictionary with geolocation data
        """
        try:
            logger.info(f"IP geolocation lookup for: {ip_address}")
            
            # Try ipstack first
            if self.ipstack_key:
                url = f"http://api.ipstack.com/{ip_address}"
                params = {
                    'access_key': self.ipstack_key,
                    'format': 'json'
                }
                
                response = self.session.get(url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    return {
                        'success': True,
                        'ip': ip_address,
                        'location': {
                            'country': data.get('country_name'),
                            'country_code': data.get('country_code'),
                            'region': data.get('region_name'),
                            'city': data.get('city'),
                            'latitude': data.get('latitude'),
                            'longitude': data.get('longitude'),
                            'timezone': data.get('time_zone', {}).get('id'),
                            'isp': data.get('isp'),
                            'organization': data.get('org')
                        },
                        'timestamp': datetime.utcnow().isoformat()
                    }
            
            # Fallback to Abstract API
            if self.abstract_key:
                url = "https://ipgeolocation.abstractapi.com/v1/"
                params = {
                    'api_key': self.abstract_key,
                    'ip_address': ip_address
                }
                
                response = self.session.get(url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    return {
                        'success': True,
                        'ip': ip_address,
                        'location': {
                            'country': data.get('country'),
                            'country_code': data.get('country_code'),
                            'region': data.get('region'),
                            'city': data.get('city'),
                            'latitude': data.get('latitude'),
                            'longitude': data.get('longitude'),
                            'timezone': data.get('timezone')
                        },
                        'timestamp': datetime.utcnow().isoformat()
                    }
            
            return {
                'success': False,
                'error': 'IP geolocation API keys not configured',
                'ip': ip_address
            }
        
        except requests.Timeout:
            logger.error(f"IP geolocation timeout for: {ip_address}")
            return {'success': False, 'error': 'Request timeout', 'ip': ip_address}
        except Exception as e:
            logger.error(f"IP geolocation error: {str(e)}")
            return {'success': False, 'error': str(e), 'ip': ip_address}
    
    # ============================================
    # Reverse IP Lookup
    # ============================================
    
    def reverse_ip_lookup(self, ip_address: str) -> Dict:
        """
        Reverse lookup - find domains hosted on IP
        
        Args:
            ip_address: IP address
            
        Returns:
            Dictionary with domains on this IP
        """
        try:
            logger.info(f"Reverse IP lookup for: {ip_address}")
            
            # Try reverse DNS lookup
            try:
                hostname = socket.gethostbyaddr(ip_address)
                return {
                    'success': True,
                    'ip': ip_address,
                    'hostname': hostname[0],
                    'aliases': hostname[1],
                    'addresses': hostname[2],
                    'timestamp': datetime.utcnow().isoformat()
                }
            except socket.herror:
                return {
                    'success': False,
                    'error': 'No reverse DNS entry found',
                    'ip': ip_address
                }
        
        except Exception as e:
            logger.error(f"Reverse IP lookup error: {str(e)}")
            return {'success': False, 'error': str(e), 'ip': ip_address}
    
    # ============================================
    # IP ISP Information
    # ============================================
    
    def isp_lookup(self, ip_address: str) -> Dict:
        """
        Get ISP information for IP address
        
        Args:
            ip_address: IP address
            
        Returns:
            Dictionary with ISP data
        """
        try:
            logger.info(f"ISP lookup for: {ip_address}")
            
            # Combine with geolocation data
            geo_data = self.ip_geolocation(ip_address)
            
            if geo_data.get('success'):
                return {
                    'success': True,
                    'ip': ip_address,
                    'isp': geo_data.get('location', {}).get('isp'),
                    'organization': geo_data.get('location', {}).get('organization'),
                    'country': geo_data.get('location', {}).get('country'),
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            return geo_data
        
        except Exception as e:
            logger.error(f"ISP lookup error: {str(e)}")
            return {'success': False, 'error': str(e), 'ip': ip_address}


# Instantiate module
domain_ip_intel = DomainIPIntelligence()
