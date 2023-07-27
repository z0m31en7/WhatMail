<h1 align="center" id="title">WhatMail?</h1><br>

<p align="center"><img src="https://socialify.git.ci/z0m31en7/WhatMail/image?font=Source%20Code%20Pro&amp;logo=https%3A%2F%2Fraw.githubusercontent.com%2Fz0m31en7%2FWhatMail%2Fmain%2FWhatMail-Logo.png&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;theme=Dark" alt="project-image"></p><br>

<p id="description">WhatMail is a command-line tool that analyzes the header of an email and provides detailed information about various fields. It extracts commonly recognized email header fields such as To From Subject Date Delivered-To as well as useful fields like Message-ID Return-Path Reply-To X-Headers MIME Version Content Type Received-SPF DKIM Signature Authentication-Results X-Mailer and DMARC Results. <br><br>This tool is useful for forensic analysis investigating email authenticity understanding email routing and gathering information about the email sender and recipient. The output is presented in a tabular format making it easy to read and analyze.</p><br>

<p align="center"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="shields"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="shields"><img src="https://img.shields.io/badge/PyCharm-000000.svg?&amp;style=for-the-badge&amp;logo=PyCharm&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="shields"></p><br>



<p align="center"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-yo0yfqDgCAgNGi_YMRO-So68vb89uQEu3pJpQJ_YSrgo1TeIrwHQF8zRhnuO5TORcttBeMRJntx0cyTS8jzOUgWLeeGA=s2560" alt="project-screenshot"></p><br><br>
<h2>Preview:</h2><br>
<p align="center"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-ycfXzKmDbWjw40MQFyRegwbt7Yunf3fl0aw03kgUkz3JE0-2P8ZM5ceDQt5xmpj0DlWBI43EGbE4XQ3VKzY2jsicvPLA=s1600" alt="project-screenshot"></p><br>

  
  <h2>💻 Filters Supported:</h2><br>

*   Message-ID
*   Return-Path
*   Reply-To
*   X-Headers
*   MIME Version
*   Content Type
*   Received-SPF
*   DKIM Signature
*   Authentication Results
*   X-Mailer
*   DMARC Results

<br><h2>🛠️ Installation Steps:</h2>

```
git clone https://github.com/z0m31en7/WhatMail.git
```

```
cd WhatMail
```

```
python WhatMail.py -hf {Path_to_header_file}
```
<br><h2>🎓 Usage:</h2>
``` 
python WhatMail.py -hf header.txt
```
<br>
Analyzes the email header in the 'header.txt' file and displays the results on the console.

<br>
<br>

```
python WhatMail.py -hf header.txt -O analysis_results.txt
```
<br>
        Analyzes the email header in the 'header.txt' file and saves the analysis results in the 'analysis_results.txt' file.


<br><h2>🛡️ License:</h2><br>
This project is licensed under the <a href="https://github.com/z0m31en7/WhatMail/blob/main/LICENSE">MIT-LICENSE</a>
