<h1>🛒 CS50 Commerce</h1>
CS50 Commerce is a Django-based auction web application where users can create listings, place bids, leave comments, browse listings by category, manage a watchlist, and close auctions.
This project follows the specifications from Harvard’s CS50 Web Programming with Python and JavaScript course and demonstrates full-stack development using Django models, views, templates, authentication, and form handling.

<h2>✨ Features</h2>
🔐 User Authentication

- Register a new account
- Log in and log out
- Restrict bidding and commenting to authenticated users

<h2>📦 Create Listings</h2>

Users can create auction listings with:

- Title
- Description
- Starting bid
- Image URL
- Category using Django TextChoices

<h2>💸 Bidding System</h2>

- Users can place bids on active listings
- Each listing displays the current highest bid
- Bids must be higher than the current price
- The highest bidder can become the auction winner

<h2>💬 Commenting</h2>

- Authenticated users can leave comments on listings
- Comments are displayed on the listing detail page

<h2>👀 Watchlist</h2>

- Users can add listings to their watchlist
- Users can remove listings from their watchlist
- Watchlist page displays saved listings

<h2>🏷️ Category Browsing</h2>
- Users can filter listings by category using a dropdown menu.
- Available categories include:

- Fashion
- Home & Garden
- Electronics
- Toys & Games
- Sports & Outdoors
- Beauty & Personal Care
- Arts & Crafts
- Pet Supplies
- Office Supplies

**The category dropdown includes a None option to show all listings and remembers the selected category after reload.**

<h2>🔒 Close Auction</h2>

- Only the listing creator can close an auction
- The highest bidder becomes the winner
- The listing becomes inactive
- The winner is displayed on the listing page


<h2>🗂️ Models Overview</h2>
<h3>Listing</h3>
Stores auction listing details, including:

- Title
- Description
- Starting bid
- Current price
- Category
- Image URL
- Creator
- Winner
- Active status

<h3>Bid</h3>
Tracks bids placed on listings.
Each bid includes:

- Bid value
- Bid creator
- Listing

<h3>Comment</h3>
Stores user comments on listings.
Each comment includes:

- Comment text
- Creator
- Listing

<h3>Category</h3>
**Uses Django TextChoices to define listing categories.

<h3>🧭 Navigation</h3>

- Home Page — Displays all active listings
- Watchlist — Shows listings saved by the user
- Listing Page — Allows users to bid, comment, add to watchlist, or close an auction
- Categories Page — Filters listings by category
- Create Listing — Allows users to create a new auction listing
- Login / Register — Handles user authentication


⚙️ Tech Stack

- Python 3
- Django 6
- HTML
- CSS
- SQLite


🚀 Getting Starte d
1. Clone the repository
git clone https://github.com/TheCrabbypatty/cs50-web-commerce.git
cd cs50-web-commerce

2. Run migrations
python manage.py makemigrations
python manage.py migrate

3. Start the development server
python manage.py runserver

4. Open the app
Visit:
Texthttp://127.0.0.1:8000/


<h3>📚 Course:</h3>
This project was built as part of Harvard’s CS50 Web Programming with Python and JavaScript course.


## Last Updated

<!-- TIMESTAMP_START -->
_Last updated: 2026-09-04 19:52 UTC_
<!-- TIMESTAMP_END -->
