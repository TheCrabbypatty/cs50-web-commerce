🛒 CS50 Commerce 
CS50 Commerce is a Django‑based web application that allows users to create listings, place bids, leave comments, browse categories, and close auctions. It follows the specifications from Harvard’s CS50 Web Programming with Python and JavaScript course.
This project demonstrates full‑stack development using Django models, views, templates, authentication, and form handling.
---
✨ Features
🔐 User Authentication
• Register a new account
• Log in / log out
• All bidding and commenting actions require authentication
📦 Create Listings
Users can create auction listings with:
• Title
• Description
• Starting bid
• Image URL
• Category (using Django TextChoices)
💸 Bidding System
• Users can place bids on active listings
• Listing displays the current highest bid
• Only bids higher than the current price are accepted
💬 Commenting
• Users can leave comments on listings
• Comments are displayed on the listing page
🏷️ Category Browsing
• Dropdown menu to filter listings by category
• “None” option shows all listings
• Dropdown remembers the selected category after reload
• Categories include:
	◦ Fashion
	◦ Home & Garden
	◦ Electronics
	◦ Toys & Games
	◦ Sports & Outdoors
	◦ Beauty & Personal Care
	◦ Arts & Crafts
	◦ Pet Supplies
	◦ Office Supplies
🔒 Close Auction (Owner Only)
• Listing creator can close the auction
• Highest bidder becomes the winner
• Listing becomes inactive
• Winner is displayed on the listing page
---
🗂️ Models Overview
Listing
Stores auction details:
• Title
• Description
• Starting bid
• Current price
• Category
• Image URL
• Creator
• Winner
• Active status
Bid
Tracks bids placed on listings:
• Bid value
• Bid creator
• Listing
Comment
Stores user comments:
• Comment text
• Creator
• Listing
Catagory (TextChoices)
Enum for listing categories.
---
🧭 Navigation
• Home Page — shows all active listing
• Watchlist - shows the listings on the watchlist
• Listing Page — bid, comment, or close auction
• Categories Page — filter listings by category
• Create Listing — add a new auction
• Login / Register — user authentication
---
⚙️ Tech Stack
• Python 3
• Django 6
• HTML / CSS
• SQLite (default Django database)
