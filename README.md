# landing-page

SMERTZ – Rebrand Landing Page
A Python/Flask-powered landing page built to support the official rebrand to SMERTZ and the four‑week social media rollout leading up to the release of the first single on February 1st, 2026.
This page serves as the central hub for the campaign: a countdown, social links, and a mailing list signup that captures early supporters before the drop.

Purpose
This landing page is designed to:
• 	Introduce the new rap identity SMERTZ
• 	Build anticipation for the first single
• 	Collect emails for early access and fan engagement
• 	Direct traffic from social platforms to one unified destination
• 	Serve as the final release location on February 1st, 2026
The design is intentionally simple, fast, and focused to support a clean and effective rollout.

Features
1. Countdown Timer
A live JavaScript countdown to February 1st, 2026, automatically switching to “OUT NOW” once the date arrives.
2. Mailing List Signup
A simple email form that stores signups in a local text file ().
This can later be upgraded to a mailing service or database.
3. Social Media Hub
Prominent links to:
• 	Facebook
• 	Instagram
• 	YouTube
• 	TikTok
These links help drive traffic to active platforms during the four‑week campaign.
4. Hero Section
A bold SMERTZ logo, tagline, and a call‑to‑action to join the mailing list.
5. About / Teaser Section
A short introduction to the SMERTZ rebrand and a teaser for the first single.
6. Responsive Layout
Mobile‑first design with a dark, minimal aesthetic that fits the SMERTZ brand.

Tech Stack
• 	Python 3.x
• 	Flask
• 	HTML5
• 	CSS3
• 	Vanilla JavaScript
No external dependencies beyond Flask.

PROJECT STRUCTUE
-landing-page/
--app.py
--emails.txt
-templates/
--landing.html
-static/
--style.css

RUNNING THE PROJECT
1. Install dependencies:
pip install flask
2. Start the server:
python app.py
3. Open page in your browser
http://127.0.0.1:5000/


Email Storage
All submitted emails are stored in  in the project root.
Each email is:
• 	Lowercased
• 	Deduplicated
• 	Appended only once
This keeps the system simple while still giving you a usable mailing list for the release.

Campaign Strategy Alignment
This landing page is built to support a four‑week rollout, including:
• 	Week 1: Reintroduce SMERTZ and push the landing page
• 	Week 2: Behind‑the‑scenes content with a call‑to‑action to join the list
• 	Week 3: Tease the single and update the page copy
• 	Week 4: Final countdown and heavy traffic to the page
On release day, the countdown automatically switches to an “OUT NOW” message, and you can easily embed the track or music video.

Customization
You can modify:
• 	Social media URLs
• 	Tagline
• 	About section
• 	Styling in 
• 	Release date in 
• 	Email storage logic
The codebase is intentionally simple so it can grow with your brand.

License
This project is yours to modify, extend, and deploy as needed.