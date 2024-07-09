# E-Commerce Auction Platform

## Overview
The E-Commerce Auction Platform is a web application developed using Django, allowing users to create, view, and bid on auction listings. The platform includes user authentication, listing creation, bidding functionality, and watchlist management.

## Features
- **User Authentication**: Secure user registration, login, and logout functionalities.
- **Auction Listings**: Users can create new auction listings, including setting a starting bid and description.
- **Bidding**: Users can place bids on active listings, with real-time updates on the highest bid.
- **Comments**: Users can leave comments on listings for others to see.
- **Categories**: Listings are organized into categories for easy browsing.
- **Watchlist**: Users can add listings to their watchlist for quick access.

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Version Control**: Git, GitHub

## Installation

### Prerequisites
- Python 3.x
- Django
- SQLite

### Steps
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd commerce
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000/` to see the application.




## Usage

### User Registration and Login
1. Navigate to the registration page to create a new account.
2. Login with your credentials.

### Create a Listing
1. After logging in, go to the "Create Listing" page.
2. Fill out the form with details about the item, starting bid, and category.
3. Submit the form to create the listing.

### Bidding on a Listing
1. Browse the listings on the homepage or through categories.
2. Click on a listing to view its details.
3. Enter your bid amount and submit to place a bid.

### Adding Comments
1. On the listing details page, enter your comment in the provided form.
2. Submit the comment to add it to the listing.

### Managing Watchlist
1. While viewing a listing, click "Add to Watchlist" to add it to your watchlist.
2. Access your watchlist from the user menu to see all saved listings.

## Contributing
`https://github.com/suryanshgr22/Commerce.git`
If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to follow the coding standards and include detailed commit messages.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or need further assistance, please feel free to contact me at suryanshgr22@gmail.com.
