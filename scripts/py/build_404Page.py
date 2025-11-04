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
  If you are looking for a specific page, please check the navigation menu for updated page locations.</p>
  <p>All previous and current lessons can be found at <a href="https://waytoni.com/All_Playlists/SiyaluDesana.html">
  https://waytoni.com/All_Playlists/SiyaluDesana.html.</a></p>
  <p>Notes used for lessons can be found at <a href="https://waytoni.com/documents/NotesForDesana/NotesForDesana.html">
    https://waytoni.com/documents/NotesForDesana/NotesForDesana.html</a>.</p>
  <p>Sorry for the inconvenience.</p>
  
  </div>
  
  
<div id="error-details-form" style="margin: 20px; padding: 10px; background: #f5f5f5; border: 1px solid #ddd;">
    <p><strong>If you reach this page, please help us by submitting the form below (simply click submit).</strong></p>
    <form name="gform" id="gform" enctype="text/plain"
      action="https://docs.google.com/forms/d/e/1FAIpQLSe3x9kVCwo4lqh2OB2Wej816f3GynYNhZ91OwSCxMRGj0pypg/formResponse?"
      target="hidden_iframe" onsubmit="submitted=true;"> Missing Page: <input type="text" name="entry.803131664"
        id="entry.803131664"><br> Linked from: <input type="text" name="entry.318794381" id="entry.318794381">
      <br>
    
      <button type="submit" id="submitButton">Submit</button>
    </form>
    <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) {}"></iframe>
</div>
<!-- Display error details -->
  <div id="error-details" style="margin: 20px; padding: 10px; background: #f8f8f8; border: 1px solid #ddd;">
    <p><strong>Missing page:</strong> <span id="broken-url"></span></p>
    <p><strong>Linked from:</strong> <span id="referring-page"></span></p>
  </div>
  <script src="/scripts/jquery-3.7.1.min.js"></script>
  <script type="text/javascript">
    var submitted = false;
  </script>
  <style>
    #submitButton {
      background-color: #ff0000;   /* Red background */
      color: #ffffff;             /* White text */
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    #submitButton:hover {
      background-color: #cc0000;
      /* Darker red on hover */
    }
  </style>
  <script type="text/javascript">
    $('#gform').on('submit', function (e) {
      $('#gform *').fadeOut(2000);
      $('#gform').prepend('Your submission has been processed...');
    });
  </script>
  <script>
    // Get the broken URL (current 404 page)
    const brokenUrl = window.location.href;
    document.getElementById('broken-url').textContent = brokenUrl;
    // Get the referring page (where the user came from)
    const referrer = document.referrer || 'Direct entry (no referrer)';
    const referrerField = document.getElementById('entry.318794381');
    document.getElementById('referring-page').textContent = referrer;
    document.getElementById('entry.803131664').value = brokenUrl;
    document.getElementById('entry.318794381').value = referrer;
    // Log to Google Analytics (GA4)
    if (typeof gtag === 'function') {
      gtag('event', '404_error', {
        broken_url: brokenUrl,
        referrer: referrer,
        page_path: window.location.pathname
      });
    }
  </script>


</body>
</html>
"""
PrepareHeadTop(html_file, series_title, simple_style)

with open(html_file, 'a', encoding='utf-8') as fp:
    fp.write(page_body)
    

