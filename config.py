# Cryptanalyzer Web UI Configuration

import os

class Config:
    """Base configuration"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = True
    
    # Server settings
    HOST = '0.0.0.0'  # Change to '127.0.0.1' for localhost only
    PORT = 5000
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 200 * 1024 * 1024  # 200 MB max file size
    ALLOWED_EXTENSIONS = {'txt', 'pem', 'json', 'key', 'pub'}
    
    # Security settings
    SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Rate limiting (optional - requires flask-limiter)
    RATELIMIT_ENABLED = False
    RATELIMIT_DEFAULT = "100 per hour"
    
    # Logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'cryptanalyzer.log'
    
    # Paths
    MODULES_PATH = os.path.join(os.getcwd(), 'modules')
    DATA_PATH = os.path.join(os.getcwd(), 'data')
    WORDLISTS_PATH = os.path.join(DATA_PATH, 'wordlists')
    
    # Timeouts (in seconds)
    HASH_CRACK_TIMEOUT = 300  # 5 minutes
    RSA_FACTOR_TIMEOUT = 120  # 2 minutes
    AES_ATTACK_TIMEOUT = 600  # 10 minutes


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    HOST = '127.0.0.1'  # Localhost only in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32).hex()
    SESSION_COOKIE_SECURE = True  # Requires HTTPS
    
    # Enable rate limiting in production
    RATELIMIT_ENABLED = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env='default'):
    """Get configuration based on environment"""
    return config.get(env, DevelopmentConfig)
