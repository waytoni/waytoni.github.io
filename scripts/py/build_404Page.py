import sys

# print the original sys.path
# print('Original sys.path:', sys.path)

import os
sys.path.append('scripts/py')

# print('Updated sys.path:', sys.path)

from utilities import *


basepath = ''

html_file = os.path.join(basepath,'404.html')

playlist_url = ''

series_title = 'Page Not Found waytoni.com'

print(html_file)

simple_style = """
	<style>
		h1,
	 	h2, 
		h3, 
		p, 
		a {
			text-align: center;
		}
	</style>
"""

page_body = """
    <br>
    <center>
        <br>
        <h2>404</h2>
        <br>
        <img src="/images/favicon-32x32.png" alt="404">
        <br>
        <h1>Page not found.</h1>
    </center>
    <br>

  <h1>404 - Page Not Found</h1>
  
 
  <div id="page-details" style="margin: 20px; padding: 10px; background: #fdfdfd; border: 1px solid #ddd;">
  <p>Please note that some pages have been moved or removed. 
  If you are looking for a specific page, please check the navigation menu for updated page location.</p>
  <p>Sorry for the inconvenience.</p>
  
  </div>
  
  
   <!-- Display error details -->
  <div id="error-details" style="margin: 20px; padding: 10px; background: #f8f8f8; border: 1px solid #ddd;">
    <p><strong>Missing page:</strong> <span id="broken-url"></span></p>
    <p><strong>Linked from:</strong> <span id="referring-page"></span></p>
  </div>

  <script>
    // Get the broken URL (current 404 page)
    const brokenUrl = window.location.href;
    document.getElementById('broken-url').textContent = brokenUrl;

    // Get the referring page (where the user came from)
    const referrer = document.referrer || 'Direct entry (no referrer)';
    document.getElementById('referring-page').textContent = referrer;

    // Log to Google Analytics (GA4)
    if (typeof gtag === 'function') {
      gtag('event', '404_error', {
        broken_url: brokenUrl,
        referrer: referrer,
        page_path: window.location.pathname
      });
    }

    // Optional: Log to console for debugging
    console.log('404 Error Details:', { brokenUrl, referrer });
  </script>


</body>
</html>
"""
PrepareHeadTop(html_file, series_title, simple_style)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write(page_body)
    

