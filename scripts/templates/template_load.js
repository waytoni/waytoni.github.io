// templates/load-template.js
class TemplateLoader {
    constructor() {
        this.cache = new Map();
    }

    async load(templateId, templateUrl) {
        // Check cache first
        if (this.cache.has(templateUrl)) {
            document.getElementById(templateId).innerHTML = this.cache.get(templateUrl);
            this.initializeComponents(templateId);
            return;
        }

        try {
            const response = await fetch(templateUrl);
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            
            const html = await response.text();
            
            // Cache the template
            this.cache.set(templateUrl, html);
            
            // Insert into DOM
            document.getElementById(templateId).innerHTML = html;
            
            // Initialize any dynamic components
            this.initializeComponents(templateId);
            
        } catch (error) {
            console.error(`Failed to load template: ${templateUrl}`, error);
            this.showError(templateId);
        }
    }

    initializeComponents(templateId) {
        const element = document.getElementById(templateId);
        
        // Add active class to current page link
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const links = element.querySelectorAll('a[href]');
        
        links.forEach(link => {
            const linkPage = link.getAttribute('href');
            if (linkPage === currentPage || 
                (currentPage === '' && linkPage === 'index.html')) {
                link.classList.add('active');
            }
        });

        // Initialize any other interactive elements
        // Example: dropdowns, mobile menu, etc.
    }

    showError(templateId) {
        const fallbackContent = `
            <div style="background: #ffebee; color: #c62828; padding: 10px; border-radius: 4px;">
                Navigation failed to load. 
                <a href="index.html">Home</a> |
                <a href="about.html">About</a> |
                <a href="contact.html">Contact</a>
            </div>
        `;
        document.getElementById(templateId).innerHTML = fallbackContent;
    }
}

// Initialize and use the template loader
const templateLoader = new TemplateLoader();

// Load templates when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    templateLoader.load('Topnavbar', 'templates/navbar.html');
    
    // You can load multiple templates
    // templateLoader.load('footer', 'templates/footer.html');
});