// Cryptanalyzer Web UI Utilities

/**
 * Format JSON output with syntax highlighting
 */
function formatOutput(data) {
    if (typeof data === 'string') {
        return data;
    }
    return JSON.stringify(data, null, 2);
}

/**
 * Show loading state in output element
 */
function showLoading(elementId, message = 'Processing...') {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = message;
        el.classList.add('loading-state');
    }
}

/**
 * Clear loading state
 */
function clearLoading(elementId) {
    const el = document.getElementById(elementId);
    if (el) {
        el.classList.remove('loading-state');
    }
}

/**
 * Display result in output element with formatting
 */
function displayResult(elementId, data) {
    const el = document.getElementById(elementId);
    if (!el) return;
    
    clearLoading(elementId);
    
    // Check if data contains error
    if (data.error) {
        el.innerHTML = `<span class="error-text">❌ Error: ${escapeHtml(data.error)}</span>`;
        if (data.traceback) {
            el.innerHTML += `\n\n<span class="text-gray-400">Traceback:</span>\n${escapeHtml(data.traceback)}`;
        }
    } else if (data.success === false) {
        el.innerHTML = `<span class="error-text">❌ ${escapeHtml(JSON.stringify(data))}</span>`;
    } else {
        // Success case
        let output = '';
        
        if (data.output) {
            output += `<span class="success-text">✅ Output:</span>\n${escapeHtml(data.output)}\n\n`;
        }
        
        if (data.result !== undefined && data.result !== null) {
            output += `<span class="text-cyan-300">Result:</span>\n${escapeHtml(formatOutput(data.result))}`;
        }
        
        if (data.private_pem) {
            output += `\n\n<a href="${data.private_pem}" class="text-cyan-400 underline">Download private.pem</a>`;
        }
        
        if (data.rainbow_table) {
            output += `\n\n<a href="${data.rainbow_table}" class="text-cyan-400 underline">Download rainbow table</a>`;
        }
        
        el.innerHTML = output || formatOutput(data);
    }
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return String(text).replace(/[&<>"']/g, m => map[m]);
}

/**
 * Validate required fields
 */
function validateFields(fields) {
    for (const field of fields) {
        const element = document.getElementById(field.id);
        if (!element) continue;
        
        const value = element.value ? element.value.trim() : '';
        
        if (field.required && !value) {
            alert(`Please provide: ${field.label}`);
            element.focus();
            return false;
        }
        
        // File input validation
        if (element.type === 'file' && field.required) {
            if (!element.files || element.files.length === 0) {
                alert(`Please upload: ${field.label}`);
                element.focus();
                return false;
            }
        }
    }
    return true;
}

/**
 * Make API call with error handling
 */
async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, options);
        
        // Check if response is JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        } else {
            const text = await response.text();
            return { success: false, error: 'Non-JSON response', response: text };
        }
    } catch (error) {
        return {
            success: false,
            error: error.message || 'Network error occurred',
            details: String(error)
        };
    }
}

/**
 * Create FormData from file input and additional fields
 */
function createFormData(fileInputId, additionalFields = {}) {
    const formData = new FormData();
    
    // Add file if exists
    if (fileInputId) {
        const fileInput = document.getElementById(fileInputId);
        if (fileInput && fileInput.files && fileInput.files.length > 0) {
            const fieldName = fileInput.getAttribute('name') || 'file';
            formData.append(fieldName, fileInput.files[0]);
        }
    }
    
    // Add additional fields
    for (const [key, value] of Object.entries(additionalFields)) {
        if (value !== null && value !== undefined) {
            formData.append(key, value);
        }
    }
    
    return formData;
}

/**
 * Copy text to clipboard
 */
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        showNotification('Copied to clipboard!', 'success');
    } catch (err) {
        showNotification('Failed to copy', 'error');
    }
}

/**
 * Show notification message
 */
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `message ${type} fixed top-4 right-4 z-50 animate-fade-in`;
    notification.textContent = message;
    notification.style.maxWidth = '300px';
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transition = 'opacity 0.3s';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Download text as file
 */
function downloadAsFile(content, filename) {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

/**
 * Format bytes to human readable
 */
function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        formatOutput,
        showLoading,
        clearLoading,
        displayResult,
        escapeHtml,
        validateFields,
        apiCall,
        createFormData,
        copyToClipboard,
        showNotification,
        downloadAsFile,
        formatBytes
    };
}
