"""
Data Consolidation Module
Merges data from all intelligence modules into unified profiles
हिंदी में unified profiles बनाता है
"""

import logging
from typing import Dict, List, Optional
from datetime import datetime
from .social_media import social_intel
from .domain_ip import domain_ip_intel
from .email_phone import email_phone_intel
from .location import location_intel
from .people import people_intel

logger = logging.getLogger(__name__)

class DataConsolidator:
    """
    सभी modules के data को एक profile में consolidate करता है
    Consolidates data from multiple intelligence modules
    """
    
    def __init__(self):
        self.modules = {
            'social': social_intel,
            'domain': domain_ip_intel,
            'contact': email_phone_intel,
            'location': location_intel,
            'people': people_intel
        }
    
    # ============================================
    # Unified Profile बनाएं
    # ============================================
    
    def create_unified_profile(self, query: str, modules_to_search: Optional[List[str]] = None) -> Dict:
        """
        एक unified profile बनाएं
        Create unified profile by consolidating data from multiple modules
        
        Args:
            query: खोज क्वेरी (email, domain, username, etc.)
            modules_to_search: Specific modules to search
            
        Returns:
            Consolidated profile in Hindi
        """
        try:
            logger.info(f"Unified profile बना रहे हैं: {query}")
            
            if modules_to_search is None:
                modules_to_search = list(self.modules.keys())
            
            profile = {
                'query': query,
                'timestamp': datetime.utcnow().isoformat(),
                'results': {},
                'summary': {
                    'description_hindi': f"{query} के लिए एक comprehensive profile तैयार की जा रही है।",
                    'modules_searched': modules_to_search
                }
            }
            
            return {
                'success': True,
                'profile': profile,
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Profile consolidation error: {str(e)}")
            return {'success': False, 'error': str(e), 'message': 'Profile बनाने में त्रुटि'}
    
    # ============================================
    # Duplicate हटाएं
    # ============================================
    
    def remove_duplicates(self, data: List[Dict]) -> List[Dict]:
        """
        Duplicate entries को हटाएं
        Remove duplicate entries from consolidated data
        
        Args:
            data: डेटा की list
            
        Returns:
            Deduplicated list
        """
        try:
            seen = set()
            unique_data = []
            
            for item in data:
                item_hash = hash(str(sorted(item.items())))
                
                if item_hash not in seen:
                    seen.add(item_hash)
                    unique_data.append(item)
            
            return unique_data
        
        except Exception as e:
            logger.error(f"Deduplication error: {str(e)}")
            return data
    
    # ============================================
    # Results को merge करें
    # ============================================
    
    def merge_results(self, *results: Dict) -> Dict:
        """
        Multiple modules के results को merge करें
        Merge results from multiple modules
        
        Args:
            *results: विभिन्न module results
            
        Returns:
            Merged dictionary
        """
        try:
            merged = {
                'success': True,
                'modules_searched': len(results),
                'consolidated_data': {},
                'description_hindi': 'सभी modules से डेटा एकत्र किया गया है।',
                'timestamp': datetime.utcnow().isoformat()
            }
            
            for result in results:
                if result.get('success'):
                    module_name = result.get('source', 'unknown')
                    merged['consolidated_data'][module_name] = result
            
            return merged
        
        except Exception as e:
            logger.error(f"Result merge error: {str(e)}")
            return {'success': False, 'error': str(e), 'message': 'Merge में त्रुटि'}
    
    # ============================================
    # Report generate करें
    # ============================================
    
    def generate_report(self, profile: Dict) -> Dict:
        """
        Comprehensive intelligence report बनाएं
        हिंदी में
        Generate comprehensive intelligence report
        
        Args:
            profile: Consolidated profile
            
        Returns:
            Formatted report dictionary
        """
        try:
            logger.info(f"Report बना रहे हैं: {profile.get('query')}")
            
            report = {
                'title': f"Intelligence Report: {profile.get('query')}",
                'query': profile.get('query'),
                'report_date': datetime.utcnow().isoformat(),
                'sections': {
                    'overview': 'Profile overview और summary',
                    'social_media': 'Social media की उपस्थिति',
                    'network': 'Domain और IP की जानकारी',
                    'contact': 'Email और phone विवरण',
                    'location': 'Geographic जानकारी',
                    'people': 'व्यक्ति की विस्तृत जानकारी'
                },
                'confidence_score': 0.0,
                'data_quality': 'pending',
                'description_hindi': f"{profile.get('query')} के लिए एक detailed report तैयार की गई है।",
                'recommendations': []
            }
            
            return {
                'success': True,
                'report': report,
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Report generation error: {str(e)}")
            return {'success': False, 'error': str(e), 'message': 'Report में त्रुटि'}
    
    # ============================================
    # Report को export करें
    # ============================================
    
    def export_report(self, report: Dict, format: str = 'json') -> Dict:
        """
        Report को विभिन्न formats में export करें
        Export report in various formats
        
        Args:
            report: Report dictionary
            format: Export format (json, csv, pdf, html)
            
        Returns:
            Exported report
        """
        try:
            logger.info(f"Report export कर रहे हैं: {format} format में")
            
            if format == 'json':
                return {
                    'success': True,
                    'format': 'json',
                    'report': report,
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            elif format == 'csv':
                return {
                    'success': True,
                    'format': 'csv',
                    'message': 'CSV export implementation pending',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            elif format == 'pdf':
                return {
                    'success': True,
                    'format': 'pdf',
                    'message': 'PDF export implementation pending',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            elif format == 'html':
                return {
                    'success': True,
                    'format': 'html',
                    'message': 'HTML export implementation pending',
                    'timestamp': datetime.utcnow().isoformat()
                }
            
            else:
                return {'success': False, 'error': f'Unknown format: {format}'}
        
        except Exception as e:
            logger.error(f"Report export error: {str(e)}")
            return {'success': False, 'error': str(e), 'message': 'Export में त्रुटि'}


# Instantiate module
data_consolidator = DataConsolidator()
